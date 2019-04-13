from preprocess import tokenize_data

def train(data_csv, model):
	context, answer = tokenize_data(data_csv)
	print('tokenized!')
	