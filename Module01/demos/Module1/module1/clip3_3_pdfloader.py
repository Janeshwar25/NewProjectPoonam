# Load a PDF file as LangChain Documents

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("../data/my_files/sports_overview.pdf") 
documents = loader.load()

print("Number of documents:", len(documents))

print(f"\nCONTENT:\n{documents[0].page_content}")
print(f"\nMETADATA:\n{documents[0].metadata}")