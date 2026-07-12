import boto3
import json

client = boto3.client("bedrock-runtime", region_name="ap-south-1")

user_prompt = input("Enter your query: ")

response = client.invoke_model(
    modelId="openai.gpt-oss-20b-1:0",
    body=json.dumps({
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    })
)

print(json.loads(response["body"].read())["choices"][0]["message"]["content"])