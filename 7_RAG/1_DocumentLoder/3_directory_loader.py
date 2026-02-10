from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='DataPath',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load() # load one by one and release the memory 
docs1 = loader.load() # load entire stuff in one go

for document in docs:
    print(document.metadata)