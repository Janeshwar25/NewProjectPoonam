# Load a CSV file as LangChain Documents

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("../data/my_files/results.csv")
documents = loader.load()

print("Total rows loaded:", len(documents))

print(f"\nCONTENT:\n{documents[0].page_content}")
print(f"\nMETADATA:\n{documents[0].metadata}")

print(f"\nCONTENT:\n{documents[1].page_content}")
print(f"\nMETADATA:\n{documents[1].metadata}")