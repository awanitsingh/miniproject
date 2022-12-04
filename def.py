#def input(name,age):
 #   print("My name is",name)
  #  print("My age is",age)

#input("Awanit","18")    



#def a(*args):
 #   for i in args:
  #      print(i)

#a("My","Name","Is","Lakhan")



#def fun(name,salary=10000):
 #   print(name,salary)

#fun("Awanit",9000)  
#fun("Babusaheb",15000)
#fun("Babuaansaheb")


#def info(name,**data):
   # print(name)
  #  for i,j in data.items():
 #       print(i,j)
#
#info("Babusaheb",age=18,place="Kotheyan",num=9999999)        



#def count(listOfNumbers):
 #   even = 0
  #  odd = 0

#    for i in listOfNumbers:
 #       if i%2 == 0:
  #        even +=1
   #     else:
    #      odd +=1
    #return even,odd        
  
listOfNumbers = [32,21,64,100,13]
even,odd = (listOfNumbers)
print(even)
print(odd)



#def func(names):
  #more =  0
  #less = 0
  #for i in names:
    #if len(i)>5:
     # print(i)
    #  more += 1
   # else:
  #    less +=1
 # return more,less           
#names = ["Atul","Shubham","Anurag","Rahul","Dev","Roy"]
#more,less = func(names)
#print(more)
#print(less)




#import sys
#sys.setrecursionlimit(43)
#def hello():
 # print("Hello World")
#hello()  



#def fact(n):
 #   if n == 0:
  #      return 1  
   # return n * fact(n-1)
#num = fact(10)    
#print(num)


#x = 5
#def sq(x):
 # return x**2
#square = sq(x)
#print(square)



#def something(a):
 # return a*a
#x = lambda a : a*a
#num = x(5)
#print(num)



#def name(x):
 #   return lambda a : a + x

#num = name(10)
#print(num(5))



