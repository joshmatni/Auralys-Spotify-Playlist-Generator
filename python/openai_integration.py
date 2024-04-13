from openai import OpenAI
import os
import logging
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO)

def get_keywords_for_search(prompt: str):
    try:
        client = OpenAI(api_key=os.getenv('OPEN_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant skilled in extracting keywords from the prompt for playlist generation and music."},
                {"role": "user", "content": prompt}
                # if the prompt doesnt have a minimum of 15 words generate some synonms then
            ],
            temperature=0.3,
            max_tokens=60
        )
        keywords = response.choices[0].message.content
        logging.info(f"Extracted Keywords: {keywords}")
        return keywords
    except Exception as e:
        logging.error(f"Failed to extract keywords: {str(e)}")
        return None

user_prompt = "generate me a playlist that makes me happy for the day"
keywords = get_keywords_for_search(user_prompt)
print(f"Keywords for Spotify search: {keywords}")

