with open("Find&Replace.txt","r+") as f:
    data=f.readlines()
    f.seek(0)
    f.truncate()
    for i in data:
        i=i.replace("Python","Java")
        f.write(i)