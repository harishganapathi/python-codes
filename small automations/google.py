import sys,requests , bs4 , webbrowser

print('googling')

res = requests.get('http://www.google.com/search?q='+' '.join(sys.argv[1:]))

res.raise_for_status()

#print(res.text)
search_page = bs4.BeautifulSoup(res.text)
print(search_page)
#links = search_page.select('.r a')



#opentabs = min(5,len(links))
#for i in range(opentabs):
#	webbrowser.open('http://google.com' + links[i].get('href'))
