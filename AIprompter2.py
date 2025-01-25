from dotenv import load_dotenv
import os
load_dotenv()
from openai import OpenAI
client = OpenAI(api_key=os.getenv("api_key"))


def get_AI(prompt):
    #print(f"This is the prompt: {prompt}")

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{prompt} no greetings in your response just respond with what is asked and nothing more "}],
        stream=True,
    )

    output =""

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            #print(chunk.choices[0].delta.content, end="")
            output+= chunk.choices[0].delta.content

    return output
            
# minecraft = get_AI("Hello is this working?")
# print(f"prompt 1: {minecraft}")
# print(f" prompt 2: {minecraft}")