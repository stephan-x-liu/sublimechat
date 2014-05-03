import sublime, sublime_plugin
import time
import hipchat
import datetime
from threading import Timer

class ChatCommand(sublime_plugin.TextCommand):
	active_users = {}
	r = ""
	api = ""
	last_date = 0
	last_said = ""

	def run(self, edit):
		self.api = hipchat.Api('c788049b7b63fce72646b09d633c81')
		self.r = self.api.rooms.show(549073)
		self.refresh(edit)
		time.sleep(0.1)
		i = 0
		self.show_input_panel_with_readline(sublime.active_window().active_view(), edit)

	def refresh(self, edit):
		message = self.fetch_update();
		for sender in message.keys():
			if sender not in self.active_users.keys():
				view = sublime.active_window().new_file()
				view.set_name("Chat: " + sender)
				view.set_read_only(True)
				view.reciever = sender
				self.active_users[sender] = view
				view.set_scratch(True)
			for dialogue in message[sender]:
				if dialogue != self.last_said:
					self.display(edit, self.active_users[sender], dialogue)

	def auto_refresh(self,edit):
		while True:
			self.refresh(edit)
			time.sleep(1)


	def display(self, edit, view, message):
		view.set_read_only(False)
		view.insert(edit, view.size(), "\n" + view.reciever + "> " + message)
		view.show_at_center(view.size())
		view.set_read_only(True)
	
	def show_input_panel_with_readline(self, view, edit):
		x = []
		def helper(y):
			
			if view.id() is sublime.active_window().active_view().id():
				self.display_at_bottom(view, edit, y)
				# send_message(user, y)
			self.run(edit)
			# self.show_input_panel_with_readline(sublime.active_window().active_view() , edit)
			# print(type(str(y)))
		sublime.active_window().show_input_panel("Your message:", "", helper, None, None)
		

	def display_at_bottom(self, view, edit, x):
		view.set_read_only(False)
		self.last_said = x
		self.r.message(x)
		view.insert(edit, view.size(), "\nMe> "+x)
		view.show_at_center(view.size())
		view.set_read_only(True)

	def fetch_update(self):
		user = self.r.history()[0].from_user
		user.name = "Stephan"
		message_list = self.r.history()[::-1]
		final = []
		for message in message_list:
			if type(self.last_date) != int and message.date <= self.last_date:
				break
			final += [message]
		self.last_date = message_list[0].date
		return {user.name : [unicode(msg) for msg in final[::-1]]}

lst = [0]

def get_usermessage():
	if lst[0]==0:
		lst[0] = 1
		return {"Sahai" : ["How long does this problem really take?", "5 minutes?", "It takes me at least 1/5 that time"]}
	else:
		return {"Sahai": ["I'm sorry"]}

def send_message(user, x):
	return None