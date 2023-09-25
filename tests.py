from django.test import TestCase
from profiles.tests import createBasicProfile
from django.test import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import json

from kernel.http.response import ResponseTest


def upload_test(dbProfile=None):
    """
        @description:
    """
    if dbProfile is None:
        dbProfile = createBasicProfile()
    c = dbProfile.httpClient

    # *** Upload ***
    file_content = b'This is a test file content.'
    uploaded_file = SimpleUploadedFile("test_file.txt", file_content)

    response = c.post(
        reverse('mediacenter__private_upload'), 
        {
            'file': uploaded_file,
            'label': 'default'
        }, 
        format='multipart'
    )
    return json.loads(response.content.decode('utf-8'))

class UploadTest(ResponseTest):
    """
        @description:
    """

    def test__upload(self):
        """
            @description: Test unitaire pour uploader un fichier s
        """
        content = self.assertSuccess(upload_test())
        self.assertEqual('file' in content, True)
        self.assertEqual('src' in content['file'], True)

    def test_upload_and_download(self):
        """
            @description: Upload and test download.
        """
        content = upload_test()
        c = Client()
        response = c.get(content['file']['src'])
        self.assertEqual(response.status_code, 200)

    def test_upload_picture(self):
        """
            @description: Test upload picture.
        """
        content = upload_test()