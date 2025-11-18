
#Operations On String

'''s=''
s=""
s=''' '''
s="' '" '''

#Conca
name='Rama'
name1="devi"
n2=name + name1
print(n2) #Ramadevi


name+ ' '+ name1
print(name+ ' '+ name1) #Rama devi

name * 10
print(name * 10) #RamaRamaRamaRamaRamaRamaRamaRamaRamaRama

name='Ramadevi'
print(name[3])#a
print(name[-2])#v

print(name[-5])#a

print(name[1])#a

names='EswararaoRamalaxmiRakeshRamadeviSukanyaa'
print(names)#EswararaoRamalaxmiRakeshRamadeviSukanyaa

print(names[0:4])#Eswa


print(names[4:11])#raraoRa

print(names[11:17])#malaxm

print(names[17:25])#iRakeshR
print(names[25:32])#amadevi

print(names[32:40])#Sukanyaa

print(names[32:]) #Sukanyaa

print(names[0:4:2])  #Ew

print(names[::3])#EarRaxReRavuna

print(names[-8:]) #Sukanyaa


print(names[-15:-8])#amadevi

print(names[-23:-15]) #iRakeshR

print(names[-29:-23]) #malaxm

print(names[-36:-29]) #raraoRa

print(names[-40:-36]) #Eswa

print(names[::-1]) #aaynakuSivedamaRhsekaRimxalamaRoararawsE

print(names) #EswararaoRamalaxmiRakeshRamadeviSukanyaa
print(names[3::-1]) #awsE


print(names[10:4]) #aRoarar

print(names[10:3:-1]) #aRoarar

print(names[16:10:-1]) #mxalam

print(names[24:16:-1]) #RhsekaRi

print(names[31:24:-1]) #ivedama

print(names[39:31:-1]) #aaynakuS

print(names) #EswararaoRamalaxmiRakeshRamadeviSukanyaa


print(names) #EswararaoRamalaxmiRakeshRamadeviSukanyaa

print(names.upper())#ESWARARAORAMALAXMIRAKESHRAMADEVISUKANYAA

print(names.lower()) # eswararaoramalaxmirakeshramadevisukanyaa

print(names.swapcase()) #eSWARARAOrAMALAXMIrAKESHrAMADEVIsUKANYAA


l='python programming language'


print(l.capitalize())#Python programming language

print(l.title()) #Python Programming Language


print("ß".casefold()) #ss


print(l.center(50,'*'))#***********python programming language************

print(l.center(50,'-'))# -----------python programming language------------

print(l.center(50,'_'))# ___________python programming language____________

print(l.ljust(50,'-')) #python programming language-----------------------

print(l.ljust(50,' ')+':') #python programming language                       :
                    
print(l.rjust(50,'-')) # -----------------------python programming language

print('2'.zfill(6))#000002

print('202'.zfill(6))#000202
print('202123'.zfill(6)) #202123
print(names) #

print(names.find('d'))
print(names.find('e'))

print(names.find('Rama'))

print(names.find('z'))

print(names.rfind('a'))

print(names.index('l'))

print(names.index('a'))

print(names.rindex('a'))


print(names)

print(names.count('a'))

print(names.count('e'))

print(names.count('i'))

print(names)

print(names.replace('a','*'))

print(names.replace('la',''))

print(names.replace('la','00'))

print(names.replace('la','-00-'))

print(names.replace('Rama','Sukanya'))

print(names)

print(names.maketrans('aeiou','*****'))

print(names.translate(names.maketrans('aeiou','*****')))

print(names.translate(names.maketrans('AEIOUaeiou','1234500000')))

print(names.translate(str.maketrans('AEIOUaeiou','1234500000')))




