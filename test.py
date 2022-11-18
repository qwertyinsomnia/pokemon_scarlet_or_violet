import time
import random
import tkinter as tk
import os

class Trainee():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("choose")
        # self.root.overrideredirect(1) # remove taskbar

        # position
        screen_width = 100
        screen_height = 100
        print(self.root.winfo_screenwidth(), self.root.winfo_screenheight()) # 1707 960
        screen_resolution = '600x300' + '+' + str(screen_width) + '+' + str(screen_height)
        self.root.geometry(screen_resolution)

        print(os.path)
        image1 = "/Users/insomnia/Desktop/pokemon/pokemon_scarlet.png"
        image2 = "/Users/insomnia/Desktop/pokemon/pokemon_violet.png"
        self.canvas = tk.Canvas(self.root, bd=10, width=500)
        self.canvas.create_image(50, 50, anchor="ne", image=image1)
        self.canvas.create_image(50, 50, anchor="ne", image=image1)
        # self.canvas.create_rectangle(0, 0, 200, 200, fill='grey')
        # self.canvas.create_rectangle(202, 0, 402, 200, fill='grey')
        self.rec = self.canvas.create_rectangle(0, 0, 200, 200, outline='white')
        self.canvas.pack(anchor="n")

        button1 = tk.Button(self.root, text="roll!!!", command=self.generate_choose_seed)
        button1.pack()

        self.index = 0


    def generate_choose_seed(self):
        self.seed = random.randint(1, 10)
        # print(seed)
        # seed = 1
        self.choose()
            


    def choose(self):
        self.index = 1 - self.index
        print(self.index)

        if self.index == 0:
            self.canvas.delete(self.rec)
            self.rec = self.canvas.create_rectangle(0, 0, 200, 200, outline='white', width=10)
        else:
            self.canvas.delete(self.rec)
            self.rec = self.canvas.create_rectangle(202, 0, 402, 200, outline='white', width=10)
        if self.seed > 0:
            self.root.after(1000, self.choose)
            self.seed -= 1

        


if __name__== "__main__":

    cat = Trainee()
    # cat.root.after(0, cat.Update)
    tk.mainloop()