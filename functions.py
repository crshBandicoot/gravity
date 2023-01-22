def distance(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5


def ort_vector(a, b):

    return ((b[0]-a[0])/distance(a, b), (b[1]-a[1])/distance(a, b))


