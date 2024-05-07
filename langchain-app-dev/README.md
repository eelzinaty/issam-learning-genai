# LangChain for LLM Application Development
*course link: [https://learn.deeplearning.ai/courses/langchain](https://learn.deeplearning.ai/courses/langchain)*

## LangChain: Models, Prompts and Output Parsers

1. Models: refer to LLM
2. Prompts: style to create input to pass to LLM
3. Output parsers: taking the output of an LLM and make it into structure format that can be used by the user

When you build applications using LLM there is usually repeated models and Langchain is used to maintain and ease the use of these models. Here are some examples:
1. [Use prompt template to create chat template for prompts](./template/prompt_template.py)
2. [Use of output parser to provide output format instructions](./template/output_parser.py)
3. [Then use output parser to parse the model output to a python object](./template/output_parser_formatted.py)


## Memory

When interacting with LLM models they don't remember what you have said before for any of the previous conversations. Which is a problem for many applications like chatbots where conversation are important to remember, thus we need a memory module to have a conversation flow that give the user better interaction experience.

![Langchain Memory Types](./img/lang_chain_memory_types.png?raw=true)
![Langchain Additional Memory Types](./img/lang_chain_additional_memory_types.png?raw=true)



