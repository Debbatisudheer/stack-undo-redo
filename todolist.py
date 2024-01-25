class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def display_text(self):
        print("Current Text:", self.text)

    def add_text(self, new_text):
        self.undo_stack.append(self.text)
        self.text += new_text
        self.redo_stack = []  # Clear redo stack when a new text is added
        self.display_text()

    def undo(self):
        if self.undo_stack:
            previous_text = self.undo_stack.pop()
            self.redo_stack.append(self.text)
            self.text = previous_text
            self.display_text()
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.redo_stack:
            next_text = self.redo_stack.pop()
            self.undo_stack.append(self.text)
            self.text = next_text
            self.display_text()
        else:
            print("Nothing to redo.")

# Example Usage:
text_editor = TextEditor()

while True:
    user_input = input("Type something (or type 'undo'/'redo' to undo/redo): ")

    if user_input.lower() == 'undo':
        text_editor.undo()
    elif user_input.lower() == 'redo':
        text_editor.redo()
    else:
        text_editor.add_text(user_input)







