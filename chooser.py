import time
import random
import tkinter as tk
import os

class Trainee():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("scarlet or violet???")
        # self.root.overrideredirect(1) # remove taskbar

        # position
        screen_width = 100
        screen_height = 100
        print(self.root.winfo_screenwidth(), self.root.winfo_screenheight()) # 1707 960
        screen_resolution = '520x480' + '+' + str(screen_width) + '+' + str(screen_height)
        self.root.geometry(screen_resolution)

        print(os.path)
        self.image1 = tk.PhotoImage(file="pokemon_scarlet2.png")
        self.image2 = tk.PhotoImage(file="pokemon_violet2.png")
        self.canvas = tk.Canvas(self.root, bd=10, width=500, height=400)
        self.canvas.create_image((10, 10), anchor="nw", image=self.image1)
        self.canvas.create_image((520, 10), anchor="ne", image=self.image2)
        # self.canvas.create_rectangle(0, 0, 200, 200, fill='grey')
        # self.canvas.create_rectangle(202, 0, 402, 200, fill='grey')
        self.rec = self.canvas.create_rectangle(10, 10, 260, 410, outline='white')
        # self.rec = self.canvas.create_rectangle(265, 15, 505, 405, outline='yellow', width=10)
        self.canvas.pack(anchor="n")

        button1 = tk.Button(self.root, text="开roll!!!", font=18, command=self.generate_choose_seed)
        button1.pack()

        self.index = 0


    def generate_choose_seed(self):
        self.seed = random.randint(20, 40)
        # print(seed)
        # seed = 1
        self.choose()
            


    def choose(self):
        self.index = 1 - self.index
        # print(self.index)

        if self.index == 0:
            self.canvas.delete(self.rec)
            self.rec = self.canvas.create_rectangle(15, 15, 255, 405, outline='yellow', width=10)
        else:
            self.canvas.delete(self.rec)
            self.rec = self.canvas.create_rectangle(265, 15, 505, 405, outline='yellow', width=10)
        if self.seed > 10:
            self.root.after(100, self.choose)
            self.seed -= 1
        elif self.seed > 4:
            self.root.after(200, self.choose)
            self.seed -= 1
        elif self.seed > 0:
            self.root.after(400, self.choose)
            self.seed -= 1

        


if __name__== "__main__":

    cat = Trainee()
    # cat.root.after(0, cat.Update)
    tk.mainloop()