# Movie Collection Manager

A Python console application for managing a movie collection using object-oriented programming.

## Features

- **Add movies** — Add movies with title, genre, year, and rating
- **View all movies** — Display the full collection
- **Search by title** — Fast lookup using a dictionary
- **Filter by genre** — List comprehension for genre filtering
- **Statistics** — Total movies, average rating, unique genres
- **Top movies** — Movies sorted by rating (descending)
- **Multi-search** — Search multiple titles at once using `*args`
- **Reference vs Copy demo** — Demonstrates Python list behavior

## Tech Stack

- Python 3
- Object-oriented design (2 classes: `Movie`, `MovieCollection`)
- Built-in data structures: list, dict, set, tuple

## How to run

1. Clone the repository
```bash
   git clone https://github.com/yaren-atici/movie-collection-manager.git
```
2. Run the app
```bash
   python main.py
```

## Project Structure

| File | Description |
|------|-------------|
| `movie.py` | `Movie` class with attributes and `__str__` method |
| `collection.py` | `MovieCollection` class managing all operations |
| `main.py` | Entry point with interactive menu loop |
