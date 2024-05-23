c={}
c['dollar']=60
c['euro']=80
print(c['dollar'])
print(c.keys())
print()
print(list(c.keys()))
print()
print(list(c.values()))
print()
print(list(c.items()))
c['dollar']=60000
print(c)
c['yen']=10000
print(c)
del c['euro']
print(c)