class Movie:
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # give the following instance variables an initial value as a placeholder
        self.director = 'N/A'
        self.year = 'N/A'
        self.rating = 'N/A'
        self.cast = []

    def add_director(self, director):
        self.director = director

    # the parameter year will be an integer
    def add_year(self, year):
        self.year = year

    def add_rating(self, rating):
        if rating in Movie.VALID_RATINGS:
            self.rating = rating

    # the parameter cast will be a list
    def add_cast(self, cast):
        for actor in cast:
            self.cast.append(actor)
