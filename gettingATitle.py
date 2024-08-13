#example.com 
# python3 -m venv myenv
# source myenv/bin/activate
# pip3 install requests
# pip lists
# https://www.youtube.com/watch?v=40D9jXY8n_Q
import requests
result = requests.get("https://www.example.com")
print(result.text)
import bs4 
soup = bs4.BeautifulSoup(result.text,"lxml")
#print(soup)
print(soup.select('title')[0].getText())
site_paragraph = soup.select('p')[0].getText()
print(site_paragraph)