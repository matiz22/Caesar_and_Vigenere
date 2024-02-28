import os
import requests
from dotenv import load_dotenv


class Ollama:

    @staticmethod
    def get_ollama_response(possible: list[str]) -> str:
        load_dotenv()
        endpoint = os.getenv('ENDPOINT')
        model = os.getenv('MODEL')
        prompt = (f'From this list of words return only those which are real english words not shortcuts\n'
                  f'Here is a list to choose a words:\n')
        for word in possible:
            prompt += word + '\n'

        data = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(endpoint, json=data)
        if response.status_code == 200:
            return '\nAi response:' + response.json()['response']
        else:
            return str(response.status_code)
