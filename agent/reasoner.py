from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def decide(context: str):
    prompt = open("prompts/reasoning_prompt.txt").read()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": context}
        ]
    )

    return response.choices[0].message.content
