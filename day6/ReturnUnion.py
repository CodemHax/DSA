from numpy.ma.core import append


def findUnion( a, b):
    union = sorted(set( a + b))
    return union


if __name__ == "__main__" :
    a = [-8 ,-3 ,-3 ,-2, 0 ,1 , 2 ,2 ,6]
    b = [-9 ,-9, 0]
    print(findUnion(a,b))