import sys
from finpredict.text_classification import * 
from finpredict.config import get_config_str

def train_nb():
    training_path = get_config_str("training_path", "data/training_data.csv", "Path to training data CSV file")



    model, words = get_model_from_data(training_path)
    return model, words