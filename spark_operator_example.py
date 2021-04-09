from datetime import timedelta
from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.apache.spark.operators.spark_jdbc import SparkJDBCOperator
from airflow.providers.apache.spark.operators.spark_sql import SparkSqlOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='example_spark_operator',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['spark'],
    params={"param": "value"},
)

run_this_last = DummyOperator(
    task_id='run_this_last',
    dag=dag,
)

# TODO - Here we are running a pi.py script. Change path to youre location.
flight_search_ingestion= SparkSubmitOperator(
	task_id='flight_search_ingestion',
	conn_id='spark_default',
	application='/home/ubuntu/anaconda3/envs/airflow/lib/python3.6/site-packages/pyspark/examples/src/main/python/pi.py',
	total_executor_cores=4,
	executor_cores=2,
	executor_memory='1g',
	driver_memory='1g',
	name='flight_search_ingestion',
	execution_timeout=timedelta(seconds=100000),
	dag=dag
)


run_this_last >> flight_search_ingestion

if __name__ == "__main__":
    dag.cli()
