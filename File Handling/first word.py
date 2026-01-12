f=open("Story.txt","r")
for l in f:
    if l.strip():
        print(l.split()[:2])
f.close()

'''['In', 'a']
['we', 'wander']
['The', 'stars']
['casting', 'light']
['Some', 'dreams']
['Others', 'are']
['Each', 'day']
['with', 'hope']
['Believe', 'in']
['trust', 'the']
['Courage', 'sometimes']
['even', 'when']
['Listen', 'closely']
['Love', 'finds']'''