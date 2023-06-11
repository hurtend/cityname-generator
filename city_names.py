import tkinter as tk 
import random

root = tk.Tk()
root.geometry('200x50')

first_name = ["HAM", "ELM", "ELDER", "RING", "FLINT", "FLY", "UROROG", "CANDLE", "WITCH", "WINE", "WOOD", "HIGH"]
last_name = ["TOWN", "VILLAGE", "CITY", "LAKE", "FOREST", "RIVER", "HILL", "MOUNTAIN"]

def randomCity():
    rand_first = random.choice(first_name)
    rand_last = random.choice(last_name)
    rand_name = rand_first + rand_last
    box_1st.delete(0, 'end')
    box_1st.insert('end', rand_name)

box_1st = tk.Listbox(root, height=1)

run_btn = tk.Button(root, text='Generate', command=randomCity)

box_1st.pack()
run_btn.pack()

root.mainloop()