import requests ,sys

url="https://nidhin.vercel.app/fuzz"
file=open("wordllists.txt","r")
r=requests.get(url)
with open("wordllists.txt","r") as words:
    wordlists=words.read().splitlines()
for  i in wordlists:
    test_url=url.replace("fuzz",i)
    r=requests.get(test_url)
    if r.status_code==200:
        print("valid")
        print(i)
    else:
        print("not valid")
