from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai_api_key  = os.getenv('OPENAI_API_KEY')

def create_chat_model(temperature=0.0, model="gpt-3.5-turbo"):
    return ChatOpenAI(temperature=temperature, model=model, api_key=openai_api_key)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'