# In GUI should allow unique numbers only
# ex:342,541 - correct
# 233,2243 - wrong
# give numbers between (1-5)
# 1,2,3,4,5,
# (12)-1,2,3(1+2),
# (31)-1,3,4
# (14)-1,4,5
# 321-1,2,3,4,5,6
# 2431-1,2,3,4,5(1+4),7(4+3),6(1+2+3),8(1+4+3),9(2+3+4),(1+2+3+4=10)(10,1+0=1)1
# 543-3,4,5,7(3+4),8(3+5),9(5+4),(5+4+3)(12)(1+2)3
# select those sentences from excel and get the words and find
# that sentence from sentences.txt and display on GUI
# Doc attached in the mail (Dad.xlsx, sentences_dad.txt)



import pandas as pd
from tkinter import *

root = Tk()
frame = Entry(root)


def sum_series():
    list1 = []
    list2 = []

    input_digit = ID.get()

    for i in str(input_digit):
        list1.append(int(i))
        list2.append(int(i))

    for x in range(len(list1)):
        for y in range(len(list1)):
            if x != y:

                val = (list1[x] + list1[y])
                # print(val)
                if val not in list2:
                    list2.append(val)
    print(list1)
    print(list2)
    f = open('sentences_dad.txt', 'r')
    res = f.read()
    res = res.lower()  # converts to lowercase
    to_list = res.split(".")
    df = pd.read_excel('Dad.xlsx', header=None)
    df.columns = ["col1", "col2"]
    df['col1'] = df['col1'].str.lower()
    df['col2'] = df['col2'].str.lower()

    df.head()
    print(df)
    df_list_data = df.values.tolist()
    res_list = []
    for num in list2:
        res_list.append(df_list_data[num - 1])

    for i in res_list:
        for j in to_list:
            srch_1 = i[0]
            srch_2 = i[1]

            rs = j.find(str(srch_1))
            rs1 = j.find(str(srch_2))
            if rs != -1 and rs1 != -1:
                print(j)


label = Label(root, text='input: ').grid(row=0, column=0)
ID = StringVar()

entry = Entry(root, textvariable=ID).grid(row=0, column=0)
frame.grid(row=0, column=0)

button = Button(root, text="get_sentences", command=sum_series).grid(row=0, column=3)
root.mainloop()

