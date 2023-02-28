from sentence_transformers import SentenceTransformer
import nltk
import hnswlib
import time
import numpy as np



model = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-dot-v1')
index = hnswlib.Index(space = 'cosine', dim = 768)

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
text = open('badeconomy.txt').read()

sentences = tokenizer.tokenize(text)

index.init_index(max_elements = len(sentences), ef_construction = 2000, M = 100)


before = time.time()
embeddings = model.encode(sentences)
num_elements = len(embeddings)
# Element insertion (can be called several times):
data_labels = np.arange(num_elements)
index.add_items(embeddings, data_labels)
print("import took {}".format(time.time() - before))

while True:
    q = input("query:")
    vec = model.encode([q])[0]
    labels, distances = index.knn_query(vec, k=1)
    for i in range(len(labels)):
        sn = data_labels[labels[0][i]]
        print(sentences[sn], distances[0][i])

#index.save_index("test.bin")

