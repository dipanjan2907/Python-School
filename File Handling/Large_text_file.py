def linefive1():
    with open("Large_text_file.txt","r") as f:
        data=f.read().split("\n")
        for i in range(4,len(data),5):
            print(data[i])
def linefive2():
    ln=0
    with open("Large_text_file.txt","r") as f:
        while True:
            data=f.readline()
            if not data:
                break
            ln+=1
            if ln%5==0:
                print(data)
linefive2()