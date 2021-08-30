#!/bin/bash

docker run -d -p 8080:8080 -v /Users/jcrasto/airflow_poc/dags/:/usr/local/airflow/dags  puckel/docker-airflow webserver