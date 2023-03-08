import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import community
import networkx.algorithms.community as nxcom
from networkx.algorithms.community import k_clique_communities
import random
import string
#shaking için rastgale n tane sayı üretme
rnd_numbers=[]
def rnd(sayi ,ns):
    for j in range(0,sayi):
        r=random.randint(0,ns)
        st=str(r)
        rnd_numbers.append(st)

G=nx.read_edgelist('karate_edge_list.txt')
com1=[]
com=[]
tabu=[]
sonuc=[]
grup=[[],[]]


def modularity(grup):
    modularity=nxcom.modularity(G,grup)
    return modularity
def initialSolution():

 for n in G:
   com1.append(n)   
 i=random.randint(0,nx.number_of_nodes(G))
 a=str(i)
 print(a)
 if a in com1:
    for m in G.neighbors(a):
        com.append(m)
        com1.remove(m)         
 
 grup[0]=com1
 grup[1]=com
 print("initial: ",grup)
 a=modularity(grup)
 print("modin",a)
 tabu.append(a)

def Shake():
 k=1
 k_max=3
 while k<=k_max:
  karate=grup[1].copy()
  n=nx.number_of_nodes(G)
  rnd(k,n)
  print(rnd_numbers)
  for l in rnd_numbers:
    if l in grup[0]:
        for nb in G.neighbors(l):
            if nb in grup[1]:
                grup[0].remove(l)
                karate.append(l)
                break
    if l in grup[1]:
        for b in  G.neighbors(l):  
             if b in grup[0]:
                karate.remove(l)
                grup[0].append(""+l)
                break
             
  grup[1]=karate.copy() 
  print("shake:",grup) 
  print("modshake:", modularity(grup))
  

  rnd_numbers.clear()
  
 

  localSearch()
  for z in tabu:
    for x in sonuc:
      if z>x:
        k=k+1
      else:
        k=1 
       
fark=[]
data=[]
def komsu(grup):
 count=0 #1.grupla bağlantı
 count2=0 # 2 .grupla bağlantı
 
 for k in range(0,2) :
   print(" k",k)
   for a in grup[k]:
     for nb in G.neighbors(a):
         if nb in grup[k]:
        
           count=count+1
         else:
           
            count2=count2+1
     if count2>count:
      count=0 
      count2=0 
      
      l=count2-count
      fark.append(l)
      data.append(a)
     elif count>=count2:
      
        count=0 
        count2=0 
      

def localSearch():
  
   komsu(grup)
   maximum=max(fark)
   index=fark.index(maximum)
  
   value=data[index]
   if value in grup[0]:
     print("0.grup",value)
     grup[0].remove(value)
     grup[1].append(value)
     t=modularity(grup)
     print(t)
     sonuc.append(t)

   else:
      print("1.grup",value)
      grup[0].append(value)
      grup[1].remove(value)
      t=modularity(grup)
      print(t)
      sonuc.append(t)
   print(grup)  
  
initialSolution()       
Shake()
localSearch()
