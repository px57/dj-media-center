from django.test import TestCase
from profiles.tests import createBasicProfile
from django.test import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from mediacenter.libs import external_set_file
from mediacenter.tests_cache.interface_list import *

import json
import os

from kernel.http.response import ResponseTest


def get_listdir_file_test(type):
    """
        @description: Get the listdir of the file.
    """
    type_list = ['audio', 'doc', 'img', 'other', 'pdf', 'video']
    if type not in type_list:
        raise Exception('Type not found ' + type)
    base_path = 'mediacenter/upload/test_cache/' + type
    listdir = os.listdir(base_path)
    new_listdir = []
    for dir in listdir:
        new_listdir.append(os.path.join(base_path, dir))
    return new_listdir

def upload_test(dbProfile=None, filesrc='test_file.txt'):
    """
        @description:
    """
    if dbProfile is None:
        dbProfile = createBasicProfile()
    c = dbProfile.httpClient

    # *** Upload ***
    # file_content = b'This is a test file content.'
    file_content = open(filesrc, 'rb').read()
    uploaded_file = SimpleUploadedFile(
        filesrc, 
        file_content, 
    )

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

        listdir = get_listdir_file_test('img')
        for dir in listdir:
            content = upload_test(None, dir)


class SetExternalFileToSystem(TestCase):
    """ 
        @description: Test the external send file. 
    """

    def test_send_file(self):
        """
            @description: 
        """
        dbFile = external_set_file(
            'default',
            'test_file.txt',
        )
        print ('################################3>>>')
        print (dbFile)
