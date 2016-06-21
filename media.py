# Lesson 3 : Make classes 
# Mini project : Movies website
# In this file, you will define the class movie.
# Importing this file into entertainment_center.py


import webbrowser
class Movie():
    ''' This classs provides a way to store movie related information'''

    VALID_RATINGS = ['PG-13', 'R', 'sci-fic']

    def __init__(self, movieTitle, movieStoryLine, posterImage, trailerYoutube, rating):
        """[Docstring about the init, typically what the input arguments do]"""
        self.title = movieTitle
        self.storyline = movieStoryLine
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYoutube
        self.rating = rating

    def show_trailer(self):
        """ Displays the trailer of the movie """
        webbrowser.open(self.trailer_youtube_url)

# initialize instance of class Movie
