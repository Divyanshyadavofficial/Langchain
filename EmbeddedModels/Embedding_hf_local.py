from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Sentences to compare
sentences = [
    "That is a happy person",
    "That is a happy dog",
    "That is a very happy person",
    "Today is a sunny day"
]

# Create embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

# Compute cosine similarity matrix
similarities = util.cos_sim(embeddings, embeddings)

print(similarities.shape)      # (4, 4)
print(similarities)            # Similarity scores
