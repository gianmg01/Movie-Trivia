from __future__ import print_function

from Tkinter import *

from random import randint

from imdb import IMDb

ia = IMDb()

score = 0
q = 0
k = 1
b = 0
movie_directories = ["0133093", "0068646", "0111161", "0108052", "0034583", "0033467", "0032138", "0109830", "0062622",
                     "0083866", "0167260", "0120338", "0120815", "0082971", "0075148", "0056592", "0073195", "0060196",
                     "0112573", "0107290", "0020629", "0110912", "0088763", "0361748", "0167261", "1010048", "0086190",
                     "0120737", "1136608", "0381061", "0190332", "0499549", "0325980", "0266697", "0452623", "0443453",
                     "0425061", "2911666", "0104257", "0088247", "4154756", "1014759", "0095016", "5104604", "0405159",
                     "0088847", "0071562", "0120382", "1517451", "0317705"]
questions = ['director', 'year']
this_question = ""
movies_used = {""}
current_movie = ""

master = Tk()
master.geometry("460x300")

v = StringVar()
l1 = Label(master, textvariable=v, anchor=CENTER)
l1.pack(padx=50, pady=25)
m = StringVar()
l2 = Label(master, textvariable=m, anchor=CENTER)
e1 = Entry(master)
e1.pack(padx=50, pady=75)
e1.focus_set()


def enter(_):
    global q, k, movie_directories, questions, this_question, movies_used, current_movie, b, score

    if b == 0:

        guess = str(e1.get())
        if this_question == "director":
            answer = str((ia.get_movie(current_movie)['director'])[0])
        elif this_question == "year":
            answer = str((ia.get_movie(current_movie)['year']))
        else:
            print("error 1")
            answer = "null"

        e1.delete(0, END)
        e1.insert(0, "")

        if guess.lower() == answer.lower():
            m.set("You are Correct!")
            score += 1
        else:
            m.set("Incorrect!\nThe correct answer was: " + str(answer) + "\nYour guess was: " + str(guess))

        if q < 20:
            b = 1
            new_question()
        else:
            b = 2

        l1.pack_forget()
        e1.pack_forget()
        l2.pack(padx=50, pady=75)

    elif b == 1:
        l2.pack_forget()
        l1.pack(padx=50, pady=25)
        e1.pack(padx=50, pady=75)
        b = 0
    elif b == 2:
        l2.pack_forget()
        l1.pack(padx=50, pady=25)
        v.set(("Finished\nyou scored " + str(score) + "/20\nwould you like to play again?"))
        b = 3
    elif b == 3:

        score = 0
        q = 0
        k = 1
        b = 0
        this_question = ""
        movies_used = {""}
        current_movie = ""
        l2.pack_forget()
        l1.pack(padx=50, pady=25)
        e1.pack(padx=50, pady=75)
        new_question()


def new_question():
    global q, k, movie_directories, questions, this_question, movies_used, current_movie

    while k == 1:
        current_movie = movie_directories[randint(0, 49)]
        reroll()
    k = 1
    this_question = questions[randint(0, 1)]
    if this_question == "director":
        v.set(("question " + str(q + 1) + "/20\n\nwho is the director of\n" + str(ia.get_movie(current_movie)) + "?"))
    elif this_question == "year":
        v.set(("question " + str(q + 1) + "/20\n\nwhat year was\n" + str(ia.get_movie(current_movie)) + " made?"))
    q += 1


def reroll():
    global q, k, movie_directories, questions, this_question, movies_used, current_movie

    if str(current_movie) not in str(movies_used):
        k = 0
        movies_used.add(current_movie)
    else:
        k = 1


new_question()

master.bind('<Return>', enter)

master.mainloop()



