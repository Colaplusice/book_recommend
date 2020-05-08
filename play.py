res = requests.get(url='https://book.douban.com/top250', headers={'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'})
articles = soup.find('div', {'class': 'article'})
import re
books = articles.find_all('table')
for book in books:
    book_image = book.find('img')
    title = book.find('div', {'class': 'pl2'}).text.strip()
    # [清] 曹雪芹 著 / 人民文学出版社 / 1996-12 / 59.70元
    book_info = book.find('p', {'class': 'pl'})
    douban_rate = book.find('span', {'class': 'rating_nums'}).text
    re.match('')
    douban_rate_nums=book.find()