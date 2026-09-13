#REFLECTION

##Test Failure Output:

Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_book_page_shows_books (catalog.tests.BookPageTests.test_book_page_shows_books)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\yoda1\Desktop\cidm3312\book-catalog\catalog\tests.py", line 17, in test_book_page_shows_books
    self.assertContains(response, "Gone With the Wind")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: False is not true : Couldn't find 'Gone With the Wind' in the following response
b'<html>\n<head>\n    <title>Book Catalog</title>\n</head>\n<body>\n    <nav>\n        <a href="/">Books</a> |\n  <a href="/publishers/">Publishers</a> |\n        <a href="/reviews/">Reviews</a>\n    </nav>\n\n    \n    <h1>Books</h1>\n    <p>You have 0 books to choose from.</p>\n\n    <ul>\n    \n    </ul>\n\n  \n\n</body>\n</html>'

----------------------------------------------------------------------
Ran 1 test in 0.036s

FAILED (failures=1)
Destroying test database for alias 'default'...

##What the failure told me:
This test created a test database that added the book "Gone With The Wind" and then searched the Books for this title, however it did not populate on the Books page so the test failed.

#Questions

##Question 1. 
Your models use two foreign keys. Pick one of them. Name which model carries the ForeignKey and which model it points at, and explain why you arranged it that way. What would be different about the data you entered if you had reversed it?

##Answer:
The field publisher is a foreign key in the Book model and points at the Publisher model. I arranged it this way so that a publisher can have many books, but a book can only belong to one publisher. If the foreign key belonged to the Publisher model and pointed at the Book model, then a book could belong to many publishers, but a publisher could only have one book. This would not make sense in a real world scenario.

##Question 2. 
You added one field of your own to Book. Which field type did you choose, and why that type rather than another? What would you lose if you had stored the same fact as a CharField?

##Answer:
I chose to add the price field to Book as a decimal. I chose this field type because it would allow me to specify how many digits the number should have and how many decimal places should be icluded to model how we typically see prices written. If I had used a CharField instead, this field could still display the same way, but it would cause problems later if we needed to do something like calculate the price of two books. The CharField would not allow us to use arithmetic, so adding different features to our program would be more difficult and require unecessary complexities like casting.
