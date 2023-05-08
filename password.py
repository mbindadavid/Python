import itertools
res = itertools.permutations('abc',3) # 3 is the length of your result.
for i in res: 
   print ('').join(i)


   