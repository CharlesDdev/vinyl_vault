import tkinter as tk
from tkinter import messagebox, ttk

class RecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vinyl Vault")
        self.records = []  # List to store records

        tk.Label(root, text="Artist").grid(row=0, column=0, padx=5, pady=5)
        self.artist_entry = tk.Entry(root)
        self.artist_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Album").grid(row=1, column=0, padx=5, pady=5)
        self.album_entry = tk.Entry(root)
        self.album_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Year").grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(root)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="Genre").grid(row=3, column=0, padx=5, pady=5)
        self.genre_entry = tk.Entry(root)
        self.genre_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(root, text="Condition").grid(row=4, column=0, padx=5, pady=5)
        self.condition_entry = tk.Entry(root)
        self.condition_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(root, text="Save Record", command=self.save_record).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(root, text="View Collection", command=self.view_records).grid(row=6, column=0, columnspan=2, pady=10)



    def save_record(self):
        artist = self.artist_entry.get()
        album = self.album_entry.get()
        year = self.year_entry.get()
        genre = self.genre_entry.get()
        condition = self.condition_entry.get()
        if not all([artist, album, year, condition]):
            messagebox.showerror("Error", "All fields are required!")
            return
        if not year.isdigit():
            messagebox.showerror("Error", "Year must be a number!")
            return
        record = {"artist": artist, "album": album, "year": int(year), "genre": genre, "condition": condition}
        self.records.append(record)
        self.artist_entry.delete(0, tk.END)
        self.album_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.condition_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Record saved!")

        def view_records(self):
            view_windows = tk.Toplevel(self.root)
            view_window.title("Record Collection")
            tree = ttk.Treeview(view_window, columns="Artist, "Album", "Year", "Genre", "Condition", show="headings")
            tree.heading("Artist", text="Artist")
            tree.heading("Album", text="Album")
            tree.heading("Year", text="Year")
            tree.heading("Genre", text="Genre")
            tree.heading("Condition", text="Condition")
            tree.pack(padx=10, pady=10)
            for record in self.records:
                tree.insert("", tk.END, values=(record["artis"]))




if __name__ == "__main__":
    root = tk.Tk()
    app = RecordApp(root)
    root.mainloop()
