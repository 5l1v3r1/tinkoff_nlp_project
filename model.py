from keras import backend as K
from keras.models import Model
from keras.layers import Embedding, Flatten, Input, merge, concatenate, Lambda
from keras.optimizers import Adam

def identity_loss(y_true, y_pred):

    return K.mean(y_pred - 0 * y_true)


def bpr_triplet_loss(X):
	positive_item_latent, negative_item_latent, user_latent = X[0], X[1], X[2]
	loss = 1.0 - K.sigmoid(
		K.sum(user_latent * positive_item_latent, axis=-1, keepdims=True) -
		K.sum(user_latent * negative_item_latent, axis=-1, keepdims=True))
	return loss

class RetrievalBasedModel():
	def __init__(self, sentence_length, vocab_size, embed_dim):
		self._model = None
		self._build_model(sentence_length, vocab_size, embed_dim)
		print(self._model.summary())

	def _build_model(self, sentence_length, vocab_size, embed_dim):
		positive_answer_input = Input((1, ), name='positive_answer_input')
		negative_answer_input = Input((1, ), name='negative_answer_input')
		context_input = Input((1, ), name='context_input')

		answer_embedding_layer = Embedding(
		    vocab_size, sentence_length, name='word_embedding', input_length=sentence_length)
		average_embedding_layer = Lambda(lambda x: keras.backend.mean(x, axis=1))

		positive_answer_embedding = answer_embedding_layer(
		    positive_answer_input)
		negative_answer_embedding = answer_embedding_layer(
		    negative_answer_input)
		context_embedding = answer_embedding_layer(
			context_embedding)

		positive_answer_average_embedding = average_embedding_layer(
			positive_answer_embedding)
		negative_answer_average_embedding = average_embedding_layer(
			negative_answer_embedding)
		context_answer_average_embedding = average_embedding_layer(
			context_embedding)

		concatenate_layer = concatenate(
			[positive_answer_average_embedding, negative_answer_average_embedding, context_answer_average_embedding],
		       name='concatenate')
		lambda_ = Lambda(bpr_triplet_loss)
		lambda_layer = lambda_(concatenate_layer)

		self._model = Model(
		    input=[positive_answer_input, negative_answer_input, context_input],
		    output=lambda_layer)
		self._model.compile(loss=identity_loss, optimizer=Adam())

	def train(self, train_uid, train_pid, train_nid, num_epochs):
		for epoch in range(num_epochs):
		    print('Epoch ' + epoch)

		    X = {
		        'context_input': train_uid,
		        'positive_answer_input': train_pid,
		        'negative_answer_input': train_nid
		    }

		    model.fit(X,
		              np.ones(len(train_uid)),
		              batch_size=64,
		              nb_epoch=1,
		              verbose=1,
		              shuffle=True)

	def get_response(self, text):
		return 'Reply to text' #TO IMPLEMENT