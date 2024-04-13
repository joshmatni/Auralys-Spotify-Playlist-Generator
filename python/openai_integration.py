from openai import OpenAI
import os
import logging
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO)

  

def get_keywords_for_search(prompt: str):
    try:
        client = OpenAI(api_key=os.getenv('OPEN_API_KEY'))
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant skilled in extracting keywords for music searches."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract keywords assuming the response is well-formed
        keywords = completion.choices[0].text.strip()
        logging.info(f"Extracted Keywords: {keywords}")
        return keywords
    except Exception as e:
        logging.error(f"Failed to extract keywords: {str(e)}")
        return None

# Example usage
# user_prompt = "chill vibes with a hint of jazz"
# keywords = get_keywords_for_search(user_prompt)
# print(f"Keywords for Spotify search: {keywords}")

