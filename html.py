import requests
from bs4 import BeautifulSoup
print(BeautifulSoup(requests.get("https://gist.github.com/dwzIo").text,"html.parser").prettify())