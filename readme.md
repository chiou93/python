
This code implements a note console application that allows the user to save, read, add, edit, and delete notes. Notes contain an ID, a title, a note body, and the date/time the note was created or last modified, and are saved in JSON format.

When the program starts, it loads the existing notes from the JSON file and provides the user with commands to perform operations on the notes:

* add - add a new note
* read - read an existing note by id
* edit - edit an existing note by id
* delete - delete an existing note by id
* list - list all notes
* help - display information about commands
* quit - exit the program
* filter - filter notes by date


When performing add and edit operations, the user must enter an ID, title, and body of the note. When performing an edit operation, the user can also change the title and body of the note.

On each operation, the program saves the modified note dictionary to a JSON file so that the changes persist between program runs.

