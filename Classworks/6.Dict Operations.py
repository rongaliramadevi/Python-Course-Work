'''
dictionary
----------
'''

d={}
d=dict()
d={'name':'sumanth','course':'pfs','batch':41}
print(d)

d={1:'val',12.3:'val','string':'val',(1,2,3):'val',False:'val'}
print(d)
d['name']='sumanth'
print(d)
print(d.get('course'))
print(d.get('batchno'))
print(d.get('name'))
print(d.get('age'))
d['age']=22
print(d)
d['passedout']=2025
print(d)
d.pop('age')
print(d)
d.keys()
print(d)
d.values()
print(d)
len(d)

