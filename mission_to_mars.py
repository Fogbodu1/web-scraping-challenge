
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():

  mars_data = {}
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#NASA MARS NEWS
#url = 'http://quotes.toscrape.com/'
url = 'https://redplanetscience.com/'
browser.visit(url)


# Scrape page into soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# save the most recent article, title and date
article = soup.find("div", class_="list_text")
news_date = article.find("div", class_="list_date").text
news_title = article.find("div", class_="content_title").text
news_p = article.find("div", class_="article_teaser_body").text


    mars_data['news_date'] = news_title
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p


#URL of JPL images scraped
url = 'https://spaceimages-mars.com/'
browser.visit(url)


#URL of JPL images scraped
full_image_elem=browser.find_by_tag('button')[1]
full_image_elem.click()


#Create a BeautifulSoup object
html=browser.html
ing_soup = BeautifulSoup(html, 'html.parser')


ing_url_rel = ing_soup.find('img', class_='fancybox-image').get('src')
ing_url_rel


featured_image_url=f'https://spaceimages-mars.com/{ing_url_rel}'
featured_image_url


url = 'https://galaxyfacts-mars.com/'
#Scrape table data from Mars webpage
tables = pd.read_html(url)
tables


#Index the first dataframe object
df = tables[0]

#Set column names
df.columns = ['Description','Mars','Earth']

#Set Description column as the index
df.set_index('Description', inplace=True)
df

#Convert table into HTML table
html_table = df.to_html()
html_table

#Remove unwanted new lines
html_table.replace('\n', '')

hemispheres_url = 'https://marshemispheres.com/'
browser.visit(hemispheres_url)

        # HTML Object
html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_hemispheres, 'html.parser')

        # Retreive all items that contain mars hemispheres information
hemispheres = soup.find_all('div', class_='item')
hemispheres

# Create empty list for mars info
     mars_info = {}
     # Create empty list for hemisphere urls 
     hemisphere_image_urls= []
     # Store the main_ul 
     hemispheres_main_url = 'https://marshemispheres.com/' 

     # Loop through the items previously stored
     for hemisphere in hemispheres:
         # Store title
         title = hemisphere.find('h3').text
         
         # Store link that leads to full image website
         partial_img_url = hemisphere.find('a', class_='itemLink product-item')['href']
         
         # Visit the link that contains the full image website 
         browser.visit(hemispheres_main_url + partial_img_url)
         
         # HTML Object of individual hemisphere information website 
         partial_img_html = browser.html
         
         # Parse HTML with Beautiful Soup for every individual hemisphere information website 
         soup = BeautifulSoup( partial_img_html, 'html.parser')
         
         # Retrieve full image source 
         img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
     
         # Append the retreived information into a list of dictionaries 
         hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

     #mars_info['hiu'] = hemisphere_image_urls
     mars_info = hemisphere_image_urls
     mars_info

