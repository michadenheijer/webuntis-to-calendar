"""
This is the main program
"""
import os
from os import path

import sys
import threading
import datetime
import json
import subprocess
import webuntis

CURRENT = os.path.dirname(sys.argv[0])
TODAY = datetime.date.today()
END = TODAY + datetime.timedelta(days=14)

if not path.exists(CURRENT + 'config.json'):
    CONFIG = ['python3', 'config.py']
    subprocess.Popen(CONFIG).wait()

from google_cal import add_event, delete_events

with open(CURRENT + "config.json") as FILE:
    DATA = json.load(FILE)
    global USERNAME, PASSWORD, SERVER, SCHOOL, STUDENTID
    USERNAME = DATA["username"]
    PASSWORD = DATA["password"]
    SERVER = DATA["server"]
    SCHOOL = DATA["school"]
    STUDENTID = DATA["webuntis_id"]

try:
    if path.exists(CURRENT + "wrong_pass"):
        print("Last time wrong password, not trying again")
        exit()
    with webuntis.Session(
        username=USERNAME,
        password=PASSWORD,
        server=SERVER,
        school=SCHOOL,
        useragent='Chrome'
    ).login() as s:
        LESSON_REQ = s.timetable(student=STUDENTID, start=TODAY, end=END)
        delete_events()
        for lesson in LESSON_REQ:
            if lesson.code != 'cancelled':
                lesson.rooms = str(lesson.rooms).replace("[", "")
                lesson.rooms = str(lesson.rooms).replace("]", "")
                lesson.subjects = str(lesson.subjects).replace("[", "")
                lesson.subjects = str(lesson.subjects).replace("]", "")
                thread = threading.Thread(target=add_event, \
                    args=(lesson.start, lesson.end, lesson.subjects, lesson.rooms,))
                thread.start()
except webuntis.errors.BadCredentialsError:
    print("Wrong password")
    FILE = open(CURRENT + "wrong_pass", "w+")
    FILE.close()
