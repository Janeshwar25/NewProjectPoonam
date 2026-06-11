# Load Wikipedia articles as LangChain Documents

from langchain_community.document_loaders import WikipediaLoader

loader = WikipediaLoader(
    query="Artificial Intelligence",
    load_max_docs=2   
)

documents = loader.load()

print("Number of documents loaded:", len(documents))

for i, doc in enumerate(documents, 1):
    print(f"\n--- Article {i} ---")
    
    print("\nMetadata:")
    for key, value in doc.metadata.items():
        print(f"{key}: {value}")
    
    print("\nPreview:\n")
    print(doc.page_content[:400])
