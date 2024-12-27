class Library:

    def __init__(self, _no_of_books, _books):
        self.books = _books
        self.no_of_books = _no_of_books

    def print_books(self):
        for book in self.books:
            print(book)

    def get_book(self, _book):
        book_found = False
        for book in self.books:
            if(book == _book) :
                book_found = True
                break
        if book_found:
            print(f"{_book} is present")

        else : 
            print("No book found!")
        
    
    def num_books(self):
        print(self.no_of_books)

books = ["Atomic Habits", "Never Finished", "48 Rules of Power", "Psychology of Money"]
success_library = Library(4, books)

success_library.print_books()
success_library.get_book("Atomic Habits")

            
        

                