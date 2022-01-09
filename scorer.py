import pandas as pd 
import pickle
import urllib.request
import os

from sklearn.metrics import mean_squared_error

class Scorer():
    def __init__(self, public_path = './master_key/public_key.csv', 
                private_path = './master_key/private_key.csv', metric = mean_squared_error):
        self.public_path = public_path
        self.private_path = private_path
        self.metric = metric

        self.df_public_key = pd.read_csv(self.public_path)
        self.df_private_key = pd.read_csv(self.private_path)
        
    def calculate_score(self, submission_path, submission_type = 'public'):
        with open(submission_path, 'rb') as f:
            model = pickle.load(f)

        # download raw dataset CSV
        test_fn = "air_quality_test.csv"

        if not os.path.exists(test_fn):
            dataset_url = "https://yashpatel5400.github.io/files/datasets/air_quality_xyz_test.csv"
            urllib.request.urlretrieve(dataset_url, test_fn)

        # load dataset into numpy
        df = pd.read_csv("air_quality.csv", sep=";",header=0, decimal=',')
        df = df[df["Date"] == df["Date"]]

        X = df.values[:,3:-2]
        y = df.values[:,2]
        y_hat = model.predict(X)

        score = sklearn.metrics.r2_score(y, y_hat)

        # if y_submission.isna().sum() > 0:
        #     return ("SUBMISSION HAS NULL VALUE", None)

        return ("SUBMISSION SUCCESS", score)