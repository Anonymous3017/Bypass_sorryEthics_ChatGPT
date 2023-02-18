import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

API_KEY = "Your_API_KEY"

def query_openai_api(prompt):
    url = 'https://api.openai.com/v1/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'model': 'text-davinci-003',
        'prompt': prompt,
        'max_tokens': 4000,
        'temperature': 1.0
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    choices = response.json()['choices']
    return [choice['text'] for choice in choices]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/query', methods=['POST'])
def query():
    prompt = request.form['prompt']
    output = query_openai_api(prompt)
    return render_template('query.html', prompt=prompt, output=output)

if __name__ == '__main__':
    app.run(debug=True)
