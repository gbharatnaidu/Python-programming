p,q=input().split(" ")
r=abs(len(p)-len(q))
for i in range(len(p)):
      if(len(p)==1 and q[i] in pc):
         break
      if(p[i]!=q[i]):
           r+=1
print(r)
