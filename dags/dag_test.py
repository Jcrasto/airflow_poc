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
    bash_command='/Users/jcrasto/airflow_poc/venv/bin/python /Users/jcrasto/airflow_poc/scripts/data_creator.py',
    dag=dag)


t2 = BashOperator(
    task_id='task_2',
    bash_command='/Users/jcrasto/airflow_poc/venv/bin/python /Users/jcrasto/airflow_poc/scripts/s3_uploader.py',
    dag=dag)

t3 = BashOperator(
    task_id='task_3',
    bash_command='/Users/jcrasto/airflow_poc/venv/bin/python /Users/jcrasto/airflow_poc/scripts/file_folder_cleanup.py',
    dag=dag)


t1 >> t2 >> t3
