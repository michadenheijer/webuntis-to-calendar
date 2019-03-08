from __future__ import print_function
import datetime
import pickle
import os.path
import time
import threading
import sys
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

current = os.path.dirname(sys.argv[0])
SCOPES = ['https://www.googleapis.com/auth/calendar']
with open(current + "config.json") as f:
    data = json.load(f)
    global calendarId
    calendarId = data['calendar_id']

def add_event(start, end, name, location):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': str(name),
        'location': str(location),
        'start': {
            'dateTime': convert_date(start),
            'timeZone': 'Europe/Amsterdam'
        },
        'end': {
            'dateTime': convert_date(end),
            'timeZone': 'Europe/Amsterdam'
        },
        'reminders':{
            'useDefault': True
        }
    }
    event = service.events().insert(calendarId=calendarId, body=event).execute()
    print("Added "+ str(name))
    
def convert_date(event):
    return str(event.date()) + 'T' + str(event.time())


thread_list = []
def delete_events():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    events_result = service.events().list(calendarId=calendarId, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    print("Deleting", len(events), "prior events")
    if not events:
        print('No upcoming events found.')
        return
    for event in events:
        time.sleep(0.2)
        thread = threading.Thread(target=delete_event, args=(event['id'],))
        thread_list.append(thread)
        thread.start()
    time.sleep(10)
    print("Finished")
        
def delete_event(eventid):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    service.events().delete(calendarId=calendarId, eventId=eventid).execute()
    print("Deleted event with id: ", str(eventid))
    
