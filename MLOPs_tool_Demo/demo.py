import os
import sys
import warnings


import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
import dagshub
import logging

import dagshub
dagshub.init(repo_owner='Roniwatson4222', repo_name='MLFlowTest', mlflow=True)

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

csv_url = (
    "https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv"
)      
try:
    data=pd.read_csv(csv_url, sep=";")
    logger.info("Data loaded successfully.")
except Exception as e:
        logger.exception(f"Error loading data:%s", e)
train, test = train_test_split(data)

train_x = train.drop(["quality"], axis=1)
test_x = test.drop(["quality"], axis=1)
train_y = train[["quality"]]
test_y = test[["quality"]]

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

with mlflow.start_run():
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    model.fit(train_x, train_y)

    predicted_qualities = model.predict(test_x)

    rmse, mae, r2 = eval_metrics(test_y, predicted_qualities)

    logger.info(f"ElasticNet model (alpha={alpha}, l1_ratio={l1_ratio}):")
    logger.info(f"  RMSE: {rmse}")
    logger.info(f"  MAE: {mae}")
    logger.info(f"  R2: {r2}")

    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("r2", r2)

#for remote server only (Dagshub)
remote_server_uri="https://dagshub.com/Roniwatson4222/MLFlowTest.mlflow"
mlflow.set_tracking_uri(remote_server_uri)

tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

if tracking_url_type_store != "file":
     mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetWineModel")
else:
     mlflow.sklearn.log_model(model, "model")     
