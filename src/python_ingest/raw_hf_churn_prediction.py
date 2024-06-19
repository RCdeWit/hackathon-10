import json
import logging
import pandas as pd
import requests

from y42.v1.decorators import data_loader

# use the @data_loader decorator to materialize an asset
# make sure you have a corresponding .yml table definition matching the function's name
# for more information check out our docs: https://www.y42.com/docs/sources/ingest-data-using-python

@data_loader
def raw_hf_churn_prediction(context) -> pd.DataFrame:
    # Your code goes here
    url = "hf://datasets/scikit-learn/churn-prediction/dataset.csv"
    data = pd.read_csv(url)

    # Return a DataFrame which will be materialized within your data warehouse
    df = pd.DataFrame(data)

    logging.info("Data fetched and DataFrame created successfully.")

    # to learn how to set up incremental updates and more
    # please visit https://www.y42.com/docs/sources/ingest-data-using-python
    return df
