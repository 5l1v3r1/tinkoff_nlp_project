import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer

def filter_nans(data):
  for i, el in enumerate(data):
    if type(el) != str:
      data[i] = ''

def tokenize_data(csv_file):
	df = pd.read_csv(csv_file)
	context = df["context"]
	answer = df["answer"]
	tokenizer = Tokenizer(num_words=5000)
	united_data = np.concatenate((context, answer), axis = None)
	tokenizer.fit_on_texts(united_data)
	tokenized_context = tokenizer.texts_to_sequences(context)
	tokenized_answer = tokenizer.texts_to_sequences(answer)
	return tokenized_context, tokenized_answer

def compute_max_length(tokenized_data):
	return max([len(i) for i in tokenized_data])

def get_triplets(context, answer):
	neg = np.copy(answer)
	np.random.shuffle(neg)
	return context, answer, neg