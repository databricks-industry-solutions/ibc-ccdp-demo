# Databricks notebook source
subscriber_data = "https://raw.githubusercontent.com/databricks-industry-solutions/ibc-ccdp-demo/main/data/subscribers.csv"
svod_data = "https://raw.githubusercontent.com/databricks-industry-solutions/ibc-ccdp-demo/main/data/svod.csv"

# COMMAND ----------

_ = spark.sql("CREATE CATALOG IF NOT EXISTS ibc")

# COMMAND ----------

_ = spark.sql("CREATE DATABASE IF NOT EXISTS ibc.ccdp_demo")

# COMMAND ----------


