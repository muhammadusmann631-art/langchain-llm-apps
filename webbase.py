from langchain_community.document_loaders import WebBaseLoader

url = "https://www.hellomagazine.com/"
load = WebBaseLoader(url)

data =load.load()
print(data[0].page_content)