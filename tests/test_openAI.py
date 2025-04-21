from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4o-mini",
    input="Hello, I am excited about building an AI agent project for an internship at Coral Protocol"
)
print(response.output_text)

