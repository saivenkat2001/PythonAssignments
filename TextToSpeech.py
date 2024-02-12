from gtts import gTTS
import os
import random
import csv

csv_file_path = 'house.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

text_csv=""
for row in data_list:
    random_item = random.choice(row)
    text_csv = text_csv + " " + random_item

speech1 = gTTS(text = text_csv, lang = 'en', slow = True)

speech1.save('text1.mp3')

os.system("start text1.mp3")

file = open("sentences.txt", "r").read().replace("\n", ".")

text =str(file)

speech = gTTS(text = text, lang = 'en', slow = True)

speech.save('text.mp3')

os.system('start text.mp3')