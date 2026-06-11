# Load arXiv papers as LangChain Documents

from langchain_community.document_loaders import ArxivLoader

loader = ArxivLoader(query="large language models",load_max_docs=2)

documents = loader.load()

print("Number of documents loaded:", len(documents))

print("\n==============================")

# Iterate through each paper
for i, doc in enumerate(documents, 1):
    print(f"\n--- Paper {i} ---")
    
    print("\nMetadata:")
    for key, value in doc.metadata.items():
        print(f"{key}: {value}")
    
    print("\nAbstract Preview:\n")
    print(doc.page_content[:500])
    
    print("\n==============================")