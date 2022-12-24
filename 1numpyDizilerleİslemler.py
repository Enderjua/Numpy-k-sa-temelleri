import numpy as np # Numpy kütüphanesini dahil etmek
import time # Time kütüphanesini dahil etmek

A = np.array([1,2,3,4,5,6]) # Numpy ile dizi oluşturma
print(A) # Diziyi ekrana yazdırma (output: [1 2 3 4 5 6])
print(A.shape) # Dizinin boyutunu öğrenme (output: (6,))
A = A.reshape(6,1) # Dizinin boyutunu (6,1) olarak değiştirir
print(A) 
print(A.shape) # output: (6,1)
# Çok boyutlu dizi oluşturma
B = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(B)
print(B.shape)

# np.zeros()
C = np.zeros(3, dtype=int) # Numpy ile içeriği 0 olan dizi oluşturmak. (dtype, arrayin type'ını şekillendirmek için kullanılır)
print(C)
print(type(C)) # Array'in türünü yazdırmak. (output: "numpy.ndarray")
print(C.shape)

# no.ones()
D = np.ones(3, dtype=int) # Numpy ile içeriği 1 olan dizi oluşturmak.
print(D)

# np.empty()
E = np.empty(4, dtype=int) # Numpy ile içeriği rastgele olan dizi oluşturmak. Bu dizilerin amacı zeros ve ones'tan daha hızlı olmasıdır.
print(E)
# Numpy Arrayler ile Python Arrayler arasındaki farkı anlamak için bir deney!
start_time = time.time()
E = np.empty(100000, dtype=int)
E ** 2
Time = time.time() - start_time

start_time_2 = time.time()
E2 = range(100000)
[ i ** 2 for i in E2 ]
Time2 = time.time() - start_time_2
print(Time2 / Time)


# np.arange()
F = np.arange(12) # 0'dan 11'e kadar içeriğe sahip olan dizi oluşturur
print(F)
# Basit arange kullanımı:
# np.arange(ilkSayı, sonSayı, artışMiktarı)
F = np.arange(4, 14, 2)
print(F)

# np.linspace()
# Basit linspace kullanımı:
# np.linspace(ilkSayı, sonSayı, doğrusalKesimNoktası)
G = np.linspace(4, 10, 6)
print(G)
# Egzersiz, tahmin etme yarışması
G = np.linspace(0, 20, 10)
print(G)


# np.sort() Öğe sıralama
H = np.array([5,4,7,2,16,9,24,6,12,0])
H = np.sort(H) # Küçükten büyüğe doğru sıralama
print(H)

# np.concatenate() Öğe birleştirme
A1 = np.array([1,2,3,45,6,7,8,])
A2 = np.array([5,7,24,6,8,1])
A3 = np.concatenate((A1,A2), axis=0)
A3 = np.sort(A3)
print(A3)

# ndim, shape, size
B1 = np.array([[
    [1,2,3,4],
    [1,2,3,4],

    [4,5,7,2],
    [6,8,2,4],

    [4,2,7,2],
    [6,1,2,4]
]])
print(B1.shape) # boyutu
print(B1.size) # size'ı
print(B1.ndim) # parantez içi

# np.reshape()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
C1 = np.arange(6, dtype=int)
C2 = C1.reshape(C1, newshape=(3,1), order='C')
print(C2)
