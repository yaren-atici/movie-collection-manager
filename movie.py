class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}, Rating: {self.rating}"