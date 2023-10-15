# look up   interview questions             DOUBT
"""fruitprice = {"apple": 40, "potato": 90, "grapes": 50}
vegprice = {"carrot": 60, "potato": 40, "tomato": 80}

cart = {"apple": 4, "potato": 3, "grapes": 3}

print({key:values*fruitprice[key] for key,values in cart.items()})
"""

#feb 3

col={"name","salary","designation"}
print(dict.fromkeys(col,"assign"))

#comprehension is easy to use , Write in single line (reverse form of normal program)

x=[10,20,30,40,50]
for k in x:
    print(k+5)

print([k+5 for k in x])     #list comprehension
print({k+5 for k in x})     # set comprehension

x=[10,20,30,40,50]
for k in x:
    if k>30:
        k=k+5
        print(k)
    else:
        print(k)

print([k+5 if k>30 else k for k in x])

for k in x:
    if k>30:
        print(k+5)

print([k+5 for k in x if k>30])   # only the element which stastify the if condition will display in output (if act as filter)
print([k+5 if k>30 else k for k in x])    #




X=["dr.ashok","dr.raja","ravi",10,20,40]

for k in X:
    if type(k)=="str" and "dr" in k:
        print(k)

print([k for k in X if type(k)==str and "dr" in k])

x=["pavi","praveen"]
for i in x:
    for j in i:
        print(j)

print([j for i in x for j in i])


x=20
y=30
print("equal" if x==y else x if x<y  else y)

name=["sanjay","miru","murali",16,45]
print ([ k for k in name if type(k)==int])

c=["hi","hello","how"]
print([k.upper() for k in c if "o" in k]) # filtered comprehensions

g=[10,60,"none",47,"none"]

print([k+4 if type(k)==int else "NA" for k in g])

dollar={"mouse":10,"keyboard":40}
print ({k:v*82  for k,v in dollar.items()})

x=["name","age","salary"]
y=["pavi",23,20000]
z=dict((zip(x,y)))   # zip combine the data using the index
print(z)

fruits={"apple":100 , "orange":80 , "grapes":60}
order={"apple":4 , "orange":8 , "grapes":5}
x={key:val*fruits[key] for key,val in order.items()}
print(x)

fruits={"sapotta":100 , "orange":80 , "grapes":60,"papaya":30}
vegg={"tomato":40,"brinjal":55,"carrot":80}

order={"sapotta":4 , "orange":8 , "grapes":5}

x={key:val*fruits[key] for key,val in order.items() if key in fruits}
print(x)


COL=["name","age","salary"]
f=dict.fromkeys(COL,"index")
print(f)


# feb 8

#UDF - User defined function
# collection of functions - modules
# collection of modules - library
# collection of library - packages

# Functions - used for reusability

z=[1,2,3]
g=sum(z)
print(g)

def factorial(x):
    fact=1
    if x<0:
        print("negative")
    elif x==0:
        return 1
    else:
        for i in range(1,x+1):    #(1,5)
            fact=fact*i           #(1
        return fact

print(factorial(4))


