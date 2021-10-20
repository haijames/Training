import urllib.request
import bs4 as bs
import requests as rq

url = "https://laodong.vn/photo/9-giong-cho-vo-cung-dang-yeu-nhung-cam-ki-voi-cac-gia-dinh-co-tre-em-816260.ldo"
re = rq.get(url)
soup = bs.BeautifulSoup(re.text, "html.parser")
links = []
imgs = soup.find_all('img')

for img in imgs:
    # links.append(img['src'])
    link = img.get('src')
    # if 'https://' not in link:
    #     link = "https://www.google.com.vn" + link
    links.append(link)

# for l in links:
#     print(l)

for fi in range(len(links)):
    filename = 'img{}.png'.format(fi)
    urllib.request.urlretrieve(links[fi], filename)