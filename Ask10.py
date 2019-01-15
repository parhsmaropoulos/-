import urllib.request


url = input("enter the url:")

def htmlcounter(url):
 counter = 0
 file = urllib.request.urlopen(url)
 page = file.read().decode("utf-8")
 for i in page.splitlines():
     if '<a' in i:
         counter += 1
     if '<br>' in i:
         counter += 1
     if '<p>' in i:
         counter += 1
     if '<p ' in i:
         counter += 1
 print(counter)

htmlcounter(url)







