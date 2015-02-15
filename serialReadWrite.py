import serial
import couchdb
import datetime
import json
import http.client

ser = serial.Serial('/dev/tty.usbmodem1411', 9600)


# connect to couchDB instance, in this case the db name is test_raspberry

# this assumes that the couchDB server is running at the default localhost:5894 location
couch = couchdb.Server()

db = couch['test_raspberry3']

hasReadingsView = False

while 1:
    # Get data being transmitted from the arduino, decode from utf-8 format, and strip newlines from
    # resulting string
    jsonString = ser.readline().decode('utf-8').rstrip()

    if jsonString:
        # parse json string into json object
        jsonObj = json.loads(jsonString)

        # need to get the current time in utc, and then convert it to an iso format
        dateCreated = datetime.datetime.utcnow()

        print(dateCreated)
        # add the datetime to the json obj
        jsonObj['dateTime'] = dateCreated.isoformat()

        # print("LOG: input 1: " + jsonObj['input 1'] + "\n" + "     input 2:  " + jsonObj['input 2'] + "\n" +
        #      "     input 3: " + jsonObj['input 3'] + "\n" + "     dateTime: " + jsonObj['dateTime'] +
        #      "\n--------------------")

        # save the document to the database
        db.save(jsonObj)


        # check to see if the couchDB instance has the correct view
        # all_readings set up. This should be standard across all db instances
        conn = http.client.HTTPConnection('127.0.0.1', 5984, timeout=10)
        # check to see if standard 'all_readings' exists
        conn.request("GET", "/test_raspberry2/_design/all_readings")
        couchResponse = conn.getresponse()
        jsonString = couchResponse.read()

        if couchResponse.status == 200:
            data = couchResponse.read()
            jsonString.decode('utf-8').rstrip()
            jsonObj = json.loads(jsonString)
            if jsonObj['views']['Readings']:
                hasReadingsView = True
            else:
                hasReadingsView = False

        # setup connection
        if hasReadingsView is False:
            x = 'do something here'