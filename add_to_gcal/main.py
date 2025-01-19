import datetime
import os.path
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    """
    Adds Vanderbilt basketball games to the user's Google Calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Define your events. 
    # Change the year (2025) to the correct year if needed.
    # Each event is assumed 2 hours long, from startTime to startTime + 2 hours.
    # Times are in 24-hour format (e.g., 18:00 for 6:00 pm).
    # You can adjust the 'timeZone' if you want something other than America/Chicago.
    
    games = [
        {
            "summary": "Vanderbilt @ Alabama",
            "location": "Tuscaloosa, Ala.",
            "start": {"dateTime": "2025-01-21T18:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-01-21T20:00:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt vs Kentucky",
            "location": "Nashville, Tenn.",
            "start": {"dateTime": "2025-01-25T13:30:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-01-25T15:30:00", "timeZone": "America/Chicago"},
            "description": "TV: ESPN"
        },
        {
            "summary": "Vanderbilt @ Oklahoma",
            "location": "Norman, Okla.",
            "start": {"dateTime": "2025-02-01T14:30:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-02-01T16:30:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt @ Florida",
            "location": "Gainesville, Fla.",
            "start": {"dateTime": "2025-02-04T18:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-02-04T20:00:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt vs Texas",
            "location": "Nashville, Tenn.",
            "start": {"dateTime": "2025-02-08T12:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-02-08T14:00:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt vs Auburn",
            "location": "Nashville, Tenn.",
            "start": {"dateTime": "2025-02-11T18:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-02-11T20:00:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt @ Tennessee",
            "location": "Knoxville, Tenn.",
            "start": {"dateTime": "2025-02-15T12:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-02-15T14:00:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt @ Kentucky",
            "location": "Lexington, Ky.",
            "start": {"dateTime": "2025-02-19T18:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-02-19T20:00:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt vs Ole Miss",
            "location": "Nashville, Tenn.",
            "start": {"dateTime": "2025-02-22T14:30:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-02-22T16:30:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt @ Texas A&M",
            "location": "College Station, Texas",
            "start": {"dateTime": "2025-02-26T18:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-02-26T20:00:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt vs Missouri",
            "location": "Nashville, Tenn.",
            "start": {"dateTime": "2025-03-01T17:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-03-01T19:00:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt vs Arkansas",
            "location": "Nashville, Tenn.",
            "start": {"dateTime": "2025-03-04T21:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-03-04T23:00:00", "timeZone": "America/Chicago"},
            "description": "TV: SEC Network"
        },
        {
            "summary": "Vanderbilt @ Georgia",
            "location": "Athens, Ga.",
            "start": {"dateTime": "2025-03-08T11:00:00", "timeZone": "America/Chicago"},
            "end":   {"dateTime": "2025-03-08T13:00:00", "timeZone": "America/Chicago"},
            "description": "TV: ESPNU"
        }
    ]

    # Insert each event into your Google Calendar
    for game in games:
        event_result = service.events().insert(
            calendarId='primary',
            body={
                'summary': game['summary'],
                'location': game['location'],
                'description': game['description'],
                'start': game['start'],
                'end': game['end']
            }
        ).execute()

        print(f"Created event: {event_result['summary']} "
              f"(ID: {event_result['id']})")

if __name__ == '__main__':
    main()
