# Build an end-to-end langchain app using Vector database.

## Pre-requisites
To run this code, you will need the following:

1. Azure Subscription with Azure Open AI Enabled. More details [here](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/limited-access)
1. A deployment of the `text-embedding-ada-002` embedding model in your Azure OpenAI service. 
1. Azure OpenAI connection and model information:
   - OpenAI API key
   - OpenAI embedding model deployment name
   - OpenAI API version
1. Access to Cognitive Search vector search private preview, since this is the vector search-enabled version of this sample. You can sign up [here](https://aka.ms/VectorSearchSignUp).

## Infra setup

1. Create Open AI Service & deploy models
   - `text-embedding-ada-002`
   - `text-davinci-003`
Instructions to deploy models available [here](https://microsoftlearning.github.io/mslearn-openai/Instructions/Labs/01-get-started-azure-openai.html)
2. Create Azure Cognitive Service Search with Vector DB. 
   - Create Azure Cognitive Services Search
   - Enable Vector DB
   - Create Index





