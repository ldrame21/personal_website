from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Load OpenAI API key from environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')
client = openai.OpenAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer_question():
    question = request.json['question']
    # Call the Chat Completions API
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",  # Use the recommended model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )

    # Extract the assistant's reply from the API response
    answer = response.choices[0].message.content
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
