#!/usr/bin/env python
# coding: utf-8

# In[11]:


#linear search using while
pos=-1
def search(a,n):
    i=0
    while i<len(a):
        if a[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False
a=[12,33,45,55,23,90,100,5]
n=55
if search(a,n):
    print("number is present,psosition is ",pos+1)
else:
    print("number is not present")


# In[14]:


#linear searchh using for loop
pos=-1
def search(a,n):
    for i in a:
        if i==n:
            globals()['pos']=a.index(i)
            return True
    return False
a=[12,33,45,55,23,90,100,5]
n=1
if search(a,n):
    print("number is present,psosition is ",pos+1)
else:
    print("number is not present")


# In[9]:


#binary search
pos=0
def search(a,n):
    l=0
    u=len(a)-1
    while l<=u:
        mid=(l+u)//2
        if a[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if a[mid] < n:
                l=mid+1
            else:
                u=mid-1
    return False
a=[2,45,67,89,234,34,3,4]
a.sort()
n=3
if search(a,n):
    print("number is present,psosition is ",pos+1)
else:
    print("number is not present")


# In[4]:


#bubble sort
def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
num=[8,2,13,8,34,64,21]
sort(num)
print(num)


# In[10]:


#insertion sort
def sort(lis):
    for i in range(1,len(lis)):
        j=i
        while lis[j-1]>=lis[j] and j>0:
            lis[j-1],lis[j]=lis[j],lis[j-1]
            j-=1
lis=[2,1,34,5,21,5]
sort(lis)
print(lis)


# In[9]:


#select Sort
def sort(num):
    for i in range(len(num)):
        minpos=i
        for j in range(i,len(num)):
            if num[j]<num[minpos]:
                minpos=j
        temp=num[i]
        num[i]=num[minpos]
        num[minpos]=temp
        
num=[4,91,33,12,4,12]
sort(num)
print(num)


# In[4]:


#heap sort
def heap(arr,n,i):
    largest=i
    l=i*2+1
    r=i*2+2
    if (l<n and arr[l]>arr[largest]):
        largest=l
    if (r<n and arr[r]>arr[largest]):
        largest=r
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heap(arr,n,largest)
def heap_sort(arr,n):
    for i in range(n//2-1,-1,-1):
        heap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heap(arr,i,0)
arr=[33,35,42,10,7,8,14,19,48]
n=len(arr)
heap_sort(arr,n)
print(arr)


# In[12]:


#breadth first search
graph = {
  '3':['23','2'],
   '2':['23','3'],
    '23':["B"],
    "B":[]
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '2')    # function calling


# In[14]:


help(bisect)


# In[ ]:





# In[ ]:




