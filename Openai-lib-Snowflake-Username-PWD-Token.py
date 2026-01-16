import os
from openai import OpenAI
from dotenv import load_dotenv
import snowflake.connector
import requests

account=<AccountID>
# Connect with username/password
conn = snowflake.connector.connect(
    user=<UserName>,
    password=<Password>,
    account=account,
    warehouse=<WH>
)

# Get session token from connection
session_token = conn.rest.token


# Use requests directly with Snowflake token format
headers = {
    'Authorization': f'Snowflake Token="{session_token}"',
    'Content-Type': 'application/json'
}

url = f"https://{account}.snowflakecomputing.com/api/v2/cortex/v1/chat/completions"

data = {
    "model": os.getenv("SNOWFLAKE_MODEL"),
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "How does a snowflake get its unique pattern?"}
    ],
    "stream": True
}

response = requests.post(url, json=data, headers=headers, stream=True)
print(response.json())
conn.close()
