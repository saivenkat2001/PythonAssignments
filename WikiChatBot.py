import tkinter as tk
from tkinter import scrolledtext
from wikipediaapi import Wikipedia

def search_server_info(query):
    wiki = Wikipedia(language='en', user_agent='WikipediaSearchBot/1.0')
    page = wiki.page(query)
    if page.exists():
        return page.summary
    else:
        return "Sorry, I couldn't find information about that."

def submit_query():
    query = entry.get()
    response = search_server_info(query)
    output.config(state=tk.NORMAL)
    output.delete('1.0', tk.END)  # Clear previous content
    output.insert(tk.END, response + "\n\n")
    output.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Server Info Chatbot")

# Create input entry
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=0, padx=10, pady=10)

# Create submit button
submit_btn = tk.Button(root, text="Submit", command=submit_query)
submit_btn.grid(row=0, column=1, padx=10, pady=10)

# Create output text area
output = scrolledtext.ScrolledText(root, width=60, height=20)
output.grid(row=1, columnspan=2, padx=10, pady=10)
output.config(state=tk.DISABLED)

# Start the GUI
root.mainloop()
