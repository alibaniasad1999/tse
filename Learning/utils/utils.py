from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

class CreateTSEDataset:
    def __init__(self, data, look_back=60, look_forward=1):
        self.data_scaled = None
        self.data = data
        self.look_back = look_back
        self.look_forward = look_forward
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        # make scaler for each column in data like dict
        self.scaler_dict = {}
        for column in data.columns:
            self.scaler_dict[column] = MinMaxScaler(feature_range=(0, 1))
            self.scaler_dict[column].fit(data[column].values.reshape(-1, 1))   
            
    def create_dataset(self, output_columns=None):    
        if output_columns is None:
            output_columns = ['close']
        X, y = [], []
        for i in range(len(self.data) - self.look_back - self.look_forward+1):
            X.append(self.data.iloc[i:(i + self.look_back)].values)
            y.append(self.data[output_columns].iloc[i + self.look_back: i + self.look_back + self.look_forward].values)
        X = np.array(X)
        y = np.array(y)
        return X, y


    # scale data
    def scale_data(self):
        self.data_scaled = self.data.copy()
        for column in self.data.columns:
            self.data_scaled[column] = self.scaler_dict[column].transform(self.data[column].values.reshape(-1, 1))
        return self.data_scaled

    def create_dataset_scaled(self, output_columns=None):
        if self.data_scaled is None:
            self.scale_data()
        if output_columns is None:
            output_columns = ['close']
        X, y = [], []
        for i in range(len(self.data_scaled) - self.look_back - self.look_forward+1):
            X.append(self.data_scaled.iloc[i:(i + self.look_back)].values)
            y.append(self.data_scaled[output_columns].iloc[i + self.look_back: i + self.look_back + self.look_forward ].values)
        X = np.array(X)
        y = np.array(y)
        return X, y


    def scale_dataframe(self, df):
        df_scaled = df.copy()
        for column in df.columns:
            df_scaled[column] = self.scaler_dict[column].transform(df[column].values.reshape(-1, 1))
        return df_scaled

    def inverse_scale_data(self, data, columns):
        data_ = data.copy()
        data_inverse = pd.DataFrame()
        for i, column in enumerate(columns):
            data_inverse[column] = self.scaler_dict[column].inverse_transform(data_[:, i].reshape(-1, 1)).ravel()
        return data_inverse

    # percentage change for sequence data
    def percentage_change(self, data):
        data_ = data.copy()
        data_pct = data_.pct_change().replace([np.inf, -np.inf], np.nan).fillna(0)
        return data_pct*100
