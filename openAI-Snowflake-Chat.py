import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv("env.demo")

client = OpenAI(
    api_key=os.getenv("SNOWFLAKE_PAT"),
    base_url=f"https://{os.getenv('SNOWFLAKE_ACCOUNT_IDENTIFIER')}.snowflakecomputing.com/api/v2/cortex/v1"
)

stream = client.chat.completions.create(
    model=os.getenv("SNOWFLAKE_MODEL"),
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "How does a snowflake get its unique pattern?"}
    ],
    stream=True
)

for event in stream:
    print(event.choices[0].delta.content or "", end="")