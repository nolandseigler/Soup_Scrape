# PLOTS VISIBLE AT 
# https://localhost/
# On my machine they popped up in a sep window

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

soup = BeautifulSoup(requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html").content, "html.parser")

# print(soup)
ratings = soup.select(".Rating")
ratings.pop(0)
rating_list = [float(rating.get_text()) for rating in ratings]

# print(rating_list)

plt.hist(rating_list)
plt.show()

company_names = soup.select(".Company")
# print(company_names)
company_names.pop(0)
# print(company_names)

company_names_list = [name.get_text() for name in company_names]



cocoa_percent = soup.select(".CocoaPercent")
# print(company_names)
cocoa_percent.pop(0)
# print(company_names)

# Not sure why I couldnt go straight to int
# ValueError: invalid literal for int() with base 10: '73.5'
# cocoa_percent_list = [int(percent.get_text().replace("%", "")) for percent in cocoa_percent]


# hacky way of doing this that i discovered. prob not smart
cocoa_percent_list = [int(float(percent.get_text().strip("%"))) for percent in cocoa_percent]

# CREATE PANDAS DATA FRAME
d = {"Company": company_names_list, "Rating": rating_list, "CocoaPercentage": cocoa_percent_list}
df = pd.DataFrame.from_dict(d)


# Use .groupby to group your DataFrame by Company and #take the average of the grouped ratings.

# Then, use the .nlargest command to get the 10 highest rated chocolate companies. Print them out.

mean_vals = df.groupby("Company").Rating.mean()
ten_best = mean_vals.nlargest(10)
# print(ten_best)

# CLEAR THE PLOT SO SECOND PLOT DOESNT HAVE DATA FROM FIRST
plt.clf()
plt.scatter(df.CocoaPercentage, df.Rating)

# Is there any correlation here? We can use some numpy commands to draw a line of best-fit over the scatterplot.
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")

plt.show()



