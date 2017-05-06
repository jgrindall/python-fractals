print ("hi")

myList =[1,3,5]

print(myList[1]);

myList.append(7);

print(myList[1]);

myList.remove(3);

print(myList[1]);

myTuple = (2, 4, 6);

print(myTuple[0]);

myList2 = [(0,1), (2,0)]

print(myList2)

for i in (1,2,3):
    print(i)

for i in range(1,6):
    print(i)

def fibo(n):
    a=1;
    b=1;
    for i in range(n):
        x = a + b;
        a = b;
        b = x;
    print(x)

fibo(9);
