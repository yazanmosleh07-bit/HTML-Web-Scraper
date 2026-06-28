#importing both requests and BeautifulSoup
import requests 
from bs4 import BeautifulSoup

# getting the html page from the url using a get request
pageResponse = requests.get("https://books.toscrape.com/")

# setting the encoding of the page to utf-8 so icons like the pound sign won't show as random numbers
pageResponse.encoding = "utf-8"

# using the built-in parser in BeautifulSoup to turn all the blob of text into an acutal text
pageSoupe = BeautifulSoup(pageResponse.text, "html.parser")

# looking for the tag and class that holds names and prices
# used the find_all method because it turns all these articles into a list 
bookpage = pageSoupe.find_all("article", class_="product_pod")

# look for the div that holds the catagory
pageCatagory = pageSoupe.find("div", class_="page-header action").find("h1")
# loo for the "ul" that holds the categories and find the "a" tag
allCatagories = pageSoupe.find("ul", class_="nav-list").find_all("a")

# scrape all the categories
def getCatagories(catagory):
    # store them in a list
    catagoryList = []
    
    catagoryCount = 0
    # loop thru all the given lis and store them
    for cat in catagory:
        catagoryCount +=1
        catagoryList.append(cat.text.strip())
    
    return catagoryCount, catagoryList

# this fucntion makes a list that holds dictionaries of names and prices
# it takes the soup page as a peramter
def getPriceNames(books,catagory):
    #holds all the dectionaries
    booklist = []
    amountOfBooks = 0
    amountofcats,listofcats = getCatagories(allCatagories)
    
    # looping thru the whole page
    for book in books:
        # find the rating store it in a list
        rating_tag = book.find("p", class_="star-rating")
        # storing a name and a price using find
        bookDetails = {
            "name": book.find("h3").find("a")["title"],
            "price":book.find("p", class_="price_color").text,
            # accses the rating and set the rating to the second index
            "rating":rating_tag["class"][1],
            #adds the availability and removes all the whilespace from it useing strip
            "availability":book.find("p", "instock availability").text.strip()
        }
        # adding that dictionary to the list
        booklist.append(bookDetails)
        # add 1 to the amount of books
        amountOfBooks += 1
    # creating a file called "result.txt"
    with open("result.txt", "w") as file:
        file.write(f"===============INFO============\nSite Name:books.toscrape.com\n Amount Of Categories:{amountofcats}\n Categories: {listofcats}\n")
        file.write("================================\n")
        file.write(f"SUMMERY:\nCurrent Category:{catagory.text}\nAmount Of Books:{amountOfBooks}\n")
        file.write("================================\n")
        #looping thru every itme in the book list and adding a line with a price and a name
        for item in booklist:
            file.write(f"Name: {item["name"]}\n Price:{item["price"]}\n Rating:{item["rating"]}\n Availability:{item["availability"]}\n")
        
# calling the function and passing bookpage(that holds the list of the page) 
getPriceNames(bookpage,pageCatagory)



