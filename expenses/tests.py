# imports for django_rest_framework tests
from rest_framework.test import APITestCase

from .models import Expense
"""
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    #category choice field
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('other', 'Other'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return f"{self.name} - {self.amount}"

"""

class ExpenseTestCase(APITestCase):

    def setUp(self):
       #create 3 expenses
       Expense.objects.bulk_create([
            Expense(name='Lunch', amount=15.50, category='food'),
            Expense(name='Bus Ticket', amount=2.75, category='transport'),
            Expense(name='Movie Ticket', amount=12.00, category='entertainment')
       ])
    def test_expense_list(self):
        """
        Test the expense list endpoint
        """
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
    
    def test_expenses_detail(self):
        """
        Test the expense detail endpoint
        """
        expense = Expense.objects.first()
        response = self.client.get(f'/api/expenses/{expense.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], expense.name)
        self.assertEqual(response.data['amount'], str(expense.amount))
        self.assertEqual(response.data['category'], expense.category)
    
    def test_expense_create(self):
        """
        Test the expense create endpoint
        """
        data = {
            'name': 'Coffee',
            'amount': 3.50,
            'category': 'food'
        }
        response = self.client.post('/api/expenses/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Expense.objects.count(), 4)
        self.assertEqual(Expense.objects.last().name, 'Coffee')

    def test_expenses_update(self):
        """
        Test the expense update endpoint
        """
        expense = Expense.objects.first()
        data = {
            'name': 'Updated Lunch',
            'amount': 20.00,
            'category': 'food'
        }
        response = self.client.put(f'/api/expenses/{expense.id}/', data, format='json')
        self.assertEqual(response.status_code, 200)
        expense.refresh_from_db()
        self.assertEqual(expense.name, 'Updated Lunch')
        self.assertEqual(expense.amount, 20.00)

    def test_expenses_delete(self):
        """
        Test the expense delete endpoint
        """
        expense = Expense.objects.first()
        response = self.client.delete(f'/api/expenses/{expense.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Expense.objects.count(), 2)  

    def tearDown(self):
        #delete all expenses
        Expense.objects.all().delete()