from model import RetrievalBasedModel
from preprocess import tokenize_data, get_triplets
from bot import start_bot
import sys

def main():
	action = None
	model = None
	file = None
	token = None
	num_epochs = 10 # default value
	sentence_length, vocab_size, embed_dim = 100, 5000, 20 # default values
	print(sys.argv[1])
	try:
		action = sys.argv[1]
	except:
		print('NO ARGUMENT ERR')

	if action == 'train':
		try:
			file = sys.argv[2]
		except:
			print('NO FILE ARGUMENT ERR')

		try:
			num_epochs = sys.argv[3]
			sentence_length, vocab_size, embed_dim = sys.argv[4], sys.argv[5], sys.argv[6]
		except:
			pass

		model = RetrievalBasedModel(sentence_length, vocab_size, embed_dim)
		context, answer = tokenize_data(file)
		train_uid, train_pid, train_nid = get_triplets(context, answer)
		model.train(train_uid, train_pid, train_nid, num_epochs)
	elif action == 'start_bot':
		try:
			token = sys.argv[2]
		except:
			print('NO TOKEN ARGUMENT ERR')
		
		start_bot(TOKEN)
	else:
		print('UNKNOWN ARGUMENT ERR')

if __name__ == "__main__":
    main()