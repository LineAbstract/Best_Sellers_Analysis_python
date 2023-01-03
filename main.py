# imports
from data import data_list
from class_book import Book


# main analysis function:
def run_analysis(books_list):
    books = creation_of_book_list(books_list)
    book_most_appeared(books)
    genre_most_appeared(books)
    author_with_most_distinct(books)
    top_book_per_year(books)
    
# functions:
# instantiate a book object for each dictionary within the data list and add the book instantiation to a book list variable
def creation_of_book_list(data_list):
    books_list = []
    for dictionary in data_list:
        new_book = Book(dictionary)
        books_list.append(new_book)
    return books_list


# q1: 
# which book appeared in the top 50s list for the most years and for how many years? print results to terminal
def book_most_appeared(books):
    print('')
    print('\033[4m'"This evaluation determines which book has had the most successful number of years in the top 50s book list:"'\033[0m')
    
    current_top_book = {'name': '', 'count': 0}
    # save list of book names
    book_names = [book.name for book in books]
    # loop through book names and count how many times they appeared, replace top if higher len() reached
    for distinct_book_name in book_names:
        list_of_specific_book = [book_name for book_name in book_names if book_name == distinct_book_name]
        if current_top_book['count'] < len(list_of_specific_book):
            current_top_book['name'] = distinct_book_name
            current_top_book['count'] = len(list_of_specific_book)
    
    print(f"\033[3m{current_top_book['name']}\033[0m appeared the most times in the top 50s book list for {current_top_book['count']} total years. ")
    print('')
    pass

# q2: 
# which genre (fiction/non-fiction) has appeared the most in the top 50s list? print results to terminal
def genre_most_appeared(books):
    print('')
    print('\033[4m'"This evaluation determines which genre (fiction or non-fiction) has appeared the most in the top 50s book list:"'\033[0m')
    
    # find len of each filtered list of genres (fiction/non-fiction)
    number_of_fiction = len(list(filter(lambda book: book.genre == 'Fiction', books)))
    number_of_nonfiction = len(list(filter(lambda book: book.genre == 'Non Fiction', books)))
    
    # set print statements
    if number_of_fiction > number_of_nonfiction:
        print('It has been determined that there are more fiction books than non-fiction books in the top 50s book list.')
        print(f'No. of fiction books: {number_of_fiction}')
        print(f'No. of non-fiction books: {number_of_nonfiction}')
    elif number_of_nonfiction > number_of_fiction:
        print('It has been determined that there are more non-fiction books than fiction books in the top 50s book list.')
        print(f'No. of fiction books: {number_of_fiction}')
        print(f'No. of non-fiction books: {number_of_nonfiction}')
    else:
        print('There are equal numbers of fiction and non-fiction books in the top 50s book list.')
        print(f'No. of fiction books: {number_of_fiction}')
        print(f'No. of non-fiction books: {number_of_nonfiction}')
    
    print('')
    pass

# q3:
# which author has shown up on the top 50s list the most with distinct books? 
def author_with_most_distinct(books):
    
    pass

# q4:
# display the top book for each year based on the book's user rating & number of reviews
def top_book_per_year(books):
    
    pass

run_analysis(data_list)