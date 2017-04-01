import numpy
from numpy import linalg

#function of a PCA object (from other code) that calculated eigenvalues/vectors
#x is number of dimensions you want the data to be
#note if x > number dimensions PCA already determined to be useful, it will
#just return what was already given.
def PCA_dimension_set(pcaobj, x):
    out = pcaobj.P[:,0:x]
    return(out)

