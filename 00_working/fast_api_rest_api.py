# To run this app, type the following in terminal
# fastapi run fast_api_rest_api.py

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello_world():
    mydict = {"A": [10, 20, 30],
              "B": [40, 50, 60]}
    return mydict