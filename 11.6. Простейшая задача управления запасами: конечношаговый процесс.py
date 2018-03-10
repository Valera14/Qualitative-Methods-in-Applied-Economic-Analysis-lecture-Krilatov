
# coding: utf-8

# In[9]:


import numpy as np

A = 13
B = 2
H = 1
R_k = 5
T_k = 4
S_k = 3
N = 6

def C_k(X):
    if X>0:
        return A + B*X
    elif X == 0:
        return 0

def H_k(Y):
    return H*Y

def C_k_all(X, Y):
    return C_k(X) + H_k(Y)

def F_1(Y):
    if Y<= S_k:
        return C_k_all(S_k - Y, 0)
    elif Y>= S_k:
        return C_k_all(0, Y - S_k)

def X_1(Y):
    if Y<= S_k:
        return S_k - Y
    elif Y>=S_k:
        return 0
    
F_all_list = list()
X_all_list = list()
F = list()
X = list()

for Y in range(0, T_k+1):
    F.append(F_1(Y))
    X.append(X_1(Y))

F_all_list.append(F)
X_all_list.append(X)

temple_row = list()
for k in range(2, N+1):
    F = list()
    X_list = list()
    for Y in range(0, T_k+1):
        temple_X = list()
        temple_row = list()
        for X in range(0, R_k+1):
                if (0<=X+Y-S_k and X+Y-S_k<=T_k):
                    temple_row.append(C_k_all(X, Y+X-S_k)+F_all_list[k-2][X+Y-S_k])
                    temple_X.append(X)
        F.append(min(temple_row))
        X_list.append(temple_X[int(temple_row.index(min(temple_row)))])
    F_all_list.append(F)
    X_all_list.append(X_list)
    
initial_stock_level = 0
optimal_values_list = list()
current_level = initial_stock_level
previous_value = initial_stock_level
for i in range(0, N):
    X_all_list[N-1-i][current_level]
    optimal_values_list.append(X_all_list[N-1-i][current_level])
    current_level = X_all_list[N-1-i][current_level] - S_k + previous_value
    previous_value = current_level


for i in range (0, N):
    print('X' + str(N-i) + '=' + str(optimal_values_list[i]))

