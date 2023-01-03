
class Book:

    def __init__(self, book_dict):
        self.id = book_dict['id']
        self.name = book_dict['name']
        self.author = book_dict['author']
        self.user_rating = book_dict['user_rating']
        self.number_of_reviews = book_dict['number_of_reviews']
        self.price = book_dict['price']
        self.year = book_dict['year']
        self.genre = book_dict['genre']