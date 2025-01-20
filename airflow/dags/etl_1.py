import pandas as pd
import requests
import json
from datetime import date
import os

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

API = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"

default_args = {
    "start_date": days_ago(1),
}


@dag(
    default_args=default_args,
    schedule_interval=None,
    start_date=days_ago(2),
    tags=["sandbox"],
    catchup=False,
)
def Test_ETL():
    @task
    def fetch_data():

        # Get JSON data and convert to dataframe
        response = requests.get(API)
        df = pd.DataFrame(json.loads(response.content))
        df = df.set_index("date_of_interest")

        # Attach the current date to the filename
        df.to_csv("data/nyccovid_{}.csv".format(date.today().strftime("%Y%m%d")))
        filename = "data/nyccovid_{}.csv".format(date.today().strftime("%Y%m%d"))

        print(filename)

        # Read CSV
        data = pd.read_csv(filename)
        print(data.info())

        # Get files in the current directory
        cwd = os.getcwd()
        print(os.listdir(cwd))

        # List files in data directory
        print(os.listdir("data/"))

        # Remove files from data directory
        os.remove(filename)

        # Check if files present in the data directory
        print(os.listdir("data/"))

    @task
    def print_dataframe():

        filename = "data/nyccovid_{}.csv".format(date.today().strftime("%Y%m%d"))

        data = pd.read_csv(filename)
        print(data.info())

        # Remove files from data directory
        os.remove(filename)

        # Check if files present in the data directory
        print(os.listdir("data/"))

    fetch_data()
    # print_dataframe(print_data(fetch_data()))


dag = Test_ETL()