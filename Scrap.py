import requests 
from bs4 import BeautifulSoup

pageResponse = requests.get("https://books.toscrape.com/")
pageResponse.encoding = "utf-8" 
pageSoupe = BeautifulSoup(pageResponse.text, "html.parser")


bookpage = pageSoupe.find_all("article", class_="product_pod")




def getPriceNames(books):
    booklist = []
    
    
    for book in books:
        
        bookDetails = {
            "name": book.find("h3").find("a")["title"],
            "price":book.find("p", class_="price_color").text
        }
        booklist.append(bookDetails)
    with open("resault.txt", "w") as file:
        for item in booklist:
            file.write(f"Name: {item["name"]}\n Price:{item["price"]}\n")   
        
    
getPriceNames(bookpage)



