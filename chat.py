import sublime, sublime_plugin

class ChatCommand(sublime_plugin.TextCommand):
	active_users = {}
	def run(self, edit):
		message = get_usermessage();
		for sender in message.keys():
			if sender not in self.active_users.values():
				view = sublime.active_window().new_file()
				view.set_name("Chat: " + sender)
				view.reciever = sender
				self.active_users[sender] = view
			for dialogue in message[sender]:
				self.display(edit, self.active_users[sender], dialogue)

	def display(self, edit, view, message):
		view.insert(edit, view.size(), "\n" + view.reciever + "> " + message)

def get_usermessage():
	return {"Sahai" : ["How long does this problem really take?", "5 minutes?", "It takes me at least 1/5 that time"]}