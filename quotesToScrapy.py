#https://quotes.toscrape.com/
import requests 
import bs4 

res = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,'lxml')

#a set is unique items 
#use a set instead of list so no duplicates

# print(soup.select('.author')[1].getText())

authors = set()
for name in soup.select('.author'): 
    authors.add(name.text)
    
print(authors)


#create a list of all the quotes on the first page 
quotes_on_page = []
for quotes in soup.select('.text'): 
    quotes_on_page.append(quotes.text)
print(quotes_on_page)
#TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.
for tag in soup.select('.tag-item'): 
    print(tag.text)

#TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!
base_url  = 'https://quotes.toscrape.com/page/'
#print(base_url+str(10))
new_authors = set()
for page in range(0,10): 
    page_url_loop = base_url+str(page)
    new_res = requests.get(page_url_loop)
    new_soup = bs4.BeautifulSoup(new_res.text,'lxml')
    for name in new_soup.select('.author'): 
        authors.add(name.text)

print(len(new_authors))


#or use while loop
#page_url = url+str(99999)
# res = requests.get(page_url)
# soup = bs4.BeautifulSoup(res.text,'lxml')
# "No quotes found!" in res.text
#Should show true 



page_still_valid = True 
diffauthors = set()
page = 1
while page_still_valid: 
    page_url = base_url+str(page)
    diffres = requests.get(page_url)
    
    if "No quotes found!" in diffres.text:
        break
    diffsoup = bs4.BeautifulSoup(diffres.text,'lxml')
    
    for name in diffsoup.select('.author'): 
        diffauthors.add(name.text)
    page +=1
    
print('\n')
print(len(diffauthors))
    