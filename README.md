This project will help you to setup Airflow with Spark

### Create conda env for airflow
``` shell
conda create -n airflow python=3.6
conda activate airflow
```

#### Install everything
``` shell
export AIRFLOW_VERSION=2.0.1
export PYTHON_VERSION=3.6
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# Put this is .bashrc
export PYSPARK_PYTHON=/home/ubuntu/anaconda3/envs/airflow/bin/python
```

### Install libs
``` shell
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
pip install apache-airflow-providers-apache-spark==1.0.1 --constraint "${CONSTRAINT_URL}" 
pip install kubernetes==11.0.0 --constraint "${CONSTRAINT_URL}" 
pip install pyspark==3.0.1 --constraint "${CONSTRAINT_URL}" 
```

### One time job
``` shell
airflow db init
airflow users create --username admin --firstname Harish --lastname Bohara --role Admin --email harish.bohara@gmail.com
 >> Enter password Here
```

1. You may want to change "web_server_port" to the port you need
2. You may want to change "auth_backend" to "auth_backend=airflow.api.auth.backend.basic_auth"

# Run in background
``` shell
airflow webserver -D
airflow scheduler -D 
```
