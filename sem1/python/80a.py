import re
inf=False
try:
    inf=open('abc.txt','r')
    lines=inf.read().splitlines()
    print("\nLines containing the word ‘explain’ : ")
    for x in lines:
        if(re.search(r'explain',x,re.I)):
            print(x)
    print("\nLines containing dates : ")
    for x in lines:
        if(re.search(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}',x,re.I)):
            print(x)
    print("\nLines containing 8 or above letter words : ")
    for x in lines:
        if(re.search(r'[a-zA-Z]{8,}',x,re.I)):
            print(x)
    print("\nLines containing mobile numbers : ")
    for x in lines:
        if(re.search(r'[6-9][0-9]{8}',x,re.I)):
            print(x)
except Exception as e:
    print(e)
finally:
    if inf:
        inf.close()
