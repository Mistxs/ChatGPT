from flask import Flask, request, jsonify, render_template
import openai
from config import openaikey

openai.api_key = openaikey
app = Flask(__name__)

message_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json['text']
    answers = chat_with_model(message)
    return jsonify({"message": answers})


def chat_with_model(message):
    message_history.append({"role": "user", "content": message})
    messages = [
                   {"role": "system", "content": "Ты - красивый бот с именем Инна"}
               ] + message_history
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": reply})
    return reply

if __name__ == "__main__":
    app.run(port=5125)
