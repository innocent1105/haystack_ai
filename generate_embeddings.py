from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Sold 50 units of iPhone 14 in January"
vector = model.encode(text).tolist() 

print(vector)
