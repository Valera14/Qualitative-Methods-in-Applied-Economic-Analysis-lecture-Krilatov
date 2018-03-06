
# coding: utf-8

# In[113]:


import numpy as np

def c1(Z):
    if Z>0:
        return 3*Z
    elif Z <= 0:
        return 0
def c2(S):
    if S>0:
        return 4+2*S
    elif S <= 0:
        return 0

N = 7
demands_in_workers = np.zeros(N)

demands_in_workers[0] = 5
demands_in_workers[1] = 7
demands_in_workers[2] = 8
demands_in_workers[3] = 4
demands_in_workers[4] = 6
demands_in_workers[5] = 4
demands_in_workers[6] = 6

F = list()
Y_numbers = list()

counter = 0
previous_value = 500000

Y0_current = list()
Y0_all = list()
for Y0 in range(int(demands_in_workers[N - 2]), 5000):
    F.append(c2(demands_in_workers[N-1] - Y0) + c1(0))
    Y_numbers.append(demands_in_workers[N-1])
    if(previous_value == F[counter]):
        break
    counter = counter + 1
    previous_value = F[counter-1]
    Y0_current.append(Y0)

if len(F)<10:
     for j in range (int(len(F) - 1), 10):
            F.append(F[len(F) - 1])
Y0_all.append(Y0_current)

F_all = list()
F_all.append(F)
Y_all = list()
Y_all.append(Y_numbers)

counter = 0
previous_value = 500000
N_counter = N
for i in range(2, N):
    F = list()
    Y_numbers = list()
    Y0_current = list()
    for Y0 in range(int(demands_in_workers[N_counter - 3]), 100):
        F_temple = list()
        counter_F = 0
        for Y in range(int(demands_in_workers[int(N_counter - 2)]), int(demands_in_workers[int(N_counter - 2)] + 10)):
            F_temple.append(c2(Y - Y0) + c1(Y - demands_in_workers[N_counter - 2]) + F_all[i-2][counter_F])
            counter_F = counter_F + 1
        F.append(min(F_temple))
        
        temple_Y = np.arange(int(demands_in_workers[int(N_counter - 2)]), int(demands_in_workers[int(N_counter - 2)] + 4))
        Y_numbers.append(temple_Y[int(F_temple.index(min(F_temple)))])
        Y0_current.append(Y0)
        if(previous_value == F[counter]):
            break
        counter = counter + 1
        previous_value = F[counter-1]
    if len(F)<10:
        for j in range (int(len(F) - 1), 10):
                F.append(F[len(F) - 1])
    F_all.append(F)
    Y_all.append(Y_numbers)
    Y0_all.append(Y0_current)
    counter = 0
    #if len(F_all[i-1])<4:
        #for y in range(len(F_all[i-1])-1, 4):
            #F_all[i-1].append(F_all[i-2][len(F_all[i-2])-1])
    N_counter = N_counter - 1
    
i = N
F = list()
Y_numbers = list()
Y0_current = list()
for Y0 in range(0, 100):
    F_temple = list()
    counter_F = 0
    for Y in range(int(demands_in_workers[int(N_counter - 2)]), int(demands_in_workers[int(N_counter - 2)] + 10)):
        F_temple.append(c2(Y - Y0) + c1(Y - demands_in_workers[N_counter - 2]) + F_all[i-2][counter_F])
        #print(F_temple)
        counter_F = counter_F + 1
    F.append(min(F_temple))
    temple_Y = np.arange(int(demands_in_workers[int(N_counter - 2)]), int(demands_in_workers[int(N_counter - 2)] + 5))
    Y_numbers.append(temple_Y[int(F_temple.index(min(F_temple)))])
    #Y.append(F_temple.index(max(F_temple)))
    #if(previous_value == F[counter]):
        #break
    Y0_current.append(Y0)
    counter = counter + 1
    previous_value = F[counter-1]
if len(F)<10:
    for j in range (int(len(F) - 1), 10):
            F.append(F[len(F) - 1])
F_all.append(F)
Y_all.append(Y_numbers)
counter = 0
    #if len(F_all[i-1])<4:
        #for y in range(len(F_all[i-1])-1, 4):
            #F_all[i-1].append(F_all[i-2][len(F_all[i-2])-1])
N_counter = N_counter - 1
Y0_all.append(Y0_current)

final_list_all = list()
#final_list = list()
previous_value = 50000000
for i in range(Y0_all[N-2][0], Y0_all[-1][-1]+1):
    dimension = N
    new_value = Y_all[-1][i]
    if (Y_all[-1][i] == previous_value):
        t = 5
    else:
        final_list = list()
        final_list.append(Y_all[-1][i])
        for u in range(1, dimension):
            new_index = Y0_all[dimension-2].index(new_value)
            new_value = Y_all[dimension-2][new_index]
            final_list.append(new_value)
            dimension = dimension - 1
        final_list_all.append(final_list)
    previous_value = Y_all[-1][i]
    
    
for t in range(0, len(final_list_all)):
    for i in range(0, N):
        print('На  ' + str(i+1) + '-ой неделе численность должна быть: ' + str(final_list_all[t][i]))
    if (t!=len(final_list_all)-1):
        print('\n Другой вариант:')


# In[38]:


t = 5


# In[39]:


print(t)

