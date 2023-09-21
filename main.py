import random
import math
import os

VOTES_TO_WIN = 5
ROAD_CHAR_LEN = 20

def get_movies():
    with open("movies.txt", "r") as f:
        lines = f.read().splitlines()
        return (
            dict(enumerate(lines)),
            {i: 0 for i in range(len(lines))}
        )


def main():
    movies, movies_votes = get_movies()
    movies_len = len(movies)
    longer_movie_len = max([len(movies[m]) for m in movies])

    os.system('clear')
    show_placar(movies, movies_votes, longer_movie_len)
    while True:
        input()
        selected = random.randint(0, movies_len - 1)
        movies_votes[selected] += 1
        show_placar(movies, movies_votes, longer_movie_len)
        if movies_votes[selected] == VOTES_TO_WIN:
            print(f'\n🏆 {movies[selected]} venceu! 🏆')
            return

def show_placar(movies, movies_votes, longer_movie_len):
    os.system('clear')
    pad = ' '
    print("PLACAR")
    print("------")
    for key in movies:
        votes = movies_votes[key]
        movie_name = movies[key]
        horse_position = int(ROAD_CHAR_LEN * votes / VOTES_TO_WIN)
        finish_line_position = math.ceil(ROAD_CHAR_LEN * (1 - votes / VOTES_TO_WIN))

        pad_horse = " " * horse_position
        pad_finish = " " * finish_line_position

        formatted_movie_name = movie_name.rjust(longer_movie_len)

        line = f"({votes}/{VOTES_TO_WIN}) {formatted_movie_name} {pad_horse}🐎{pad_finish}🏁"
        print(line)
    print("------")
    print("Aperte [ENTER] para jogar o próximo dado.")
    

main()
