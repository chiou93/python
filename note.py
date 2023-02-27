import json
import datetime

notes = {}

def save_notes():
    with open('notes.json', 'w') as f:
        json.dump(notes, f)

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        pass

def add_note():
    id = input("Enter note id: ")
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[id] = {"title": title, "body": body, "timestamp": timestamp}
    save_notes()

def read_note():
    id = input("Enter note id: ")
    if id in notes:
        note = notes[id]
        print(f"Title: {note['title']}\nBody: {note['body']}\nTimestamp: {note['timestamp']}")
    else:
        print("Note not found")

def edit_note():
    id = input("Enter note id: ")
    if id in notes:
        note = notes[id]
        print(f"Current Title: {note['title']}\nCurrent Body: {note['body']}")
        title = input("Enter new note title (leave blank to keep current): ")
        body = input("Enter new note body (leave blank to keep current): ")
        if title:
            note['title'] = title
        if body:
            note['body'] = body
        note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes()
    else:
        print("Note not found")

def delete_note():
    id = input("Enter note id: ")
    if id in notes:
        del notes[id]
        save_notes()
    else:
        print("Note not found")

def list_notes():
    for id, note in notes.items():
        print(f"{id}: {note['title']} ({note['timestamp']})")

def filter_notes_by_date():
    date_str = input('Enter the date for the selection (in the format DD.MM.YYYY): ')
    try:
        date = datetime.datetime.strptime(date_str, '%d.%m.%Y')
        filtered_notes = [note for note in notes if datetime.datetime.strptime(note['date'], '%d.%m.%Y %H:%M:%S') == date]
        list_notes(filtered_notes)
    except ValueError:
        print('Error: invalid date format')

def print_usage():
    print("""
Usage:
  add    - add a new note
  read   - read an existing note
  edit   - edit an existing note
  delete - delete an existing note
  list   - list all notes
  help   - show this usage information
  quit   - quit the program
  filter - filter notes by date
""")

if __name__ == "__main__":
    load_notes()

    while True:
        command = input("Enter command (type 'help' for usage): ")
        if command == "add":
            add_note()
        elif command == "read":
            read_note()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "list":  
            list_notes()
        elif command == "filter":
            filter_notes_by_date()
        elif command == "help":
            print_usage()
        elif command == "quit":
            break
        else:
            print("Invalid command. Type 'help' for usage.")
