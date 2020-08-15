from django.test import TestCase

# Create your tests here.
# todos/tests.py
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='a body here')
        # Will certainly fail for this test case
        Todo.objects.create(title='wrong object', body=1213)

    def test_title_content(self):
        # todo = Todo.objects.get(id=2)
        # expected_object_name = f'{todo.title}'
        # self.assertEquals(expected_object_name, 'wrong object')
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_body_content(self):
        # todo = Todo.objects.get(id=2)
        # expected_object_name = f'{todo.body}'
        # self.assertEquals(expected_object_name, 1213)
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'a body here')
