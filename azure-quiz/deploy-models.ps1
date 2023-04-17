
$resourceGroup = 'OAIResourceGroup'
$location = 'eastus'
$subscriptionId = '6a01260f-39d6-415f-a6c9-cf4fd479cbec'

# this should be globally unique
$openAIResourceName = 'openai-samples'

# the model names declared here are used in the script 'quiz-generator.py', make sure they match.
$davince = 'text-davinci-003'
$ada = 'text-similarity-ada-001'
$chatgpt = 'gpt-35-turbo'

# create resource group
az group create --name $resourceGroup --location $location

# create OpenAI resource
Write-Host "Creating OpenAI resource..."
az cognitiveservices account create `
-n $openAIResourceName `
-g $resourceGroup `
-l $location `
--kind OpenAI `
--sku s0 `
--subscription $subscriptionId

# get the key
Write-Host "Getting key..."
$key = (az cognitiveservices account keys list `
-n $openAIResourceName `
-g $resourceGroup `
| jq -r .key1)

# get the endpoint
Write-Host "Getting endpoint..."
$endpoint = (az cognitiveservices account show --name $openAIResourceName --resource-group $resourceGroup | jq -r .properties.endpoint)
Write-Host "Endpoint : " $endpoint

# Copy the key to use in code for key based authentication
Write-Host "Key : " $key

# deploy davince models
Write-Host "Deploying davince models..."
az cognitiveservices account deployment create `
   -g $resourceGroup `
   -n $openAIResourceName `
   --deployment-name $davince `
   --model-name $davince `
   --model-version "1"  `
   --model-format OpenAI `
   --scale-settings-scale-type "Standard"

# deploy ada models
Write-Host "Deploying ada models..."
az cognitiveservices account deployment create `
   -g $resourceGroup `
   -n $openAIResourceName `
   --deployment-name $ada `
   --model-name $ada `
   --model-version "1"  `
   --model-format OpenAI `
   --scale-settings-scale-type "Standard"

# deploy chatgpt models
Write-Host "Deploying chatgpt models..."
az cognitiveservices account deployment create `
   -g $resourceGroup `
   -n $openAIResourceName `
   --deployment-name $chatgpt `
   --model-name $chatgpt `
   --model-version "0301"  `
   --model-format OpenAI `
   --scale-settings-scale-type "Standard"

## Clean up
# az group delete -g $resourceGroup --yes 


