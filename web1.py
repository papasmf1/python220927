# web1.py 
#크롤링 
from bs4 import BeautifulSoup

#파일을 로딩(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )
#모든 <p> 검색
#print( soup.find_all("p") )
#첫번째 <p> 검색
#print( soup.find("p") )
#<p class="outer-text">
print( soup.find_all("p", class_="outer-text") )

