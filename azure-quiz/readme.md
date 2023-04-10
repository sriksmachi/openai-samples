# Quiz Generator using Azure Open-AI 

## Introduction

This sample demonstrates the value of advanced large language models (LLMs) from Azure Open AI.

### Problem Statement

Screening entry level candidates like engineers on Azure Knowledge is a time taking activity. Traditionally there are two ways
- Personal Interview -  In this method interviewer sits with the candidate to assess the knowledge, though this is the most ideal way it is time taking and hectic specially when you want to screen a large group of candidates.
- Automated Questionnaire - In this method a tool is fed with pre-baked questionnaire and the system pics questions randomly (like Azure Certification Exams). This reduces the overhead to quickly filter, however overtime the questions become stale and need updates.

This tool addresses the above common problems. It is capable of generating sample questionnaire on Azure Topics prompted by the end user, validate the response and also provide explanation for each response. It helps in screening candidates on Azure Knowledge & Training purpose.

## Setup

### Pre-requisites

This sample is tested with WSL , Linux.
Windows users ensure the machine has all dependencies listed in requirements.txt.

- Windows with WSL / Linux machine
- Azure Subscription 
- Azure Open AI Service enabled. For instructions on how to enable click [here](https://aka.ms/oai/access)


###  Model Deployment

Once open AI service is enabled you need to deploy the models before starting to make API calls. 
The following scripts deploys 3 models
- chatgpt (gpt-35-turbo). This is used for generating content for a given topic.
- text-davinci. This is used for generating questions and options as well as the answer for the question.
- text-similarity-ada-001. This is used to find the similarity between answer provided by model and the option choosen by the user.

```
deploy-models.ps1
```

## High level Flow.

The following diagrams shows the high level flow.

![alt text](docs/diagram.png)

### UI Screenshots 


![alt text](docs/app.png)

## Running the application

Run the below command to run the API from root (azure-quiz). Ensure the API key is initialized in `quiz-generator.py'

```
python3 quiz-generator.py
```

Run the below command from folder `quizgen`. 
This application points to API at http://127.0.0.1:5000
```
ng serve
```




