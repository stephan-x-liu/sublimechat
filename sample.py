import sublime, sublime_plugin
	
class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print(type(edit))
		print(type(self.view))
		print(len(sublime.windows()))
		for window in sublime.windows():
			print([view.id() for view in window.views()])
		window.show_input_panel("string", "text", None, None, None)
		#sublime.active_window().new_file()
		viewlist = sublime.active_window().views()
		print(viewlist)
		self.view.insert(edit, 0, "")
		self.view.settings().set("name", "thing")
		print(self.view.settings().get("name"))
		print(self.view.settings().has("name"))

def func(x):
	print(x)
	return x
while True:
	x = 4