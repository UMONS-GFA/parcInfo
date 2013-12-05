__author__ = 'Christophe Bastin'

from django.test import TestCase
from django.test import Client


class ParcInfoTestCase(TestCase):
    fixtures = ['fixtures']

    def setUp(self):
        self.client = Client()

    def testAdmin(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/admin', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/index.html')

    def testAdminAnonymous(self):
        response = self.client.post('/admin', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/login.html')

    def testAdminNotAuthorized(self):
        self.client.login(username='test', password='test')
        response = self.client.post('/admin', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/login.html')

    def testAdminParcInfo(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/admin/parcInfo', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/app_index.html')