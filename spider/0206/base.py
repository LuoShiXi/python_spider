from urllib.request import urlopen

#if has Chinese,apply decode()
html = urlopen("https://morvanzhou.github.io/tutorials/data-manipulation/scraping/2-01-beautifulsoup-basic/")
print(html)
