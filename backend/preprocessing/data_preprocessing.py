import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataPreprocessing:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.dataset_path)

    def handle_missing_values(self):
        # Fill missing values
        self.data.fillna(self.data.mean(), inplace=True)

    def encode categorical_features(self):
        # Example encoding
        self.data = pd.get_dummies(self.data, drop_first=True)

    def scale_features(self):
        scaler = StandardScaler()
        self.data[self.data.columns] = scaler.fit_transform(self.data[self.data.columns])

    def split_data(self, target_col):
        X = self.data.drop(columns=[target_col])
        y = self.data[target_col]
        return train_test_split(X, y, test_size=0.2, random_state=42)