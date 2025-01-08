import logging
import os

import azure.identity
import openai
from dotenv import load_dotenv

load_dotenv()
# Change to logging.DEBUG for more verbose logging from Azure and OpenAI SDKs
logging.basicConfig(level=logging.WARNING)


if not os.getenv("AZURE_OPENAI_SERVICE") or not os.getenv("AZURE_OPENAI_GPT_DEPLOYMENT"):
    logging.warning("AZURE_OPENAI_SERVICE and AZURE_OPENAI_GPT_DEPLOYMENT environment variables are empty. See README.")
    exit(1)


credential = azure.identity.DefaultAzureCredential()
token_provider = azure.identity.get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")

client = openai.OpenAI(
    base_url="https://Phi-3-5-mini-instruct-klelm.eastus2.models.ai.azure.com/v1/",
    api_key=os.getenv("AZURE_INFERENCE_KEY"),
)

client = openai.AzureOpenAI(
    api_version="2024-03-01-preview",
    azure_endpoint=f"https://{os.getenv('AZURE_OPENAI_SERVICE')}.openai.azure.com",
    azure_ad_token_provider=token_provider,
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_GPT_DEPLOYMENT"),
    temperature=0.7,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that makes lots of cat references and uses emojis."},
        {"role": "user", "content": "Write a haiku about a hungry cat who wants tuna"},
    ],
)

print("Response: ")
print(response.choices[0].message.content)
