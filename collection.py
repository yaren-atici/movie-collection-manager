from movie import Movie

class MovieCollection:
    def __init__(self):
        self.movies = []
        self.genres = set()
        self.movie_dict = {}

    def add_movie(self, **kwargs):
        movie = Movie(**kwargs)
        self.movies.append(movie)
        self.genres.add(movie.genre)
        self.movie_dict[movie.title] = movie

    def view_movies(self):
        for movie in self.movies:
            print(movie)

    def search_by_title(self, title):
        return self.movie_dict.get(title, "Movie not found.")

    def filter_by_genre(self, genre):
        return [m for m in self.movies if m.genre.lower() == genre.lower()]

    def search_multiple_titles(self, *titles):
        return [self.movie_dict[t] for t in titles if t in self.movie_dict]

    def get_statistics(self):
        total = len(self.movies)
        if total == 0:
            return "No data."

        avg_rating = sum(m.rating for m in self.movies) / total
        return {
            "total_movies": total,
            "average_rating": round(avg_rating, 2),
            "genres": tuple(self.genres)
        }

    def top_movies(self, n=3):
        return sorted(self.movies, key=lambda m: m.rating, reverse=True)[:n]

    def reference_vs_copy_demo(self):
        ref_list = self.movies
        copy_list = self.movies.copy()

        if self.movies:
            ref_list[0].title = "CHANGED (Reference)"

        print("\nReference affects original:")
        for m in self.movies:
            print(m)

        print("\nCopy list:")
        for m in copy_list:
            print(m)