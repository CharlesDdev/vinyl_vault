# Core RecordApp class with all features

import tkinter as tk
from tkinter import messagebox #shows pop-up messages

class RecordApp: #defines class
   def __init__(self, root):
      self.root = root
      self.root.title("Vinyl Vault")
      self.records = [] #empty list to store records

      # Labels and Entry fields
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

      # Save button
      tk.Button(root, text="Save Record", command=self.save_record).grid(row=5, column=0, columnspan=2, pady=10)

   # {{REWRITTEN_CODE}}
   def save_record(self):
          # Get input values
          artist = self.artist_entry.get()
          album = self.album_entry.get()
          year = self.year_entry.get()
          genre = self.genre_entry.get()
          condition = self.condition_entry.get()

          # Basic validation
          if not all([artist, album, year, genre, condition]):
              messagebox.showerror("Error", "All fields are required!")
              return
          if not year.isdigit():
              messagebox.showerror("Error", "Year must be a number!")
              return

          # Store Record
          record = {"artist": artist, "album": album, "year": int(year), "genre": genre, "condition": condition}
          self.records.append(record)

          # Clear inputs
          self.artist_entry.delete(0, tk.END)
          self.album_entry.delete(0, tk.END)
          self.year_entry.delete(0, tk.END)
          self.genre_entry.delete(0, tk.END)
          self.condition_entry.delete(0, tk.END)

          messagebox.showinfo("Success", "Record saved!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecordApp(root)
    root.mainloop()
