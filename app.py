from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
# get Hugging Face API Key
HF_API_KEY = os.getenv("HF_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        generated_text = generate_text(prompt)
        return render_template('index.html', prompt=prompt, generated_text=generated_text)
    return render_template('index.html')

def generate_text(prompt):
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }
    json_data = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }
    response = requests.post(
        "https://api-inference.huggingface.co/models/gpt2",
        headers=headers,
        json=json_data
    )
    if response.status_code == 200:
        result = response.json()
        return result[0]['generated_text']
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
