import requests
from bs4 import BeautifulSoup

URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="_h3_cuogz_1")

movie_titles = [movie.getText() for movie in all_movies]
movies = [movie.replace('\xa0', ' ') for movie in movie_titles]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
