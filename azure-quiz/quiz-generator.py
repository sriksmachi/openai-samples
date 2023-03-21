#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import json
import requests
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

# request parameters
temperature=0.5
max_tokens=800
top_p=0.95

mock_url = "https://137edb13-b1a9-49dd-b3a6-fc81f72953d8.mock.pstmn.io"
openai.api_type = "azure"
openai.api_base = "https://vism-openai.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = ""

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
def getQuestionnaireContent():
    # creating a list of messages to track the conversation
    topic = request.form.get('topic')
    messages = [{"sender":"user","text":topic}]
    # # topicResponse = openai.Completion.create(
    #   engine="vism-chatgpt",
    #   prompt= create_prompt(system_message, messages),
    #   temperature=0.5,
    #   max_tokens=800,
    #   top_p=0.95,
    #   frequency_penalty=0,
    #   presence_penalty=0,
    #   stop=["<|im_end|>"])
    topicResponse = requests.request("POST", mock_url + '/content', headers={}, data="").text
    topicText = (json.loads(topicResponse)["choices"][0]["text"])
    print(topicText)

    # questionnaireResponse = openai.Completion.create(
    #   engine="vism-davinci-003",
    #   prompt="Generate a multiple choice quiz from the text below. Quiz should contain at least 3 questions. Each answer choice should be on a separate line, with a blank line separating each question.\n\n "  + response,
    #   temperature=0.8,
    #   max_tokens=500,
    #   top_p=1,
    #   frequency_penalty=0,
    #   presence_penalty=0.5,
    #   best_of=1,
    #   stop=None)
    questionsResponse = requests.request("POST", mock_url + '/questionnaire', headers={}, data="").text
    questions = (json.loads(questionsResponse)["choices"][0]["text"])
    print(questions)
    return questions

@app.route('/validate', methods=['POST'])
def validate():
    topicResponse = requests.request("POST", mock_url + '/content', headers={}, data="").text
    topicText = (json.loads(topicResponse)["choices"][0]["text"])
    # response = openai.Completion.create(
    #   engine="vism-davinci-003",
    #   prompt= topicText + "\n\nAnswer the following question from the text above.\n\n" + "Q: How does Azure Functions scale?\n",
    #   temperature=0.7,
    #   max_tokens=256,
    #   top_p=1,
    #   frequency_penalty=0,
    #   presence_penalty=0,
    #   best_of=1,
    #   stop=["\n"])
    qna_response = requests.request("POST", mock_url + '/qna', headers={}, data="").text
    qna_text = (json.loads(qna_response)["choices"][0]["text"])
    return qna_text


if __name__ == '__main__':
   app.run()