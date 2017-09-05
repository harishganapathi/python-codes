import bs4 , webbrowser , requests
webpage = input('enter the webpage\n https://')
webpage = 'https://' + webpage
response = requests.get(webpage)

try:
	response.raise_for_status()
except Exception as exec:
	print('sorry something is wrong %s' %exec)


html_content = bs4.BeautifulSoup(response.text)
#parsing html tags from html documents
#print(html_content)
tag = input('enter the attribute')
name_tag = html_content.select(tag)
for i in name_tag:
	print(i)
#print(name_tag)
print('there are '+ str(len(name_tag))+ ' '+tag +' tags in the link')

#html_content.select(tag)






