# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 07:50:25 2025

@author: juleigar
"""
movie_lists = []
favourite_movies ={1: 'Dumb and Dumber',
                   2: 'Alice in Wonderland',
                   3: 'Pooh Bear',
                   4: 'Hannibal',
                   5: 'Shawshank'
                   }

for index, movie in enumerate(favourite_movies):
    movie_list = "Movie " + str(movie) + " :" +favourite_movies[movie]
    movie_lists.append(movie_list)
print((movie_lists))
    