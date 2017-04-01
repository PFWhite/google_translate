import numpy
from numpy import linalg

#given a vector and a dictionary, will return index of dictionary closest to vector
def nearest_neighbor(vec, data):
    dist = numpy.array([])
    for j in range(len(data[:,0])):
        dist = numpy.append(dist, linalg.norm(vec - data[j,:]))
    out = dist.argmin()
    return(out)

#literally just uses other code to return PCA of word closest to our vector, if we want it
def identify(vec, data):
    j = nearest_neighbor(vec, data)
    out = data[j,:]
    return(out)


