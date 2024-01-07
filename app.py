from flask import Flask, render_template, request
from langchain.memory import ConversationBufferMemory
from chatbot.langchain_chat.rag import get_reply

app = Flask(__name__)
app.static_folder = 'static'

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    bot_reply =  get_reply(userText, memory)
    memory.save_context({'input':userText},{'output':bot_reply})
    return bot_reply

if __name__ == "__main__":
    app.run()