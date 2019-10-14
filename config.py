"""
The config function
"""
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import json
import os
import sys

CURRENT = os.path.dirname(sys.argv[0])
STORE = os.path.join(CURRENT, "config.json")
WRONG_PASS = os.path.join(CURRENT, "wrong_pass")

QUESTIONS = [
    {
        'type': 'input',
        'name': 'username',
        'message': 'What\'s your WebUntis username',
    },
    {
        'type': 'password',
        'name': 'password',
        'message': 'What\'s your WebUntis password',
    },
    {
        'type': 'input',
        'name': 'server',
        'message': 'What\'s your Webuntis server',
    },
    {
        'type': 'input',
        'name': 'school',
        'message': 'What\'s your school',
    },
    {
        'type': 'input',
        'name': 'webuntis_id',
        'message': 'What\'s your WebUntis id',
    },
    {
        'type': 'input',
        'name': 'calendar_id',
        'message': 'What\'s your calendar id (primary)',
        'default': 'primary'
    }
]

def config():
    ANSWERS = prompt(QUESTIONS)
    
    with open(STORE, "w+") as CONFIG:
        CONFIG.write(json.dumps(ANSWERS))
    
    if os.path.exists(WRONG_PASS):
        os.remove(WRONG_PASS)

if __name__ == "__main__":
    config()
