from langchain_ollama import OllamaLLM
model = OllamaLLM(model = 'llama2')
prompt = 'who are you?'
print(model.invoke(prompt))