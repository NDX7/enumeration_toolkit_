import requests

url="https://nidhin.vercel.app/fuzz"#test url
file=open("wordllists.txt","r")
r=requests.get(url)
with open("wordllists.txt","r") as words:
    wordlists=words.read().splitlines()
for  i in wordlists:
    # print(i)
    test_url=url.replace("fuzz",i)
    r=requests.get(test_url)
    if r.status_code in (200,300,301):
        print(test_url)
        
    else:
        continue
   
    

