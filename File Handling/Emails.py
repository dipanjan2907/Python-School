with open("Emails.txt","r") as f:
    try:
        fl=0
        while True:
            data=f.readline()
            if not data:
                break
            l1=data.split()
            for i in l1:
                if '@' in i:
                    print(i)
                    fl=1
    except:
        print()
    finally:
        if fl==0:
            print("No words with '@cmail")
