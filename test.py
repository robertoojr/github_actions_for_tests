# Databricks notebook source
from functions import *

# COMMAND ----------

def test_sum():
    result = sum_numbers(3, 2)
    assert result == 5

# COMMAND ----------

def test_subtract():
    result = subtract_numbers(3, 2)
    assert result == 1
