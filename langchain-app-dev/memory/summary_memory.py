from utilities_langchain import *
chat = create_chat_model()
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from prompt_toolkit import prompt

# create a long string
schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory = ConversationSummaryBufferMemory(llm=chat, max_token_limit=100)
memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"}, 
                    {"output": f"{schedule}"})
memory.load_memory_variables({})

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