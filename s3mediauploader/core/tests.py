from django.test import TestCase
from .models import randomizer, Document
from .views import upload
from .forms import DocumentForm
from django.urls import resolve
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse
from django.core.files import File
from django.utils.six import BytesIO

from PIL import Image
from io import StringIO


def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
   """
   Generate a test image, returning the filename that it was saved as.

   If storage is None, the BytesIO containing the image data
   will be passed instead.
   """
   data = BytesIO()
   Image.new(image_mode, size).save(data, image_format)
   data.seek(0)
   if not storage:
       return data
   image_file = ContentFile(data.read())
   return storage.save(filename, image_file)

class models_test(TestCase):

    """
    Testing the randomizer function

    """

    def test_randomizer(self):
        filename = 'abcd'
        returned_filename = randomizer(self, filename)
        self.assertNotEqual(filename, returned_filename)

class views_test(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, upload)

class UploadImageTests(TestCase):
   def setUp(self):
       super(UploadImageTests, self).setUp()


   def test_valid_form(self):
       '''
       valid post data should redirect
       The expected behavior is to show the image
       '''
       url = reverse('home')
       avatar = create_image(None, 'avatar.png')
       avatar_file = SimpleUploadedFile('front.png', avatar.getvalue())
       data = {'upload': avatar_file}
       response = self.client.post(url, data, follow=True)

       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed('core/document_form.html')
