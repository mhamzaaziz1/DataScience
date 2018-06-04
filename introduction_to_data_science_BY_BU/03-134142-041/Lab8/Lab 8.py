from bs4 import BeautifulSoup
import urllib


url = 'http://www.imdb.com/search/title?release_date=2000-01-01,2017-12-31'


r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, 'html.parser')
type(soup)
movie_containers = soup.findAll('div', class_='lister-item-content')


for movie in movie_containers:
    m = movie.h3.a.text.strip()
    year= movie.h3.find('span', class_='lister-item-year text-muted unbold')
    rating = movie.find('div', class_='inline-block ratings-imdb-rating')
    voting = movie.find('p', class_ ='sort-num_votes-visible')
    metascore = movie.find('span', class_ = 'metascore mixed')
     
    print m
    print year.text.strip()
    print rating.text.strip()
    print voting.text.strip()
    if(metascore == None):
        print ""
    else:
        print "Metascore:", metascore.text.strip()

    print ""
    
    
   


