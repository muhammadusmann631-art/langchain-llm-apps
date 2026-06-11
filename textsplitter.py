from langchain.text_splitter import CharacterTextSplitter

text = '''
Yeh error is wajah se aa rahi hai ke PyPDFLoader naam ka package PyPI par directly available nahi hai. Iska matlab hai ke aap galat package name use kar rahe ho. 

Sahi tarika yeh hai:
PyPDFLoader actually LangChain ecosystem ka part hai — use karne ke liye aapko langchain-community ya langchain ke andar se import karna padta hai.
'''
split = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
    separator = "\n"
    
)
# split.tex