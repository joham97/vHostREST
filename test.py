from bottle import route, run
import socket

@route('/teamspeak')
def teamspeakOnline():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('testoknof.de', 30033))
	if result == 0:
		return "teamspeak is online"
	else:	
		return "teamspeak is offline"

run(host='testoknof.de', port=8080, debug=True)
