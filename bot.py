import telepot
from model import RetrievalBasedModel
from telepot.delegate import (per_chat_id, create_open, pave_event_space)
from telepot.loop import MessageLoop
import time
import sys

SetProxy = telepot.api.set_proxy("http://110.164.58.106:8082") #remove if not russian hosting :)

def is_command(text):
		return len(text) > 1 and text[0] == '/' 

class TalkativeGuyChatHandler(telepot.helper.ChatHandler):
	def __init__(self, seed_tuple, **kwargs):
		self._model = RetrievalBasedModel()
		super(TalkativeGuyChatHandler, self).__init__(seed_tuple, **kwargs)
		print('oru')

	def on_chat_message(self, msg):
		content_type, chat_type, chat_id = telepot.glance(msg)
		print('msg')
		if content_type == 'text':
			if msg.get('text', None) and is_command(msg['text']):
				print('commad')
				self._handle_text_command(msg['text'])
			else:
				self._handle_text_message(msg['text'])
			
	def _handle_text_command(self, text):
		self.sender.sendMessage('Reply to text command') #TODO 

	def _handle_text_message(self, text):
		answer = self._model.get_response(text) #TODO 
		self.sender.sendMessage(answer)


class TalkativeGuyBot(telepot.DelegatorBot):
	def __init__(self, token):
		super(TalkativeGuyBot, self).__init__(token, [
            # Handler for the chat actions
            pave_event_space()(per_chat_id(), create_open, TalkativeGuyChatHandler, timeout=1000000)
        ])

def start_bot(TOKEN):
	bot = TalkativeGuyBot(TOKEN)

	MessageLoop(bot).run_as_thread()
	print ('BotHosting: I am listening ...')

	while 1:
	    time.sleep(4)