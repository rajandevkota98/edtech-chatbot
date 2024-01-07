import dotenv
import os
import dotenv
import os
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from chatbot.utils import read_file
from chatbot.constant.application import POLICY_FILE_PATH

def get_reply(user_input: str, memory: str):
    course_content = read_file(POLICY_FILE_PATH)
    # course_content.append()
    dotenv.load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    llm = ChatOpenAI()

    prompt_messages = [
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot  from Digital Sikhshya having a conversation with a student, please provide very short answer and precise to the question of the student, try to give in in 20 words."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]

    if course_content:
        prompt_messages.insert(1, SystemMessagePromptTemplate.from_template(course_content))

    prompt = ChatPromptTemplate(messages=prompt_messages)
    conversation = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)
    conversation_input = {"question": user_input}
    bot_output = conversation(conversation_input)
    bot_reply = bot_output['text']
    return bot_reply

