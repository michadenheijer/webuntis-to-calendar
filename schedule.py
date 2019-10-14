"""
This is the main program
"""
import os
from os import path

import sys
import datetime
import json
import subprocess
import webuntis

import config

CURRENT = os.path.dirname(sys.argv[0])
TODAY = datetime.date.today()
END = TODAY + datetime.timedelta(days=14)
SCHEDULE = os.path.join(CURRENT, "config.json")
WRONG_PASS = os.path.join(CURRENT, "wrong_pass")

class WrongPasswordError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

if not path.exists(SCHEDULE):
    config.config()

from google_cal import add_event, delete_events

with open(SCHEDULE) as FILE:
    DATA = json.load(FILE)
    global USERNAME, PASSWORD, SERVER, SCHOOL, STUDENTID
    USERNAME = DATA["username"]
    PASSWORD = DATA["password"]
    SERVER = DATA["server"]
    SCHOOL = DATA["school"]
    STUDENTID = DATA["webuntis_id"]

try:
    if path.exists(WRONG_PASS):
        raise WrongPasswordError("Before you've entered a wrong password, run config.py to fix the error.")
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
                add_event(lesson.start, lesson.end, lesson.subjects, lesson.rooms)
except webuntis.errors.BadCredentialsError:
    FILE = open(WRONG_PASS, "w+")
    FILE.close()
    raise WrongPasswordError("The password you entered appears to be wrong.")
