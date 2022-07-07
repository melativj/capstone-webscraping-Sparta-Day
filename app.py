from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/history/IDR/USD/T')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('div', attrs={'class':'table-responsive'})
row = table.find_all('tr')

row_length = len(row)

temp = [] #initiating a list 

for i in range(0, row_length):
#insert the scrapping process here
  	#get date 
    period_date = table.find_all('tr')[i].find_all('td')[0].text
    
    #get price daily
    price_daily = table.find_all('tr')[i].find_all('td')[2].text
    price_daily = price_daily.replace('IDR','').strip() #to remove word "IDR" & excess white space
    
    temp.append((period_date,price_daily)) 

#reserve the data 
temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp, columns = ('period_date','price_daily'))

#insert data wrangling here

# change the price daily to float64 type
df['price_daily'] = df['price_daily'].str.replace(",","")
df['price_daily'] = df['price_daily'].astype('float64')

# change the period date to datetime64
df['period_date'] = pd.to_datetime(df['period_date'])
df['month_name'] = df['period_date'].dt.month_name()

# create column the month year
df['month_year'] = df['period_date'].dt.to_period('M')

#challenge
df2 = df.groupby(['month_year']).mean()
df2 = df2.rename(columns={'price_daily': 'mean_price'})

df = df.set_index('period_date') 
#end of data wranggling 




@app.route("/")
def index(): 
	
	card_data = f'{round(df["price_daily"].mean(),2)}' #be careful with the " and ' 

	# generate plot
	ax = df.plot(figsize = (20,9)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# generate plot challenge
	ax = df2.plot(figsize = (20,9)) 
	
	# Rendering plot
	# Do not change this
	figfile2 = BytesIO()
	plt.savefig(figfile2, format='png', transparent=True)
	figfile2.seek(0)
	figdata_png2 = base64.b64encode(figfile2.getvalue())
	plot_result2 = str(figdata_png2)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result,
		plot_result2=plot_result2
		)


if __name__ == "__main__": 
    app.run(debug=True)