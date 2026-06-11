# Load multiple web pages as LangChain Documents

from langchain_community.document_loaders import WebBaseLoader

urls = [
    "https://docs.python.org/3/tutorial/interpreter.html",
    "https://docs.python.org/3/tutorial/introduction.html"
]

loader = WebBaseLoader(urls)

documents = loader.load()

print("Number of documents loaded:", len(documents))

print("\n==============================")

# Loop through each document
for i, doc in enumerate(documents, 1):
    print(f"\n--- Document {i} ---")
    
    print("\nMetadata:")
    for key, value in doc.metadata.items():
        print(f"{key}: {value}")
       
    # Clean and preview content
    print("\nPreview:\n")
    clean_text = " ".join(doc.page_content.split())
    print(clean_text[:500])   # show first 500 characters
    
    print("\n==============================")