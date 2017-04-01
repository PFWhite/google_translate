import numpy
from numpy import linalg

#Given X, a numpy.array matrix object with each element as a float:

class PCA(object):

    def __init__(self, X):
        self.X = X
        self.val = numpy.array([])
        self.vec = numpy.array([])
        self.m = numpy.array([])
        self.k = 0

    def calc(self):
        R = self.X
        for i in range(len(self.X[1])):
            w = numpy.array([])
            for j in range(len(self.X)):
                w = numpy.append(w, float(self.X[j][i]))
            self.m = numpy.append(self.m, numpy.mean(w))
            for j in range(len(w)):
                w[j] -= self.m[i]
        S = numpy.cov(R.T)
        eigen = linalg.eig(S)
        self.val = eigen[0]
        self.vec = eigen[1]
        for i in range(len(self.val)):
            if self.val[i] > 0.9:
                self.k += 1
        self.E = self.vec[:,0:(self.k+1)]
        self.P = numpy.matmul(R,self.E).real


#self.P will return principal components.
#self.E will return eigenvectors used, including imaginary elements
#self.val will return all eigenvalues
#self.vec will return all eigenvectors used
#self.k will return number of eigenvalues used
#self.m will return means used to calculate stuff in PCA; not useful really, unless given a new word we want to run PCA on. Not really applicable to our project.

