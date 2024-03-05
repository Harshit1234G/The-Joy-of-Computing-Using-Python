import random

movie_names = [
    "Harry Potter and the Sorcerer's Stone",
    "Avengers Endgame",
    "The Lord of the Rings",
    "Toy Story",
    "Jurassic Park",
    "Star Wars",
    "The Lion King",
    "Titanic",
    "Insidious",
    "The Matrix",
    "Avatar",
    "Frozen",
    "Spider Man Into the Spider Verse",
    "Wonder Woman",
    "The Avengers",
    "Toy Story 3",
    "Guardians of the Galaxy",
    "Mad Max Fury Road",
    "Interstellar",
    "The Godfather",
    "The Terminator",
    "Beauty and the Beast",
    "Black Panther",
    "The Jurassic World",
    "Jaws",
    "The Fast and the Furious",
    "The Star Wars The Force Awakens",
    "Iron Man",
    "The Spider Man",
    "The Shrek",
    "Pirates of the Caribbean and the curse of black pearl",
    "Harry Potter and the Chamber of Secrets",
    "Guardians of the Galaxy Vol. 2",
    "Avengers Infinity War",
    "Pirates of the Caribbean on stranger tides",
    "Alice in Wonderland",
    "The Dark Knight Rises",
    "Finding Dory"
]
movie_names = [i.lower() for i in movie_names]

movie = random.choice(movie_names)


