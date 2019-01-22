from __future__ import print_function

from ttk import *

score = 0

master = setup_master()
master.geometry("460x300")

l1 = Label(master, text="Hello").place(x=200, y=45)
e1 = Entry(master).place(x=170, y=190)

master.mainloop()
