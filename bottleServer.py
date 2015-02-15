from bottle import run, static_file, request, route, response
import http.client
import dateutil.parser

@route('/saveData', method=['GET'])
def download():

    couchDBConn = http.client.HTTPConnection('127.0.0.1', 5984)

    url = '/test_raspberry3/_design/Readings/_view/all_readings'

    if request.query.startkey:
        #TODO: Fix this on the client side so it doesn't send a double and single quoted string
        queryStartKey = request.query.startkey
        queryStartKey = queryStartKey.replace('\"', '')
        startDate = dateutil.parser.parse(queryStartKey)
        url += '?startKey=' + startDate.utcnow().isoformat() + '/'

    if request.query.endkey:
        url += '&endKey=' + request.query.endkey

    couchDBConn.request('GET', url)
    couchResponse = couchDBConn.getresponse()

    if couchResponse.status == 200:
        data = couchResponse.read()
        # decode to a string and strip new line and /r characters
        data = data.decode('utf-8').rstrip()
        jsonFile = open('/Users/randall/PycharmProjects/bottleTest/dump.json', 'w')
        jsonFile.write(data)
        jsonFile.close()
        return static_file('dump.json', root='/Users/randall/PycharmProjects/bottleTest', download='test.json')

    else:
        response.status = 404
        return '404 not found'



run(host='localhost', port=8080)