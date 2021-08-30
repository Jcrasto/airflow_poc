from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'josh',
    'depends_on_past': False,
    'start_date': datetime(2021, 8, 29),
    'email': ['crasto.dataprojects@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('dag_test', default_args=default_args)