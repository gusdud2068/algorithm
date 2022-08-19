n = list(input())
c = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
d = list(range(3,11)) #2부터 10까지 뺴주고
f = dict(zip(c,d))
print(f)

j=0
for word in n:
    for a,b in f.items():
        if word in a:
            j = j+b
print(j)