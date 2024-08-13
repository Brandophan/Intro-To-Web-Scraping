import requests
import bs4
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,'lxml')
computer = soup.select('.mw-file-element')[1]
#rememeber on google type the https and copy the src = "" part

# print(computer['src'])
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

#binary content
#image_link.content
f = open('my_computer_image.jpg','wb')
f.write(image_link.content)
f.close()