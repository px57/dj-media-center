from django.test import TestCase
from profiles.tests import createBasicProfile
from django.test import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


class UploadTest(TestCase):
    """
        @description:
    """

    def test__upload(self):
        """
            @description: Test unitaire pour uploader un fichier s
        """
        dbProfile = createBasicProfile()
        c = dbProfile.httpClient

        # *** Upload ***
        file_content = b'This is a test file content.'
        uploaded_file = SimpleUploadedFile("test_file.txt", file_content)

        response = c.post(
            reverse('mediacenter__private_upload'), 
            {
                'file': uploaded_file
            }, 
            format='multipart'
        )
        self.assertEqual(response.status_code, 200)