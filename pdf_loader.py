from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader('Saylani Welfare Management System.pdf')
data = data.load()

for DOC in data:
    print(DOC.metadata)

# print(data[0])
# print(len(data))