
from numpy import zeros
from scipy.linalg import svd
from math import log
from numpy import asarray, sum
import numpy as numpy
class LSA(object):
    def __init__(self, stopwords, ignorechar):
        self.stopwords = stopwords
        self.ignorechar = ignorechar
        self.word_dict = {}
        self.count = 0

    def parse(self, doc):
        word = doc.split()
        for i in word:
            i = i.lower().translate(None, self.ignorechar)
            if i in self.stopwords:
                continue
            elif i in self.word_dict:
                self.word_dict[i].append(self.count)
            else:
                self.word_dict[i] =  [self.count]
                self.count += 1

    def build(self):
        self.keys = [k for k in self.word_dict.keys() if len(self.word_dict[k]) > 1]
        self.keys.sort()
        self.A = zeros([len(self.keys), self.count])
        for i, k in enumerate(self.keys):
            for d in self.word_dict[k]:
                self.A[i, d] += 1

    def transform(self):
        word_doc_count = sum(self.A, axis=0)
        doc_word_count = sum(asarray(self.A > 0), axis=1)
        rows, cols = self.A.shape
        for i in range(rows):
            for j in range(cols):
                if word_doc_count[j] != 0 and doc_word_count[i] !=0:
                    self.A[i, j] = (self.A[i, j] / word_doc_count[j]) * log(float(cols) / doc_word_count[i])

    def printMatrix(self):
        print self.A

    def calc_svd(self):
        self.U, self.S, self.Vt = svd(self.A)

def query (A, q , docs):
    norm_q = q/numpy.linalg.normalize(q)
    for i in len(docs):
        similarity = numpy.dot(norm_q, A[:i].T)
