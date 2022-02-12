import tkinter as tk
import pyttsx3
from tkinter import messagebox as msg
from threading import Thread
from queue import Queue
import time
x = 2
y = ''
player_1 = []
player_2 = []
threads = []
voice = pyttsx3.init()
gender_voice = voice.getProperty("voices")

class TicTac():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("700x525+20+10")
        self.root.resizable(False, False)
        self.frame1()
        self.all_widgets()

    def frame1(self):
        self.first_frame = tk.Frame(self.root)
        self.first_frame.pack(pady=0, padx=0, anchor = "center", expand=1)
        self.second_frame = tk.Frame(self.root)
        self.second_frame.pack(pady=0, padx=0, anchor="center", expand=1)
    def get_value(self, number):
        global x, y
        global player_1, player_2
        global name_one, name_two

        if number == 1:
            if x%2 == 0:
                y = "X"
                print(self.first_button)
                player_1.append(number)
                voice.say("you just played cross")
                voice.setProperty("voice", gender_voice[0].id)
                voice.runAndWait()

            elif x%2!=0:
                y = "0"
                player_2.append(number)
                voice.say("you just played circle")
                voice.setProperty("voice", gender_voice[1].id)
                voice.runAndWait()

            self.first_button.configure(text=y, font="Helvetica, 40", bg="yellow", fg="black", state="disabled")


            x = x+1


        if number == 2:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                voice.say("you just played cross")
                voice.setProperty("voice", gender_voice[0].id)
                voice.runAndWait()
            elif x % 2 != 0:
                y = "0"
                player_2.append(number)
                voice.say("you just played circle")
                voice.setProperty("voice", gender_voice[1].id)
                voice.runAndWait()
            self.second_button.configure(text=y, font="Helvetica, 40", bg="blue", fg="black", state="disabled")
            x = x + 1
        if number == 3:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                voice.say("you just played cross")
                voice.setProperty("voice", gender_voice[0].id)
                voice.runAndWait()
            elif x % 2 != 0:
                y = "0"
                player_2.append(number)
                voice.say("you just played circle")
                voice.setProperty("voice", gender_voice[1].id)
                voice.runAndWait()
            self.third_button.configure(text=y, font="Helvetica, 40", bg="red", fg="black", state="disabled")
            x = x + 1
        if number == 4:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                voice.say("you just played cross")
                voice.setProperty("voice", gender_voice[0].id)
                voice.runAndWait()
            elif x % 2 != 0:
                y = "0"
                player_2.append(number)
                voice.say("you just played circle")
                voice.setProperty("voice", gender_voice[1].id)
                voice.runAndWait()
            self.fourth_button.configure(text=y, font="Helvetica, 40", bg="green", fg="black", state="disabled")
            x = x + 1
        if number == 5:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                voice.say("you just played cross")
                voice.setProperty("voice", gender_voice[0].id)
                voice.runAndWait()
            elif x % 2 != 0:
                y = "0"
                player_2.append(number)
                voice.say("you just played circle")
                voice.setProperty("voice", gender_voice[1].id)
                voice.runAndWait()
            self.fifth_button.configure(text=y, font="Helvetica, 40", bg="grey", fg="black", state="disabled")
            x = x + 1
        if number == 6:
            if x % 2 == 0:
                y = "X"
                voice.say("you just played cross")
                voice.setProperty("voice", gender_voice[0].id)
                voice.runAndWait()
                player_1.append(number)
            elif x % 2 != 0:
                y = "0"
                player_2.append(number)
                voice.say("you just played circle")
                voice.setProperty("voice", gender_voice[1].id)
                voice.runAndWait()
            self.sixth_button.configure(text=y, font="Helvetica, 40", bg="green", fg="black", state="disabled")
            x = x + 1
        if number == 7:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                voice.say("you just played cross")
                voice.setProperty("voice", gender_voice[0].id)
                voice.runAndWait()
            elif x % 2 != 0:
                y = "0"
                player_2.append(number)
                voice.say("you just played circle")
                voice.setProperty("voice", gender_voice[1].id)
                voice.runAndWait()
            self.seventh_button.configure(text=y, font="Helvetica, 40", bg="white", fg="black", state="disabled")
            x = x + 1
        if number == 8:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                voice.say("you just played cross")
                voice.setProperty("voice", gender_voice[0].id)
                voice.runAndWait()
            elif x % 2 != 0:
                y = "0"
                player_2.append(number)
                voice.say("you just played circle")
                voice.setProperty("voice", gender_voice[1].id)
                voice.runAndWait()
            self.eighth_button.configure(text=y, font="Helvetica, 40", bg="violet", fg="black", state="disabled")
            x = x + 1
        if number == 9:
            if x % 2 == 0:
                y = "X"
                player_1.append(number)
                voice.say("you just played cross")
                voice.setProperty("voice", gender_voice[0].id)
                voice.runAndWait()
            elif x % 2 != 0:
                y = "0"
                player_2.append(number)
                voice.say("you just played circle")
                voice.setProperty("voice", gender_voice[1].id)
                voice.runAndWait()
            self.ninth_button.configure(text=y, font="Helvetica, 40", bg="indigo", fg="black", state="disabled")
            x = x + 1
        if self.first_button["text"] == "X" and self.second_button["text"] == "X" and self.third_button["text"] == "X":
            self.first_button.configure(bg="red")
            self.second_button.configure(bg="red")
            self.third_button.configure(bg="red")
            voice.say("player one wins, Congratulation, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 1 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.first_button["text"] == "0" and self.second_button["text"] == "0" and self.third_button["text"] == "0":
            self.first_button.configure(bg="red")
            self.second_button.configure(bg="red")
            self.third_button.configure(bg="red")
            voice.say("Player two wins, Congratulations, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 2 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.fourth_button["text"] == "X" and self.fifth_button["text"] == "X" and self.sixth_button["text"] == "X":
            self.fourth_button.configure(bg="green")
            self.fifth_button.configure(bg="green")
            self.sixth_button.configure(bg="green")
            voice.say("Player 1 wins, Congratulation, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 1 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.fourth_button["text"] == "0" and self.fifth_button["text"] == "0" and self.sixth_button["text"] == "0":
            self.fourth_button.configure(bg="green")
            self.fifth_button.configure(bg="green")
            self.sixth_button.configure(bg="green")
            voice.say("Player 2 wins, Congratulations, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 2 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.seventh_button["text"] == "X" and self.eighth_button["text"] == "X" and self.ninth_button["text"] == "X":
            self.seventh_button.configure(bg="blue")
            self.eighth_button.configure(bg="blue")
            self.ninth_button.configure(bg="blue")
            voice.say("Player 1 wins, Congratulation, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 1 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.seventh_button["text"] == "0" and self.eighth_button["text"] == "0" and self.ninth_button["text"] == "0":
            self.seventh_button.configure(bg="blue")
            self.eighth_button.configure(bg="blue")
            self.ninth_button.configure(bg="blue")
            voice.say("Player 2 wins, Congratulations, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 2 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.fourth_button["text"] == "X" and self.first_button["text"] == "X" and self.seventh_button[
            "text"] == "X":
            self.fourth_button.configure(bg="black")
            self.first_button.configure(bg="black")
            self.seventh_button.configure(bg="black")
            voice.say("Player 1 wins, Congratulation, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 1 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.fourth_button["text"] == "0" and self.first_button["text"] == "0" and self.seventh_button["text"] == "0":

            self.fourth_button.configure(bg="black")
            self.first_button.configure(bg="black")
            self.seventh_button.configure(bg="black")
            voice.say("Player 2 wins, Congratulations, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 2 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] ="disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.second_button["text"] == "X" and self.fifth_button["text"] == "X" and self.eighth_button["text"] == "X":
            self.second_button.configure(bg="yellow")
            self.fifth_button.configure(bg="yellow")
            self.eighth_button.configure(bg="yellow")
            voice.say("Player 1 wins, Congratulation, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 1 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.second_button["text"] == "0" and self.fifth_button["text"] == "0" and self.eighth_button["text"] == "0":

            self.second_button.configure(bg="yellow")
            self.fifth_button.configure(bg="yellow")
            self.eighth_button.configure(bg="yellow")
            voice.say("Player 2 wins, Congratulations, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 2 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] ="disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.third_button["text"] == "X" and self.sixth_button["text"] == "X" and self.ninth_button["text"] == "X":
            self.third_button.configure(bg="grey")
            self.sixth_button.configure(bg="grey")
            self.ninth_button.configure(bg="grey")
            voice.say("Player 1 wins, Congratulation, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 1 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.third_button["text"] == "0" and self.sixth_button["text"] == "0" and self.ninth_button[
                "text"] == "0":

            self.third_button.configure(bg="grey")
            self.sixth_button.configure(bg="grey")
            self.ninth_button.configure(bg="grey")
            voice.say("Player 2 wins, Congratulations, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 2 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] ="disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.first_button["text"] == "X" and self.fifth_button["text"] == "X" and self.ninth_button["text"] == "X":
            self.first_button.configure(bg="black")
            self.fifth_button.configure(bg="black")
            self.ninth_button.configure(bg="black")
            voice.say("Player 1 wins, Congratulation, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 1 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.first_button["text"] == "0" and self.fifth_button["text"] == "0" and self.ninth_button[
                "text"] == "0":

            self.first_button.configure(bg="black")
            self.fifth_button.configure(bg="black")
            self.ninth_button.configure(bg="black")
            voice.say("Player 2 wins, Congratulations, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 2 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] ="disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.third_button["text"] == "X" and self.fifth_button["text"] == "X" and self.seventh_button["text"] == "X":
            self.third_button.configure(bg="violet")
            self.fifth_button.configure(bg="violet")
            self.seventh_button.configure(bg="violet")
            voice.say("Player 1 wins, Congratulation, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 1 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"
        elif self.third_button["text"] == "0" and self.fifth_button["text"] == "0" and self.seventh_button["text"] == "0":

            self.third_button.configure(bg="violet")
            self.fifth_button.configure(bg="violet")
            self.seventh_button.configure(bg="violet")
            voice.say("Player 2 wins, Congratulations, Yeah")
            voice.runAndWait()
            msg.showinfo("Winner", "Player 2 wins, Congratulations, Yeah!")
            if True:
                self.first_button["state"] = "disabled"
                self.second_button["state"] = "disabled"
                self.third_button["state"] = "disabled"
                self.fourth_button["state"] = "disabled"
                self.fifth_button["state"] = "disabled"
                self.sixth_button["state"] = "disabled"
                self.seventh_button["state"] = "disabled"
                self.eighth_button["state"] = "disabled"
                self.ninth_button["state"] = "disabled"

    def reload_game(self):
        voice.say("Do you want to reload the game")
        voice.runAndWait()
        message=msg.askyesno("Select Choice", "Do you want to reload the game?")

        if message is True:
            if __name__ == "__main__":
                voice.say("Welcome again to the game, player 1 and player 2, let the game begins again")
                voice.runAndWait()
                self.all_widgets()

    def quit_game(self):
        message=msg.askyesno("Quit", "Do you want to end the game?")
        if message is True:
            self.root.quit()

    def all_widgets(self):
        self.first_button = tk.Button(self.first_frame, text ="",font=("Helvetica",40), width= 5, height=1, bd=2, relief="raised", fg = "grey", bg = "old lace", command= lambda : self.get_value(1))
        self.first_button.grid(row=0, column=0, padx=0, pady=0, sticky="w")
        self.second_button = tk.Button(self.first_frame,font=("Helvetica",40), width= 5, height=1,   bd=2, relief="raised", fg="grey", bg="old lace", command= lambda : self.get_value(2))
        self.second_button.grid(row=0, column=5, padx=0, pady=0, sticky="w")
        self.third_button = tk.Button(self.first_frame, font=("Helvetica",40), width= 5, height=1,  bd=2, relief="raised", fg="grey", bg="old lace", command= lambda : self.get_value(3))
        self.third_button.grid(row=0, column=8, padx=0, pady=0, sticky="w")
        self.fourth_button = tk.Button(self.first_frame, font=("Helvetica",40), width= 5, height=1,   bd=2, relief="raised", fg="grey", bg="old lace",activebackground="green",  command= lambda : self.get_value(4))
        self.fourth_button.grid(row=1, column=0, padx=0, pady=0, sticky="w")
        self.fifth_button = tk.Button(self.first_frame, font=("Helvetica",40), width= 5, height=1,   bd=2, relief="raised", fg="grey", bg="old lace", activebackground="green",  command= lambda : self.get_value(5))
        self.fifth_button.grid(row=1, column=5, padx=0, pady=0, sticky="w")
        self.sixth_button = tk.Button(self.first_frame, font=("Helvetica",40), width= 5, height=1,   bd=2, relief="raised", fg="grey", bg="old lace", activebackground="green",  command= lambda : self.get_value(6))
        self.sixth_button.grid(row=1, column=8, padx=0, pady=0, sticky="w")
        self.seventh_button = tk.Button(self.first_frame,font=("Helvetica",40), width= 5, height=1,   bd=2, relief="raised", fg="grey", bg="old lace",  command= lambda : self.get_value(7))
        self.seventh_button.grid(row=2, column=0, padx=0, pady=0, sticky="w")
        self.eighth_button = tk.Button(self.first_frame, font=("Helvetica",40), width= 5, height=1, bd=2, relief="raised", fg="grey", bg="old lace",activebackground="green",  command= lambda : self.get_value(8))
        self.eighth_button.grid(row=2, column=5, padx=0, pady=0, sticky="w")
        self.ninth_button = tk.Button(self.first_frame, font=("Helvetica",40), width= 5, height=1,  bd=2, relief="raised", fg="grey", bg="old lace",activebackground="green",  command= lambda : self.get_value(9))
        self.ninth_button.grid(row=2, column=8, padx=0, pady=0, sticky="w")
        self.tenth_button=tk.Button(self.second_frame, text="Reload", width=12, bd =2, relief="raised", fg="black", bg="old lace", command=self.reload_game)
        self.tenth_button.grid(row=0, column=0, columnspan=3, sticky="w", padx=20, pady=10)
        self.eleventh_button = tk.Button(self.second_frame, text="Quit", width=12, bd=2, relief="raised", fg="black",bg="old lace", command=self.quit_game)
        self.eleventh_button.grid(row=0, column=4, columnspan=3, sticky="w", padx=20, pady=10)
tic_toc = TicTac()
if __name__ == "__main__":
    voice.say("Welcome to the game, player 1 and player 2, let the game begin")
    voice.runAndWait()
    tic_toc.root.mainloop()
