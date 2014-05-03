import sublime, sublime_plugin

def show_input_panel_with_readline(window):
	def helper(y):
		nonlocal x
		x = y
	x = ""
	view = window.show_input_panel("Your message:", "", helper, None, None)
	display_at_bottom(view, x)
	send_message(user, x)
	show_input_panel_with_readline(window)


