import sublime, sublime_plugin
import time

class ChatCommand(sublime_plugin.TextCommand):
	active_users = {}
	def run(self, edit):
		self.refresh(edit)


		time.sleep(1)
		self.refresh(edit)
		i = 0

		self.show_input_panel_with_readline(sublime.active_window().active_view(), edit)

	def refresh(self, edit):
		message = get_usermessage();
		for sender in message.keys():
			if sender not in self.active_users.keys():
				view = sublime.active_window().new_file()
				view.set_name("Chat: " + sender)
				view.set_read_only(True)
				view.reciever = sender
				self.active_users[sender] = view
				view.set_scratch(True)
			for dialogue in message[sender]:
				self.display(edit, self.active_users[sender], dialogue)

	def display(self, edit, view, message):
		view.set_read_only(False)
		view.insert(edit, view.size(), "\n" + view.reciever + "> " + message)
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
		

	def display_at_bottom(self, view,edit, x):
		view.set_read_only(False)
		view.insert(edit, view.size(), "\nMe> "+x)
		view.set_read_only(True)
	
lst = [0]

def get_usermessage():
	if lst[0]==0:
		lst[0] = 1
		return {"Sahai" : ["How long does this problem really take?", "5 minutes?", "It takes me at least 1/5 that time"]}
	else:
		return {"Sahai": ["I'm sorry"]}

def send_message(user, x):
	return None