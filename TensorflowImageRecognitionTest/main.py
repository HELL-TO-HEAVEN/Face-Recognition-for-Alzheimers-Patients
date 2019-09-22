from easyfacenet.simple import facenet

images = ['IMG_7268.JPG', "IMG_7269.JPG", "IMG_7270.JPG"]

aligned = facenet.align_face(images)
embeddings = facenet.embedding(aligned)
comparisons = facenet.compare(aligned)

print("Is image 1 and 2 similar? ", bool(comparisons[0][1]))
print("Is image 1 and 3 similar? ", bool(comparisons[0][2]))
