import tkinter as tk
import pymysql

class NoteTakingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Taking App")
        self.root.geometry("600x450")  # Set a larger window size

        self.conn = pymysql.connect(
            host="localhost",
            user="UNAME",
            password="PASSWD",
            database="DB_NAME"
        )

        self.create_widgets()
        self.refresh_notes_list()
    
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack()

        self.content_label = tk.Label(self.root, text="Content:")
        self.content_label.pack()

        self.content_text = tk.Text(self.root, height=10, width=60)  # Increased width
        self.content_text.pack()

        self.save_button = tk.Button(self.root, text="Save Note", command=self.save_note)
        self.save_button.pack()

        self.notes_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=40)  # Adjusted width
        self.notes_listbox.pack()
        self.notes_listbox.bind("<<ListboxSelect>>", self.display_selected_note)

        self.delete_button = tk.Button(self.root, text="Delete Note", command=self.delete_note)
        self.delete_button.pack()

    def delete_note(self):
        selected_index = self.notes_listbox.curselection()[0]
        selected_title = self.notes_listbox.get(selected_index)
        
        cursor = self.conn.cursor()
        query = "DELETE FROM notes WHERE title = %s"
        cursor.execute(query, (selected_title,))
        self.conn.commit()
        cursor.close()
        
        self.refresh_notes_list()
        self.clear_note_display()

    def clear_note_display(self):
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)

    def refresh_notes_list(self):
        cursor = self.conn.cursor()
        query = "SELECT id, title FROM notes"
        cursor.execute(query)
        notes = cursor.fetchall()
        self.notes_listbox.delete(0, tk.END)
        for note in notes:
            self.notes_listbox.insert(tk.END, note[1])
        cursor.close()

    def save_note(self):
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END)
        
        cursor = self.conn.cursor()
        query = "INSERT INTO notes (title, content) VALUES (%s, %s)"
        cursor.execute(query, (title, content))
        self.conn.commit()
        cursor.close()
        
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
        
        self.refresh_notes_list()

    def display_selected_note(self, event):
        selected_index = self.notes_listbox.curselection()[0]
        selected_title = self.notes_listbox.get(selected_index)
        
        cursor = self.conn.cursor()
        query = "SELECT content FROM notes WHERE title = %s"
        cursor.execute(query, (selected_title,))
        content = cursor.fetchone()[0]
        cursor.close()
        
        self.content_text.delete("1.0", tk.END)
        self.content_text.insert("1.0", content)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteTakingApp(root)
    root.mainloop()
