import webapp2
import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            self.view.insert(edit, 0, "Hello, World!")

'''
username = 'cbartondock@gmail.com'
passwd = ''
to = 'guardianxero@gmail.com'
msg = 'titty face'

client = xmpp.
'''
