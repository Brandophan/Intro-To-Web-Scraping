# Now its time to figure out what we are actually looking for. Inspect the element on the page to see that the section headers have the class "mw-headline". Because this is a class and not a straight tag, we need to adhere to some syntax for CSS. In this case

# Syntax to pass to the .select() method

# Match Results

# soup.select('div')

# All elements with the <div> tag

# soup.select('#some_id')

# The HTML element containing the id attribute of some_id

# soup.select('.notice')

# All the HTML elements with the CSS class named notice

# soup.select('div span')

# Any elements named <span> that are within an element named <div>

# soup.select('div > span')

# Any elements named <span> that are directly within an element named <div>, with no other element in between

import requests
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper#Career')
import bs4
soup = bs4.BeautifulSoup(res.text,"lxml")
#print(soup)   
first_item = soup.select('.vector-toc-text')[0]
for item in soup.select('.vector-toc-text'): 
    print(item.text)