import requests
import sys

API_KEY = 'e6bce0c7d07b10fcab9dee27c0ec2868'
BASE_URL = 'http://data.fixer.io/api/latest?access_key=e6bce0c7d07b10fcab9dee27c0ec2868&symbols=USD,AUD,CAD,PLN,MXN'



class Convertor:
    	
	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()

		
		self.rates = data["rates"]

	
 
 
	def convertion(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]

		
  
		amount = round(amount * self.rates[to_currency], 2)
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))




if __name__ == "__main__":

	
	url = str.__add__('http://data.fixer.io/api/latest?access_key=', 'e6bce0c7d07b10fcab9dee27c0ec2868')
	c = Convertor(url)
	from_country = input("From Country: ")
	to_country = input("TO Country: ")
	amount = int(input("Amount: "))

	c.convertion(from_country, to_country, amount)
