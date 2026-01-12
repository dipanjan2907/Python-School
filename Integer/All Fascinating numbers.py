l = int(input("Enter limit {beyond 100}: "))
n2 = 0

if l > 99:
    for a in range(100, l+1):
        s = ""
        n = 0
        l1 = []
        for i in range(1, 4):
            s = s + str(a*i)
        s1 = int(s)
        while s1 > 0:
            r = s1 % 10
            l1.append(r)
            s1 = s1 // 10
        if 0 in l1:
            c = l1.count(0)
            while c > 0:
                l1.remove(0)
                c = l1.count(0)
        l1.sort()
        for i in l1:
            n2 = (n2 + i) * 10
        n2 //= 10
        if 123456789 == n2:
            print(a)
else:
    print("You need to enter a 3-digit number")
