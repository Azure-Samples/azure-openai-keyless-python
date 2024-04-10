import os

import azure.identity
import openai
from dotenv import load_dotenv

load_dotenv()

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)
client = openai.AzureOpenAI(
    api_version="2024-03-01-preview",
    azure_endpoint=f"https://{os.getenv('AZURE_OPENAI_SERVICE')}.openai.azure.com",
    azure_ad_token_provider=token_provider,
)

response = client.chat.completions.create(
    # For Azure OpenAI, the model parameter must be set to the deployment name
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
