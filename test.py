from bottle import route, run, response, get, post, request
from json import dumps
import socket

@get('/teamspeak')
def teamspeakOnline():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('testoknof.de', 30033))
    if result == 0:
        return sendResult(0)
    else:	
        return sendResult(1)

def sendResult(value):
    rv = { "result": value }
    response.content_type = 'application/json'
    return dumps(rv)

#run(host='10.112.16.123', port=8080, debug=True)
run(host='testoknof.de', port=8080, debug=True)
