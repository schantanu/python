import os
import sys
from datetime import timedelta

import pandas as pd
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import get_current_context
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.utils.helpers import chain

from include.func_pandas import cleanup_columns
from include.func_source import get_source_data
from include.func_sql import (
    create_table,
    execute_stored_procedure,
    insert_data_to_database,
    update_bi_tables,
)

# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Report Parameters
reports = {"report_id": [100, 101, 102]}
reports_df = pd.DataFrame(reports)

# DAG definition
default_args = {"owner": "airflow", "start_date": days_ago(1)}

dag = DAG(
    "Projects_All",
    description="Extract for Projects All Reports " + str(reports["report_id"]),
    default_args=default_args,
    schedule_interval="0 6 * * *",
    dagrun_timeout=timedelta(minutes=30),
    tags=["vine", "prod"],
    catchup=False,
)

# Tasks
get_vine_data_task = PythonOperator(
    task_id="get_vine_data",
    python_callable=get_source_data,
    op_kwargs={"reports": reports["report_id"]},
    provide_context=True,
    dag=dag,
)

for index, row in reports_df.iterrows():

    cleanup_columns_task = PythonOperator(
        task_id="cleanup_columns_for_" + str(row["report_id"]),
        python_callable=cleanup_columns,
        op_kwargs={"report": row["report_id"]},
        provide_context=True,
        dag=dag,
    )

    create_table_task = PythonOperator(
        task_id="create_table_for_" + str(row["report_id"]),
        python_callable=create_table,
        op_kwargs={"report": row["report_id"]},
        provide_context=True,
        dag=dag,
    )

    insert_data_to_database_task = PythonOperator(
        task_id="insert_data_to_database_for_" + str(row["report_id"]),
        python_callable=insert_data_to_database,
        op_kwargs={"report": row["report_id"]},
        provide_context=True,
        dag=dag,
    )

    update_bi_tables_task = PythonOperator(
        task_id="update_BI_TABLES_for_" + str(row["report_id"]),
        python_callable=update_bi_tables,
        op_kwargs={"table_name": "RAW_SOURCE_" + str(row["report_id"])},
        provide_context=True,
        dag=dag,
    )

    # Tasks Chaining
    tasks = [
        get_vine_data_task,
        cleanup_columns_task,
        create_table_task,
        insert_data_to_database_task,
        update_bi_tables_task,
    ]
    chain(*tasks)