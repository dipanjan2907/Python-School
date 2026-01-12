with open("longer_than_5.txt","r") as f:
    try:
        fl=0
        print("WORD LONGER THAN 5 CHARACTERS:\n")
        while True:
            data=f.readline()
            if not data:
                break
            data=f.readline()
            l1=data.split()
            for i in l1:
                if len(i)>5:
                    print(i)
                    fl=1
    except:
        print()
    finally:
        if fl==0:
            print("No Such Word!")