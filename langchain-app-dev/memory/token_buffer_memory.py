from utilities_langchain import *
chat = create_chat_model()
from langchain.chains import ConversationChain
from langchain.memory import ConversationTokenBufferMemory
from prompt_toolkit import prompt

memory = ConversationTokenBufferMemory(max_token_limit=50)
conversation = ConversationChain(
    llm=chat, 
    memory = memory,
    verbose=False
)

while 1:
    user_input = prompt('>')
    if user_input == "bye":
        break
    response = conversation.predict(input=user_input)
    print(f'{bcolors.OKGREEN}{response}{bcolors.ENDC}')

print(memory.buffer)
print(memory.load_memory_variables({}))