import numpy as np

# Endeksleme
A = np.array([1,2,3,4,5,6,7])
A1 = A[1]
print(A1) # "2"
A2 = A[4]
print(A2) # "5"
A3 = A[-4]
print(A3)
# -'ler ile index numarası belirteceğimiz zaman -n'den sola doğru gideriz. (n = eleman sayısı) n!= index numarası
A4 = A[3:]
print(A4) # "4,5,6,7"

B = np.array(
    [1,2,3,4,5,6,7],
    dtype=int
)
B1 = B[B < 4]
print(B1) # "1,2,3"
B2 = B[B > 4] # "5,6,7"
print(B2) # "1,2,3"
B3 = (B > 4)
print(B[B3])
