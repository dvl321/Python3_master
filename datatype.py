#text datatype string str
a = "Hello,This is my first string added for variable"
print(a)
print(type(a))
#number datatype integer int

b = 20
print(b)
print(type(b))
#number datatype floating float 

c = 50.12
print(c)
print(type(c))

e = c+b
print(e)
print(type(e))

#number with string  datatype choice

d = 7j
print(d)
print(type(d))

#sequence type: list , tuple and range

#list

f = ["windows","macos","linux"]
print(f)
print(type(f))

#tuple

g = ("windows","macos","linux")
print(g)
print(type(g))

#range

h = range(10)
print(h)
print(type(h))

i = { "name" : "josh","age" : 35 }
print(i)
print(type(i))

#set type : set,frozenset

#set

j = {"windows","macos","linux"}
print(j)
print(type(j))

#frozenset

k = ({"windows","macos","linux"})
print(k)
print(type(k))

#boolean : bool

L = True
print(L)

M = False
print(M)

print(type(M)(L))

#sinary type: bytes,bytearry,memoryview

#byte:

n = b"Hello"
print(n)
print(type(n))

#bytearray

o = bytearray(1)
print(o)
print(type(o))

#memoryview

p = memoryview(bytes(8))
print(p)
print(type(p))

