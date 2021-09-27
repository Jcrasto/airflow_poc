# airflow_poc
docker run -d -p 8080:8080 puckel/docker-airflow webserver
docker run -d -p 8080:8080 -v /Users/jcrasto/airflow_poc/dags:/usr/local/airflow/dags  puckel/docker-airflow webserver

http://localhost:8080/admin/