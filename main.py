#You gotta learn basics first
from bs4 import BeautifulSoup
with open('index_copy.html','r') as file:
    content=file.read()
    soup=BeautifulSoup(content,'lxml')
    #print(soup.prettify())
    #tags=soup.find('h1')
    #tags=soup.find_all('b')
    #for tag in tags:
    #    print(tag.text)
    #print(tags)
    skills=soup.find('div',class_ ='tab-contents active-tab')
    if skills:
        list_items = skills.find_all('li')
        for item in list_items:
            h6_tag = item.find('h6')
            if h6_tag:
                last_word = h6_tag.text.split(',')[-1].strip()
                print(last_word)

    titles=soup.find_all('div',class_='tab-titles')
    for title in titles:
        titlee=title.p.text
