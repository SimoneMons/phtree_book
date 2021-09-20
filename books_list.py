import glob
import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

os.chdir("C:\Proyectos\phtree\phtree_book\\books")
for file in glob.glob("*.epub"):
    print(file)


book = epub.read_epub(file)

chapters = []
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        chapters.append(item.get_content())

soup = BeautifulSoup(chapters[10], 'html.parser')

text = soup.find_all(text=True)

print(text)