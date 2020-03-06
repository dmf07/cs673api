#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup


# In[18]:


Keywords = input('input Barcode: ')


# In[19]:


api = finding(appid='WenjieCh-FindChea-', config_file=None)


# In[20]:


api_request = {'keywords': Keywords, 'outputSelector': 'SellerInfo'}


# In[21]:


response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content, 'lxml')


# In[22]:


items = soup.find_all('item')


# In[23]:


for item in items:
    cat = item.categoryname.string.lower()
    print('category: ' + cat)
    title = item.title.string.lower().strip()
    print('Title: ' + title)
    price = item.currentprice.string
    print('Price: ' + price)
    url = item.viewitemurl.string.lower()
    print("url: " + url)
    #seller = item.sellerusername.text.lower()
    listingtype = item.listingtype.string.lower()
    print('Listing type: ' + listingtype)
    condition = item.conditiondisplayname.string.lower()
    print('Condition: ' + condition)


# In[24]:


# In[25]:


# In[ ]:
