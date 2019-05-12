"""
Digital Bucket
randomize events
events_pt | columns: id, events, lat, long
By D. Bailey
"""

import random
import PySimpleGUI27 as sg
import sqlite3
import os.path

# randomize event from sqlite database within PySimpleGUI27
def getEvent():

    # variables
    database = '/Users/DavidBailey/db/pythonsqlite.db'
    table = "events_pt"
    value = 'urban'

    # connect to sqlite
    conn = sqlite3.connect(database)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, database)
    with sqlite3.connect(db_path) as db:

        # gui layout
        sg.SetOptions(
            button_color=sg.COLOR_SYSTEM_DEFAULT
            , text_color=sg.COLOR_SYSTEM_DEFAULT
        )
        layout = [[sg.Text('Enter text here', size=(40, 1), font=800)],
                  [sg.Text('What type of event?', size=(15, 1), font=800),
                   # values in event column in database
                   sg.InputCombo(('urban', 'outdoors - hike', 'outdoors - no hike', 'outdoors - hard hike', '13er',
                                  '14er', 'backpacking'), size=(20, 1))],
                  [sg.Button('Submit')]]

        window = sg.Window('Digital Bucket').Layout(layout)
        button, values = window.Read()
        value = ''.join(values)

        # select query on database
        cursor = conn.cursor()
        cursor.execute("SELECT event FROM %s where complete = 'N' and type = '%s'" % (table, value))
        event_list = []
        for record in cursor:
            event_list.append(record)
        main_value_list = random.choice(event_list)
        main_value = ''.join(main_value_list)
        print value
        print main_value

        # update query on database
        cursor.execute("UPDATE %s SET complete = 'Y' where event = '%s' and type = '%s'" % (table, main_value, value))
        conn.commit()

        # show value in gui popup
        sg.Popup('You are going to....', main_value, font='800', size=(40, 1))

getEvent()