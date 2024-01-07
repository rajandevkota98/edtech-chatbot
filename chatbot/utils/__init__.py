import os, sys
from chatbot.exceptio import ChatBotException
def read_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        raise ChatBotException(e,sys)
