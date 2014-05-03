import hipchat

api = hipchat.Api('c788049b7b63fce72646b09d633c81')

for room in api.rooms.list():
    print room.name, room.topic, room.room_id

for user in api.users.list():
    print user.name, user.photo_url

r = api.rooms.show(549073)
r.message("bitch fuck cunt ass")

lst = r.history()
prevdate = 0
for message in lst:
    print(type(message.date))

"""import xmpp

username = 'i.am.gauthamke'
passwd = 'Aparides9'
to='guardianxero@gmail.com'
msg='hello :)'

def func(x):
    return 1

client = xmpp.Client('gmail.com')
client.connect(server=('talk.google.com',5223))
client.auth(username, passwd, 'botty')
client.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
thing = client.send(message)
def func(connect_object, message_node):
    print(message_node)
client.RegisterHandler('message', func)
while client.Process(1):
    pass
#response = client.WaitForResponse(thing, 5)
#response = client.WaitForResponse(thing, 5)
#client.send(message)
#thing = client.WaitForResponse("B363BC89", 5)


"""
"""
import xmpp

FACEBOOK_ID = "gautham.kesineni@chat.facebook.com"
PASS = "Knightsofparadice9"
SERVER = "chat.facebook.com"

jid=xmpp.protocol.JID(FACEBOOK_ID)

client=xmpp.Client(jid.getDomain(),debug=['always'])
if not client.connect((SERVER,5222)):
    raise IOError('Can not connect to server.')
if not client.auth(jid.getNode(),PASS):
    raise IOError('Can not auth with server.')

message = xmpp.protocol.Message(frm=client.Bind.bound[0], to="guardianxero@chat.facebook.com", typ="chat", body="Hello world",)
client.SendAndWaitForResponse(message)"""
"""
import socket
import os
import select
import sys

def prompt():

   sys.stdout.flush()

PORT = 2200
HOST = '10.142.36.205'
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.connect((HOST, PORT))

print 'Connected to remote host. Start sending messages'
prompt()

try:
    while True:

        socket_list = [sys.stdin, s]

        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    sys.stdout.write(data)
                    prompt()
            else:
                msg = sys.stdin.readline()
                s.send('\r<Test Account>: ' + msg)
                prompt()
except KeyboardInterrupt:
    s.close()
"""