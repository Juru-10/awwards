from django.test import TestCase

from .models import User,Profile,Project,Review
import datetime as dt

class ProfileTest(TestCase):
    """class for testing the class Profile."""
    def setUp(self):
        self.juru = Profile(prof_pic = 'Test Image',bio = 'Test',contact = 'Test')

    def test_instance(self):
        self.assertTrue(isinstance(self.juru,Profile))

    def test_save(self):
        self.juru.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) >0 )

class ProjectTest(TestCase):
    """Test class to test the class Project."""
    def setUp(self):
        self.juru = Profile(prof_pic = 'Test Image',bio = 'Test',contact = 'Test')
        self.juru.save_profile()

        self.new_project = Project(profile = self.juru, title = 'Test', image = 'Test Image', description = 'Test', link = 'Test')

    def tearDown(self):
        Profile.objects.all().delete()
        Review.objects.all().delete()
        Project.objects.all().delete()

    def test_save(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) >0 )

class ReviewTest(TestCase):
    """A class to test the Review class methods"""
    def setUp(self):
        self.juru = Profile(prof_pic = 'Test Image',bio = 'Test',contact = 'Test')
        self.juru.save_profile()

        self.project = Project(profile = self.juru, title = 'Test', image = 'Test Image', description = 'Test', link = 'Test')
        self.project.save()

        self.review = Review(profile = self.new_project, design = , usability = self.usability, content = self.content)

    def test_save(self):
        self.project.save_review()
        reviews = Project.objects.all()
        self.assertTrue(len(reviews) >0 )
