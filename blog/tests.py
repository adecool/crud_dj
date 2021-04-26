from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from . models import Post
# Create your tests here.
class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'secret'
        )
        self.post = Post.objects.create(
            title='A good title',
            body='Nice body',
            author = self.user
        )
    def test_string_representation(self):
        post = Post(title='a simple title')
        self.assertEqual(str(post), post.title)   

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')    
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'home.html')
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

# additional test
class HomePageTests(TestCase):
        
    def test_home_contains_hello_message(self):
        response = self.client.get(reverse('home'))
        self.assertIn(b'You are not Logged in', response.content)
         
    def test_home_using_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    
    def test_home_has_title(self): 
        response = self.client.get(reverse('home'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class ModelTests(TestCase):

    def get_UserProfile(self, name):
        
        from . models import UserProfile
        try:                  
            cat = UserProfile.objects.get(username=user.username)
        except Category.DoesNotExist:    
            cat = None
        return cat    


                 
def LogInTest(TestCase):
    def setUp(self):
        self.credentials = {'username': 'testuser', 'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        response = self.client.post('/login/', **self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)    