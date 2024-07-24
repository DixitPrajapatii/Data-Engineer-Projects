from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
# from datetime import datetime
import os
import sys

# Add the path to the twitter_dag folder to the system path
dag_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dag_folder)

from Twitter_DAG.Twitter_ETL import Tweets_ETL

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=Tweets_ETL,
    dag=dag,
)

run_etl