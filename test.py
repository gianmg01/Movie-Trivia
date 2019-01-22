from __future__ import print_function

from Tkinter import *

from random import randint

from imdb import IMDb

ia = IMDb()


the_matrix = ia.get_movie('0133093')

ia.update(the_matrix, ['main'])

print(ia.get_movie_main('0133093'))



