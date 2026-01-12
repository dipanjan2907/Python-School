def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

y=2024
d='Monday'
dt='29 th February'
timegap=int(input("Time Gap in days: "))
m=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
md={'January':31,'February':29,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}

l1=dt.split()
im=l1[2].capitalize()
c=0
if im in md:
    for month in md:
        if im==month:
            c+=int(l1[0])
            break
        else:
            c+=md[month]

p=m.index(d)
g=1
while g<c:
    g+=7
    while (c-g)<7 and (c-g)>0:
        g+=1
        p+=1
        if p==len(m):
            p=0
        if c==g:
            break

mn=m[p]
print(f"{dt} is {mn}")

l1=list(md.items())
i,d,cd,t=0,1,0,0
month=l1[i][0]
'''if is_leap_year(y):
    l1[1] = list(l1[1])
    l1[1][1] = 29
    l1[1] = tuple(l1[1])
else:
    l1[1] = list(l1[1])
    l1[1][1] = 28
    l1[1] = tuple(l1[1])'''

while cd!=timegap:
    d+=1
    cd+=1
    t+=1
    if d==l1[i][1]:
        i+=1
        month=l1[i][0]
        d=0
    elif i==0:
        month=l1[i][0]
print(d,month,y)
