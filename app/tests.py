from django.test import TestCase
from .models import Vendor

# Create your tests here.
class TestVendor(TestCase):
    def setUp(self):
        self.new_vendor  = Vendor(name='Ian', email='moringa@gmail.com',contact='07123456', location='Athi-river', product_type='clothes')

    def tearDown(self):
        Vendor.objects.all.delete()

    def testInstance(self):
        self.assertTrue(isinstance(self.new_vendor, Vendor))

    def testSaving(self):
        vendors = Vendor.objects.all()
        self.new_vendor.saveVendor()
        self.assertTrue(len(vendors)>0)