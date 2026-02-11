from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('ipl.pdf')

docs = loader.load()
print(len(docs))

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

response = splitter.split_documents(docs)
# print(response)
# print(response[1].page_content)