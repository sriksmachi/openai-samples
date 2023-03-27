
$resourceGroup = 'OAIResourceGroup'
$location = 'eastus'
$subscriptionId = ''

# this should be globally unique
$openAIResourceName = 'samples-openai'

# the model names declared here are used in the script 'quiz-generator.py', make sure they match.
$davince = 'text-davinci-003'
$ada = 'text-similarity-ada-001'
$chatgpt = 'gpt-35-turbo'

az group create --name $resourceGroup --location $location

az cognitiveservices account create `
-n MyOpenAIResource `
-g $resourceGroup `
-l $location `
--kind OpenAI `
--sku s0 `
--subscription $subscriptionId

$key = (az cognitiveservices account keys list `
-n $openAIResourceName `
-g $resourceGroup `
| jq -r .key1)


az cognitiveservices account deployment create `
   -g $resourceGroup `
   -n $openAIResourceName `
   --deployment-name $davince `
   --model-name $davince `
   --model-version "1"  `
   --model-format OpenAI `
   --scale-settings-scale-type "Standard"

az cognitiveservices account deployment create `
   -g $resourceGroup `
   -n $openAIResourceName `
   --deployment-name $ada `
   --model-name $ada `
   --model-version "1"  `
   --model-format OpenAI `
   --scale-settings-scale-type "Standard"

az cognitiveservices account deployment create `
   -g $resourceGroup `
   -n $openAIResourceName `
   --deployment-name $chatgpt `
   --model-name $chatgpt `
   --model-version "1"  `
   --model-format OpenAI `
   --scale-settings-scale-type "Standard"

## Clean up
# az group delete -g $resourceGroup --yes 


