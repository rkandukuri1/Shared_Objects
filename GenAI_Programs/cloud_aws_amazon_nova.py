import boto3
import json

# Create Bedrock Runtime client
client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

prompt = input("Enter your prompt: ")

request_body = {
    "messages": [
        {
            "role": "user",
            "content": [{"text": prompt}]
        }
    ]
}

response = client.invoke_model(
    modelId="amazon.nova-lite-v1:0",
    body=json.dumps(request_body)
)

response_body = json.loads(response["body"].read())

print(response_body["output"]["message"]["content"][0]["text"])