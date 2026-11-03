from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

texts = ["I forgot my password", "How do I reset my password?"]
numbers = model.encode(texts)

print(numbers)