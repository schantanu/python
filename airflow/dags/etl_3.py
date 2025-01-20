import json
import os
from datetime import date, timedelta

import pandas as pd
import requests
from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.utils.helpers import chain
from include.func_example import print_dataframe, print_list

my_list = [1, 2, 3, 4, 5]

# DAG Definition
default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
}

dag = DAG(
    "Example_Import",
    description="Simple example of an import function",
    default_args=default_args,
    schedule_interval="*/60 * * * *",
    dagrun_timeout=timedelta(minutes=20),
    tags=["sandbox"],
    catchup=False,
)

print_list_task = PythonOperator(
    task_id="print_list_task",
    python_callable=print_list,
    op_kwargs={"my_list": my_list},
    provide_context=True,
    dag=dag,
)

print_dataframe_task = PythonOperator(
    task_id="print_dataframe_task",
    python_callable=print_dataframe,
    dag=dag,
)

# Tasks Chaining
tasks = [print_list_task, print_dataframe_task]

chain(*tasks)