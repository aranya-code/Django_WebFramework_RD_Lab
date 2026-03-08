import datetime
from django.test import TestCase, Client
from django.urls import reverse
from movieList.models import movie
from movieList.forms import movieCreation

class TestMovieModel(TestCase):
    def test_movie_creation(self):
        # Test that the model successfully creates and stores records
        new_movie = movie.objects.create(
            name="Inception",
            releaseDate=datetime.date(2010, 7, 16),
            rating=9
        )
        self.assertEqual(new_movie.name, "Inception")
        self.assertEqual(movie.objects.count(), 1)


class TestMovieForm(TestCase):
    def test_valid_form(self):
        # Test that valid data passes form validation
        form = movieCreation(data={
            'name': 'The Matrix',
            'releaseDate': '1999-03-31',
            'rating': 10
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_data(self):
        # Test that empty data fails validation for all required fields
        form = movieCreation(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a sample movie to ensure the list view has data
        self.test_movie = movie.objects.create(
            name="Avatar",
            releaseDate="2009-12-18",
            rating=8
        )

    def test_list_view(self):
        # Test that the home page loads the list and context correctly
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movieList/index.html')
        self.assertIn(self.test_movie, response.context['all_movies'])

    def test_add_movies_view_get(self):
        # Test that a GET request loads the blank form
        response = self.client.get(reverse('addMovies'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movieList/addmovie.html')
        self.assertIsInstance(response.context['movie_add'], movieCreation)

    def test_add_movies_view_post_valid(self):
        initial_count = movie.objects.count()

        # Submit valid POST data
        response = self.client.post(reverse('addMovies'), data={
            'name': 'Interstellar',
            'releaseDate': '2014-11-07',
            'rating': 9
        })

        # Check that the movie was saved to the database
        self.assertEqual(movie.objects.count(), initial_count + 1)

        # Check that the view redirects the user to the list page
        self.assertRedirects(response, reverse('list'))