import sys
from src.text_classification import * 

training_path = sys.argv[-2]
input_text = sys.argv[-1]


model, words = get_model_from_data(training_path)
print(classify_content(input_text, model, words))