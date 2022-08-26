import requests
from bs4 import BeautifulSoup
import xlsxwriter

imdburl = "https://www.imdb.com/chart/top"

r = requests.get(imdburl)

soup = BeautifulSoup(r.content, "html.parser")

gelen_veri = soup.find_all("table", {"class":"chart full-width"})

filmtablosu = gelen_veri[0].contents[len(gelen_veri[0].contents) - 2]

filmtablosu = filmtablosu.find_all("tr")
workbook = xlsxwriter.Workbook('7.harf.deneme.xlsx')
worksheet = workbook.add_worksheet()
row = 0
call = 0
for film in filmtablosu:
    filmbasliklari = film.find_all("td", {"class": "titleColumn"})
    filmismi = str(filmbasliklari[0].a.text)
    filmismi = filmismi.replace("\n", "")
    if  filmismi.startswith("H"):
        worksheet.write(row, call, filmismi)
        row+=1

workbook.close()