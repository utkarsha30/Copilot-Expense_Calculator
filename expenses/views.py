from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import ExpenseSerializer
from .models import Expense

class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

def index(request):
    return render(request, "index.html")