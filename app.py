#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, request, render_template


# In[4]:


app = Flask(__name__)


# In[5]:


import joblib


# In[6]:


@app.route("/", methods=["GET", "POST"])
def index1():
    if request.method == "POST":
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        print(purchases, suppcard)
        model1 = joblib.load("CART")
        purchases = float(purchases)
        suppcard = float(suppcard)
        pred1 = model1.predict([[purchases,suppcard]])
        model2= joblib.load("RF")
        pred2 = model2.predict([[purchases,suppcard]])
        model3= joblib.load("GB")
        pred3 = model3.predict([[purchases,suppcard]])
        return(render_template("index.html", result1=pred1, result2=pred2, result3=pred3))
    else:
        return(render_template("index.html", result1="2", result2="2", result3='2'))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




