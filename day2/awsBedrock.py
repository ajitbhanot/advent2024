import boto3
import json


# bedrock = boto3.client(service_name='bedrock',
#                        region_name='us-east-1',
#                        aws_access_key_id=AWS_KEY,
#                        aws_secret_access_key=AWS_SECRET_KEY)
# response = bedrock.list_foundation_models(byProvider="anthropic")
#
# for summary in response["modelSummaries"]:
#     print(summary["modelId"])

system_prompt = "Extract shipping information from the email "
# modelId obtained from printing out modelIds in previous step
modelId = 'anthropic.claude-3-5-sonnet-20240620-v1:0'

### parameters for the LLM to control text-generation
# temperature increases randomness as it increases
temperature = 0.5
# top_p increases more word choice as it increases
top_p = 1
# maximum number of tokens to generate in the output
max_tokens_to_generate = 250
messages = [{"role": "user", "content": "Hello, world, tell me a funny poem"},
            {"role": "assistant", "content": "Here is a haiku poem for you:\n\nLaughing out loud\nAt silly jokes and stories\nBringing joyful smiles"},
            {"role": "user", "content": "I don't want to smile"}]

bedrock_runtime = boto3.client(service_name='bedrock-runtime',
                               region_name='us-east-1',
                               aws_access_key_id=AWS_KEY,
                               aws_secret_access_key=AWS_SECRET_KEY)

body = json.dumps({
    "messages": messages,
    "system": system_prompt,
    "max_tokens": max_tokens_to_generate,
    "temperature": temperature,
    "top_p": top_p,
    "anthropic_version": "bedrock-2023-05-31"
})
response = bedrock_runtime.invoke_model(body=body, modelId=modelId, accept="application/json", contentType="application/json")
response_body = json.loads(response.get('body').read())
result = response_body.get('content', '')
print(result)