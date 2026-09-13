from django.test import TestCase

from .models import Publisher, Book, Review

from django.urls import reverse

# Create your tests here.
class BookPageTests(TestCase):
    def test_book_page_shows_books(self):
        # Arrange - put a book in the database
        publisher = Publisher.objects.create(name="Public House")
        book = Book.objects.create(publisher=publisher, title="Gone With the Wind", price=19.99)
        # Act - request the book page
        response = self.client.get(reverse("book_list"))
        # Assert - claim that the book's title is in the response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gone With the Wind")
