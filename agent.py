import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

root = tk.Tk()
root.title("Your AI Assistant")

# Adding a background color
root.configure(bg="lightblue")

# define the function to automate youtube search 
def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# define the function to automate google search
def search_google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# define the function to automate instagram search    
def search_instagram():
    username = entry.get().replace("@", "")
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)

# create input fields, labels, buttons 
Label(root, text="Enter your command", bg="lightblue").pack(pady=10)

entry = Entry(root, width=50)
entry.pack(pady=10)

Button(root, text="Search on YouTube", command=search_youtube).pack(pady=5)
Button(root, text="Search on Google", command=search_google).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram).pack(pady=5)

# run the GUI event loop 
root.mainloop()
