#https://toscrape.com/
#https://books.toscrape.com/
#Goal get the title of every book with a 2 star rating 

import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text,'lxml')
# products = soup.select('.product_pod')
#one way to check if something is present in the particular example, will return boolean
# example = products[0]
# print('star-rating Three' in str(example))

#official tactic, check the class 
# example = products[0]
# print([]==example.select('.star-rating.Three'))
#if you get back empty list[], false 
#if you get back something like this 
# [<p class="star-rating Three">
# <i class="icon-star"></i>
# <i class="icon-star"></i>
# <i class="icon-star"></i>
# <i class="icon-star"></i>
# <i class="icon-star"></i>
# </p>]
#means item is checked true for that particular item or product


#we can check if something is 2 stars(string call in, example.select(rating))
#example.select(('a')[1]['title']) to grab the book title 

two_star_titles = []
for n in range(1,51): 
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")
    for book in books: 
        #for every book that is returned 
        #if the list is not empty for star-rating Two, that means i do have a two star rating book 
        if len(book.select('.star-rating.Two')) != 0: 
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)
            
print(two_star_titles)