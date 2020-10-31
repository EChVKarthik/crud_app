from django.test import TestCase
from app.models import Name

# Create your tests here.

class Testing(TestCase):

    def setUp(self):
        Name.objects.create(id=2, name="sairakesh")

    def test_delete(self):
        tmp = Name.objects.count()
        obj = Name.objects.get(id=2)
        obj.delete()
        upTmp = Name.objects.count()
        print(tmp, upTmp)
        self.assertEqual(tmp-1, upTmp)
        print("\n User deleted")

    def test_retrive(self):
        obj = Name.objects.get(id=2)
        self.assertEqual(obj.name, "sairakesh")
        print("\n User exist")
    
    def test_upate(self):
        obj = Name.objects.get(id=2)
        obj.name = "shanmukha"
        obj.save()
        upObj = Name.objects.get(id=2)
        self.assertEqual(upObj.name, "shanmukha")
        print("\n Successfully Updated")
    
    
    
    