import webbrowser
webbrowser.open('https://www.youtube.com')

import requests
res= requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
res.raise_for_status()
print(len(res.text))
print(res.text[:200])
print()

badres=requests.get('https://automatetheboringstuff.com/files/rjgrgrgbeverg')
badres.raise_for_status()
print()


playFile= open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()


import bs4
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
res = requests.get("https://www.amazon.in/Introduction-Algorithms-Eastern-Economy-Thomas/dp/8120340078", headers=headers)
res.raise_for_status()

soup= bs4.BeautifulSoup(res.text, "html.parser")
elems= soup.select('span.a-price span.a-price-whole')
#print(elems)
print(elems[0].text)
