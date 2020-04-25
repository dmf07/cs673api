import requests
import json
import operator
import csv
import pandas as pd
import flask
from flask import request

class recommendation:
	def __init__(self,upc):
		self.upc=str(upc)
		self.brand_json={}
		self.category_json={}
		self.brand=""
		self.category=""
		self.sort_result=""
		self.dict_save_result={}



	def test_brand(self):
		if type(self.brand_json)!=str:
			return None
		try:
			json.loads(self.brand_json)
		except ValueError:
			return False
		return True

	def test_category(self):
		if type(self.category_json)!=str:
			return None

		try:
			json.loads(self.category_json)
		except ValueError:
			return False
		return True

	def capture_brand(self):
		url="https://api.barcodespider.com/v1/lookup?token=eba3ac19cc270a0e8b42&upc="+self.upc
		response=requests.get(url)
		response_text=json.loads(response.text)
		value_attributes=response_text.get('item_attributes')

		self.brand=value_attributes.get('brand')
		return self.brand

	def capture_category(self):
		url="https://api.barcodespider.com/v1/lookup?token=eba3ac19cc270a0e8b42&upc="+self.upc
		response=requests.get(url)
		response_text=json.loads(response.text)
		value_attributes=response_text.get('item_attributes')
		self.category=value_attributes.get('category')
		return self.category

	def __checkresponse(self,checkobject):
		
		response=checkobject.get('item_response')
		code=response.get('code')
		if code=='200':
			print('MMM')
			return True
		else:
			print(code)
			return False

	def recommendation_brand(self):
		
		url_brand='https://api.barcodespider.com/v1/search?token=eba3ac19cc270a0e8b42&s='+str(self.brand)
		response_brand=requests.get(url_brand)
		self.brand_json=json.loads(response_brand.text)
		
		"""self.brand_json=str(self.brand_json)"""
		return self.brand_json

	
	def recommendation_category(self):
		url_catageory='https://api.barcodespider.com/v1/search?token=eba3ac19cc270a0e8b42&s='+str(self.category)
		response_catageory=requests.get(url_catageory)
		self.category_json=json.loads(response_catageory.text)
		
		"""self.category_json=str(self.category_json)"""
		return self.category_json

	def getbrand(self):
		return self.brand_json

	
	def getcategory(self):
		return self.category_json

	
	def choose_category(self):
		self.capture_category()
		self.recommendation_category()
		
		self.data_process(self.getcategory())
		self.to_csv(self.getcategory())

		return self.getsaveddata()


	

	def choose_brand(self):
		self.capture_brand()
		self.recommendation_brand()
		
		self.data_process(self.getbrand())
		
		self.to_csv(self.getbrand())

		return self.getsaveddata()


	def to_csv(self,data):
		df=pd.DataFrame(data["Data"])
		df.to_csv('output.csv') 


	def data_process(self,data):
		self.dict_save_result={}
		m=data.get('Data')
		for i in m:
			S_1=i.get('item_attributes')
			s_2=S_1.get('title')
			s_3=S_1.get('upc')
			self.dict_save_result.update({s_2:s_3})

	
	def getsaveddata(self):
		
		return self.dict_save_result


server=flask.Flask(__name__)

@server.route('/system_result',methods=['get','post'])
def system_result():
	upc=request.values.get('upc')
	if upc:
		k=recommendation(upc)
		resu=k.choose_brand()
		return json.dumps(resu,ensure_ascii=False)


	else:
		resu={'code':10001,'message':'UPC code can not be empty!'}
		return json.dumps(resu,ensure_ascii=False)
if __name__=='__main__':
	server.run(debug=True,port=8888,host='0.0.0.0')

	
	
		




	










	





    





	
	

  
	



 


