import langchain
from langchain_community.document_loaders import TextLoader
 
data = TextLoader('football.txt',encoding="utf-8")
loader_data = data.load()

# print(loader_data)
# print(type(loader_data))
# print(len(loader_data))
# pritn(loader_data[])

print(loader_data)
print(loader_data[0].page_content)
print(loader_data[0].metadata)