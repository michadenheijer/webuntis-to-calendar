from to_google_cal import add_event, delete_events
import sys
import os.path
from os import path
import threading
import datetime
import json
import webuntis

current = os.path.dirname(sys.argv[0])
today = datetime.date.today()
end = today + datetime.timedelta(days=14)

with open(current + "config.json") as f:
    data = json.load(f)
    global username, password, server, school, studentID
    username = data["username"]
    password = data["password"]
    server = data["server"]
    school = data["school"]
    studentID = data["webuntis_id"]

try:
    if path.exists(current + "wrong_pass"):
        print("Last time wrong password, not trying again")
        exit()
    with webuntis.Session(
        username=username,
        password=password,
        server=server,
        school=school,
        useragent='Chrome'
    ).login() as s:
        lesson_request = s.timetable(student=studentID, start=today, end=end)
        delete_events()
        for lesson in lesson_request:
            if lesson.code != 'cancelled':
                lesson.rooms = str(lesson.rooms).replace("[", "")
                lesson.rooms = str(lesson.rooms).replace("]", "")
                lesson.subjects = str(lesson.subjects).replace("[", "")
                lesson.subjects = str(lesson.subjects).replace("]", "")
                thread = threading.Thread(target=add_event, args=(lesson.start, lesson.end, lesson.subjects, lesson.rooms,))
                thread.start()
except webuntis.errors.BadCredentialsError:
    print("Wrong password")
    f = open(current + "wrong_pass", "w+")
    f.close()
