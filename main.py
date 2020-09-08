#HEAPSORT
import matplotlib.pyplot as plt
import random
import time

lista=[]
tamanhos= [20000, 30000, 40000, 50000, 60000]
tempos=[]
def geraLista(tamanho):
  x=[]
  for i in range(tamanho): x.append(i)
  random.shuffle(x)
  return x

def geraListaPiorCaso(tamanho):
  x=[]
  for i in range(tamanho,0,-1):
    x.append(i)
  return x

def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)
    return alist
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1
 
def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)
 
for i in tamanhos:
  print("comecei")
  lista=geraLista(i)
  #print(lista)
  #lista=geraListaPiorCaso(i)
  print("comecei dnv")
  now=time.time()
  lista=heapsort(lista)
  then=time.time()
  #print(lista)
  print("acabei dnv")
  tempos.append(then-now)
# Plot the data
plt.plot(tamanhos,tempos)
print(tempos)
# Show the plot
plt.show()
