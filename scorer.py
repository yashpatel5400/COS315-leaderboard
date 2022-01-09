import pandas as pd 
import pickle

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

        print(model)
        score = 1.0

        # if y_submission.isna().sum() > 0:
        #     return ("SUBMISSION HAS NULL VALUE", None)

        return ("SUBMISSION SUCCESS", score)