X = [l.strip() for l in open('in.txt')]
#print(X)
a=0
li = []
for i in X:
    if i != "":
        a+=int(i)
    else:
        li.append(int(a))
        a=0

print(max(li))

#2
lis = sorted(li, reverse=True)
b = 0
for i in range(3):
    b+=lis[i]

print(b)