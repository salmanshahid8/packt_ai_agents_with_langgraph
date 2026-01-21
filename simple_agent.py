import os
from pprint import pprint

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)

model_id = "gemini-3-flash-preview"

model_info = client.models.get(model=model_id)

print(f"Model: {model_info.display_name}")
print(f"Max Output Tokens: {model_info.output_token_limit}")

# Set the maximum output tokens in the config
config = types.GenerateContentConfig(
    max_output_tokens=model_info.output_token_limit,
    temperature=0.7,
)

response = client.models.generate_content(
    model=model_id,
    contents="what is the capital of greenland?",
    config=config,
)
pprint(response.text)

# load_dotenv()

# openai_api_key = os.getenv("OPENAI_API_KEY")

# llm_name = "gpt-3.5-turbo"

# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Why people are attracted towards luxury?"},
# ]

# client = OpenAI(api_key=openai_api_key)

# response = client.chat.completions.create(model=llm_name, messages=messages)

# pprint(response)
