# Book Scraper 📚

## What's Scraping?
Scraping is a way to automate collecting data from websites 
instead of looking manually and writing it down by hand.

## Why Python?
Python has great built-in tools for this like the `requests` 
library and `BeautifulSoup`. I used what I already knew and built on it.

## How I did it
Using [books.toscrape.com](https://books.toscrape.com) I built a tool 
that scrapes all books and saves them to a text file.

- `requests` — sends a GET request to get the HTML file
- `BeautifulSoup` — parses the HTML and extracts what I need

## What it scrapes
- Book name
- Price
- Star rating
- Availability
- Categories

## Example output
Name: A Light in the Attic
Price: £51.77
Rating: Three
Availability: In stock

## What I learned
- How browsers and HTTP work
- How HTML is structured
- How GET requests work
- Writing and creating files in Python
- Storing data in lists and dictionaries
