
# coding: utf-8

# In[3]:


import numpy as np


W_all = 10
N = 3
Matrix = np.zeros((W_all + 1, N*2))
C = np.zeros(N)
W = np.zeros(N)
W[0] = 4
W[1] = 3
W[2] = 2

C[0] = 8
C[1] = 7
C[2] = 4

counter_N = np.arange(W_all+1)

max_index = 0
for i in counter_N:
    number = i // W[0]
    counter_number = np.arange(number+1)
    max_list = list()
    for counter in counter_number:
        max_list.append(C[0]*counter)
    max_index = max_list.index(max(max_list))
    
    Matrix[i][1] = max_index
    Matrix[i][0] = C[0]*max_index


for n in range(2,N+1):
    max_index = 0
    for i in counter_N:
        number = i // W[n-1]
        counter_number = np.arange(number+1)
        max_list = list()
        for counter in counter_number:
            t = int(2*(n - 2))
            u = int(C[n-1]*counter)
            r = int(i - counter*W[n-1])
            max_list.append(u + Matrix[r][t])
        max_index = max_list.index(max(max_list))

        Matrix[i][2*n-1] = max_index
        Matrix[i][2*n-2] = max_list[max_index]


number = N
counter_N = N
amount_list = list()
W_sum = 0
for i in range(1, N+1):
    y = int(W_all-W_sum)
    o = int(2*N-1)
    amount_list.append(Matrix[y][o])
    W_sum = W_sum + amount_list[i-1]*W[counter_N-1]
    counter_N = counter_N - 1
    N = N - 1

amount_list.reverse()
numbers = np.arange(number)
for i in numbers:
    print(str(i+1) + "-ого товара необходимо взять в количестве: " + str(amount_list[i]))


# In[2]:


t = 0
input(t)

