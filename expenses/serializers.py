from rest_framework import serializers
from expenses.models import Expense  
class ExpenseSerializer(serializers.ModelSerializer):
    """
    exposes Expense model fields"""
    class Meta:
        model = Expense 
        fields = ['id', 'name', 'amount', 'timestamp', 'category']

   

    
    