#Note: The openai-python library support for Azure OpenAI is in preview.
import openai
import json
import pandas as pd
from flask import Flask, request
from flask_cors import CORS, cross_origin
from openai.embeddings_utils import get_embedding, cosine_similarity

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

session = dict()
cors = CORS(app)

# request parameters
temperature=0.5
max_tokens=800
top_p=0.95
similarityModel = "text-similarity-ada-001"
gptModel = "vism-davinci-003"
chatgptModel = "vism-chatgpt"

mock_url = "https://137edb13-b1a9-49dd-b3a6-fc81f72953d8.mock.pstmn.io"
openai.api_type = "azure"
openai.api_base = "https://vism-openai.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "785b8d732f7e4029bd3c1be42ca40c5d"


# defining a function to create the prompt from the system message and the messages
def create_prompt(system_message, messages):
    prompt = system_message
    message_template = "\n<|im_start|>{}\n{}\n<|im_end|>"
    for message in messages:
        prompt += message_template.format(message['sender'], message['text'])
    prompt += "\n<|im_start|>assistant\n"
    return prompt

# defining the system message
system_message_template = "<|im_start|>system\n{}\n<|im_end|>"
system_message = system_message_template.format("")


@app.route('/content', methods=['POST'])
@cross_origin()
def getQuestionnaireContent():
    # creating a list of messages to track the conversation
    topic = request.form.get('topic')
    print("Topic: ",topic)
    topicText = getTopicText(topic)
    print("Topic Text: ", topicText)
    questionnaire = getQuesstionnaire(topicText)
    print("Questions: ", questionnaire)
    qna_arr = convertToArr(questionnaire)
    session["topic"] = topic
    session["topicText"] = topicText
    session['questions'] = qna_arr
    return qna_arr

@app.route('/validate', methods=['POST'])
@cross_origin()
def validate():
    topicResponse = session['topicText']
    user_response = request.form.get('userresponse')
    qna_arr = session['questions']
    print("User Response:", user_response)
    userresp_arr = user_response.split(',')
    responses = []
    for userresp in userresp_arr:
        response = []
        q_choice = int(userresp.split('-')[0])
        a_choice = int(userresp.split('-')[1])
        qna = qna_arr[q_choice]
        qna_text = getQnAResponse(topicResponse, qna[0])
        print('Model ans:', qna_text)
        df_answers = pd.DataFrame()
        df_answers['text'] = [qna[1], qna[2], qna[3], qna[4]]
        df_answers['curie_search'] = df_answers["text"].apply(lambda x : get_embedding(x, engine = similarityModel))
        embedding = get_embedding(qna_text, engine=similarityModel )
        df_answers['similarities'] = df_answers.curie_search.apply(lambda x: cosine_similarity(x, embedding))
        res = int(df_answers.sort_values("similarities", ascending=False).head(1).index.values[0])
        print(df_answers)
        print(res, a_choice)
        response.append(res==a_choice)
        response.append(qna_text)
        responses.append(response)
    return responses

def convertToArr(questions):
    qs = questions.split('\n\n')
    q_arr = []
    for q in qs:
        f = q.splitlines()
        if len(f) > 0:
            q_arr.append(f)
    return q_arr

def getQuesstionnaire(topicText):
    questionnaireResponse = openai.Completion.create(
      engine=gptModel,
      prompt="Generate a multiple choice quiz from the text below. Quiz should contain at least 3 questions. Each answer choice should be on a separate line, with a blank line separating each question.\n\n "  + topicText,
      temperature=0.8,
      max_tokens=500,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.5,
      best_of=1,
      stop=None)
    # questionnaireResponse = requests.request("POST", mock_url + '/questionnaire', headers={}, data="").text
    questionnaire = (json.loads(str(questionnaireResponse))["choices"][0]["text"])
    return questionnaire

def getQnAResponse(topicResponse, question):
    print("QnAResponse: ", topicResponse, question)
    question = question.replace(question[0:3], "Q. ")
    qna_response = openai.Completion.create(
      engine=gptModel,
      prompt= topicResponse + "\n\nAnswer the following question from the text above.\n\n" + question + "\n",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      best_of=1,
      stop=["\n"])
    qna_response = str(qna_response)
    app.logger.info('open api qna response ',  qna_response)
    # qna_response = requests.request("POST", mock_url + '/qna', headers={}, data="").text
    qna_response = json.loads(qna_response)["choices"][0]["text"]
    return qna_response

def getTopicText(topic):
    messages = [{"sender":"user","text":topic}]
    topicResponse = openai.Completion.create(
      engine=chatgptModel,
      prompt= create_prompt(system_message, messages),
      temperature=0.5,
      max_tokens=800,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["<|im_end|>"])
    topicResponse = str(topicResponse)
    # topicResponse = requests.request("POST", mock_url + '/content', headers={}, data="").text
    topicText = (json.loads(str(topicResponse))["choices"][0]["text"])
    return topicText

if __name__ == '__main__':
   app.run()