import sublime, sublime_plugin

def show_input_panel_with_readline(view, edit):
	def helper(y):
		nonlocal x
		x = y
	x = ""
	window.show_input_panel("Your message:", "", helper, None, None)
	if view == sublime.active_window().active_view():
		display_at_bottom(view, edit, x)
		send_message(user, x)
	show_input_panel_with_readline(sublime.active_window().active_view() , edit)

def display_at_bottom(view,edit, x):
	view.insert(edit, view.size(), x+"\n")

