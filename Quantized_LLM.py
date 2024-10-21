from langchain_community.llms import Ollama
model = Ollama(model = 'llama2')
prompt = 'who are you?'
print(model.invoke(prompt))

