from tkinter import *
from gtts import gTTS
from translate import Translator
from win32com.client import Dispatch
import pyttsx3
import os

speaker = Dispatch("SAPI.SpVoice")

engine = pyttsx3.init()


# Translator function
def translate():
    translator = Translator(from_lang=lan1.get(), to_lang=lan2.get())
    translation = translator.translate(var.get())
    var1.set(translation)
    print(var1.get())


def play():
    engine.say(var1.get())
    engine.runAndWait()


# Tkinter root Window with title
root = Toplevel()
root.title("Translator")

# Creating a Frame and Grid to hold the Content
mainframe = Frame(root)
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=10, padx=10)

# variables for dropdown list
lan1 = StringVar(root)
lan2 = StringVar(root)

# choices to show in dropdown menu
lan1_choices = {'English'}
lan2_choices = {'English', 'Spanish', 'German',
                'chinese', 'arabic', 'russian', 'french', 'portuguese', 'italian'
                                                                        'japanese', 'korean', 'greek', 'dutch',
                'turkish', 'malay', 'thai', 'vietnamese', 'indonesian', 'polish', 'hebrew', 'serbian', 'Telugu',
                'Hindi'}
lan1.set('English')
lan2.set('English')

# creating dropdown and arranging in the grid
lan1menu = OptionMenu(mainframe, lan1, *lan1_choices)
Label(mainframe, text="Source language").grid(row=0, column=1)
lan1menu.grid(row=1, column=1)

lan2menu = OptionMenu(mainframe, lan2, *lan2_choices)
Label(mainframe, text="Translated language").grid(row=0, column=2)
lan2menu.grid(row=1, column=2)

# Text Box to take user input
Label(mainframe, text="Enter text").grid(row=2, column=0)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=2, column=1)

# textbox to show output
# label can also be used
Label(mainframe, text="Output").grid(row=2, column=2)
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1).grid(row=2, column=3)

# creating a button to call Translator functi on
# click_btn = PhotoImage(file="text.png")

b = Button(mainframe,text='translate', command=lambda: [translate(), play()], anchor=CENTER).grid(row=3, column=1,
                                                                                                  columnspan=3)

root.mainloop()
