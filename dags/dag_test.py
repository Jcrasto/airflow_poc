from airflow import DAG
from airflow.operators import BashOperator, PythonOperator
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

t1 = BashOperator(
    task_id='task_1',
    bash_command='python /Users/jcrasto/airflow_poc/scripts/data_creator.py',
    dag=dag)