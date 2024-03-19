import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL) 
webArchive_html = response.text

soup = BeautifulSoup(webArchive_html, "html.parser")

webArchive_title = [title.getText() for title in soup.find_all(name="h3", class_="title")]

with open(file="./100_topMovies", mode='w') as file: 
    for index in range(99,0,-1):
        file.write(f"{webArchive_title[index]}\n")

        










