def main():
    data_structure = {
        'full_name': 'Vraj Prajapati',
        'student_id': 10318327,
        'pizza_toppings': ['ROASTED GARLIC', 'OLIVES', 'SPINACH'],
        'movies': [
            {
                'title': 'Iron Man',
                'genre': 'sci-fi'
            },
            {
                'title': 'Hangover',
                'genre': 'comedy'
            }
        ]
    }

    data_structure['movies'].append({'title': 'Ramayana: The Epic', 'genre': 'action'})
    
    print_student_info(data_structure)
    print_pizza_toppings(data_structure)
    print()
    add_pizza_toppings(data_structure, ('PEPPERS', 'MUSHROOM'))
    print()
    print_pizza_toppings(data_structure)
    print()
    print_movie_genres(data_structure)
    print_movie_titles(data_structure['movies'])
    
def print_student_info(data):
    full_name = data['full_name']
    first_name = full_name.split()[0]
    student_id = data['student_id']
    
    print(f"My name is {full_name}, but you can call me Emperor {first_name}.")
    print(f"My student ID is {student_id}.")
    print()
    
def add_pizza_toppings(data, toppings):
    data['pizza_toppings'].extend(toppings)
    data['pizza_toppings'].sort()
    data['pizza_toppings'] = [topping.lower() for topping in data['pizza_toppings']]
    
def print_pizza_toppings(data):
    print("My favorite pizza toppings are:")
    for topping in data['pizza_toppings']:
      print(f"- {topping}")
     

def print_movie_genres(data):
        genres = [movie['genre'] for movie in data['movies']]
        print("I like to watch", end=" ")
        for i, genre in enumerate(genres):
            if i == len(genres) - 1:
                print(f"and {genre}", end=" ")
            else:
                print(f"{genre},", end=" ")
        print("movies.")
    

def print_movie_titles(movie_list):
        titles = [movie['title'].title() for movie in movie_list]
        print("Some of my favorite movies are", end=" ")
        for i, title in enumerate(titles):
            if i == len(titles) - 1:
                print(f"and {title}!")
            else:
                print(f"{title},", end=" ")
    

if __name__ == "__main__":
    main()

