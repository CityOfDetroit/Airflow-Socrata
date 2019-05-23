"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
"""
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.airflow_socrata import PostgresToSocrataOperator


default_args = {
    "owner": "xyx0826",
    "start_date": datetime(1970, 1, 1),
    "concurrency": 1,
    "retries": 0
}

dag = DAG('socrata_example', default_args=default_args, schedule_interval=None)

sheet_task = PostgresToSocrataOperator(
    task_id="upsert",
    table_name="people",
    dataset_id="5xa4-w5rv",
    replace=True,
    conn_id=None,
    postgres_conn_id=None,
    postgres_schema=None,
    dag=dag
)