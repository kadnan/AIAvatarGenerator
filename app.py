from flask import Flask, render_template, jsonify, request
from openai import OpenAI
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_avatar():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API")
    data = json.dumps(request.json)
    prompt = f"Generate an avatar based on the following specifications given in JSON format, ensuring all details are accurately reflected and styled as described. You must NOT write any text on the generated image\n {data}"
    client = OpenAI(
        api_key=openai_api_key)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    response = {
        "image_url": image_url
    }
    return jsonify(response)


@app.route('/')
def home():
    return render_template('index.html')  # Ensure this HTML file is in the 'templates' folder


if __name__ == '__main__':
    app.run(debug=True)
