# Load a text file as LangChain Documents

from langchain_community.document_loaders import TextLoader

loader = TextLoader("../data/my_files/sports.txt", encoding="utf-8")
documents = loader.load()

print(documents[0].page_content)
print(documents[0].metadata)