# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {"name": name,
                "director": director,
                "year": year,
                "runtime": runtime}
    database.append(movie)

def find_movies(database: list, search_term: str):
    new_list = []
    for i in database:
        if search_term in i['name'].casefold():
            # print(i['name'])
            new_list.append(i)
    return new_list




if __name__ == '__main__':
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "Python")
    print(my_movies)