from django.test import TestCase
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from snippets.models import Snippet
from rest_framework.test import APIRequestFactory
from snippets import views

class ViewsTestCase(TestCase):
    
    def setUp(self):
        # Create a test instance
        # Create auth user for views using api request factory
        self.username = 'config_tester'
        self.password = 'goldenstandard'
        self.owner = User.objects.create_superuser(self.username, 'test@example.com', self.password)
        self = Snippet.objects.create(
            title='Python snippet', code='Snippet.objects.all()', owner=self.owner)
        # Using the standard RequestFactory API to create a form POST request
        factory = APIRequestFactory()
        factory.post('/snippets/', {'title': 'python snippet', 'code': 'Snippet.objects.all()', 'owner': self.owner})
        factory.post('/snippets/', {'title': 'java snippet', 'code': 'System.out.println()', 'owner': self.owner})

    def tearDown(self):
        pass
 
    @classmethod
    def setup_class(cls):
        """setup_class() before any methods in this class"""
        pass

    @classmethod
    def teardown_class(cls):
        """teardown_class() after any methods in this class"""
        pass

    def shortDescription(self):
        return None


    def test_view_set1(self):
        """
        No auth example
        """
        print("test_list_Snippet")
        factory = APIRequestFactory()
        view = views.SnippetViewSet.as_view({'get':'list'})
        request = factory.get('') 
        response = view(request)        
        self.assertEqual(response.status_code, 200)

    def test_view_set2(self):
        """
        Auth using force_authenticate
        """
        print("test_list_Snippet with force_authenticate")
        factory = APIRequestFactory()
        user = User.objects.get(username=self.username)
        detail_view = views.SnippetViewSet.as_view({'get': 'list'})

        # Make an authenticated request to the view...
        api_request = factory.get('')
        force_authenticate(api_request, user=user)
        response = detail_view(api_request)
        self.assertEqual(response.status_code, 200)
        
    def test_get_Snippet(self):             
        
        snippet = Snippet.objects.create(title="Python snippet", owner=self.owner)        
        factory = APIRequestFactory()
        view = views.SnippetViewSet.as_view({'get':'retrieve'})
        request = factory.get('')
        print("test_get_Snippet, self.id = " + str(snippet.pk))
        response = view(request, pk=snippet.pk)        
        self.assertEqual(response.status_code, 200)
    
    def test_delete_Snippet(self):             
        
        snippet = Snippet.objects.create(title="Python snippet", owner=self.owner)        
        factory = APIRequestFactory()
        view = views.SnippetViewSet.as_view({'get':'destroy'})
        request = factory.get('')
        print("test_delete_Snippet, self.id = " + str(snippet.pk))
        response = view(request, pk=snippet.pk)        
        self.assertEqual(response.status_code, 204)
        
    def test_create_Snippet(self):             
        print("test_create_Snippet")
        factory = APIRequestFactory()
        request = factory.post('/snippets/', {'title': 'PythonSnippet', 'code': 'SomePythonCode'}, format='json')  
        response = views.SnippetViewSet.as_view(request);
    
    def test_update_put_Snippet(self):
 
        snippet = Snippet.objects.create(title="Python snippet", owner=self.owner)        
        factory = APIRequestFactory()
        print("test_update_put_Snippet, self.id = " + str(snippet.pk))
        url = "/snippets/" + str(snippet.pk) + "/"
        print("test_update_put_Snippet url = " + str(url))   
        request = factory.put(url, {'title': 'PythonSnippetUpdated'}, format='json')
        
    def test_update_patch_Snippet(self):
 
        snippet = Snippet.objects.create(title="Python snippet", owner=self.owner)        
        factory = APIRequestFactory()
        print("test_update_patch_Snippet, self.id = " + str(snippet.pk))
        url = "/snippets/" + str(snippet.pk) + "/"
        print("test_update_patch_Snippet url = " + str(url))   
        request = factory.patch(url, {'title': 'PythonSnippetUpdated'}, format='json')           