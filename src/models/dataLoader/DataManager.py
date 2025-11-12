import pandas as pd
import numpy as np
from src.interfaces.dataLoader import DataLoader
class DataManagerCSV(DataLoader):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)
    
    def __repr__(self) -> str:
        return f"DataManager loading data from {self.file_path}"
        