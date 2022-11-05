from gensim.doc2vec import Doc2Vec
import numpy as np


class KJ:
    def __init__(self):
        self.model = Doc2Vec.load("")
        self.items = []

    def push(self, new_item):
        self.items.push(new_item)

    def abstraction(self):
        vectors = map(lambda d: self.model.get_vector(d), self.items)
        if len(vectors) == 0:
            return ""
        average_vector = np.zeros(vectors[0].shape)
        for vector in vectors:
            average_vector += vector
        average_vector /= len(vectors)
        return self.model.most_similar_by_vector(average_vector)
