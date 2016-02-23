
# coding: utf-8

# In[1]:

f=('роман иванов','елена роганова','игорь петров','иван разумов','родион сидоров')
begin=int(input("input begin"))
spisok=(f[begin])
print(spisok)


# In[1]:

f=('роман иванов','елена роганова','игорь петров','иван разумов','родион сидоров')
begin=int(input("input begin"))
end=int(input("input end"))
spisok=(f[begin:end])
print(spisok)


# In[3]:

f=['роман иванов','елена роганова','игорь петров','иван разумов','родион сидоров']
k=0
for n in f:
    c=n.split()[0]
    p=0
    for i in c:
        if i=='р':
            p=1
    k=k+p
    #print(p)
print(k)
  
 

