import MatrixLibrary as Matrix

v1 = Matrix.generate(3,1)
v2 = Matrix.generate(3,1)
Matrix.populate(v1)
Matrix.populate(v2)

a = Matrix.angleBetweenVectors(v1, v2)
print(a)