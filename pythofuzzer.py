import requests

base_url=input("Enter the url:")
url=f"{base_url}/fuzz"
file=open("wordllists.txt","r")
r=requests.get(url)
with open("wordllists.txt","r") as words:
    wordlists=words.read().splitlines()
session=requests.session()
for  i in wordlists:
    # print(i)
    test_url=url.replace("fuzz",i)
    r=session.head(test_url)
    if r.status_code in (200,300,301):
        print(test_url)
        
    else:
        continue
