from django.contrib import admin
from .models import Expense
@admin.register(Expense)

class ExpenseAdmin(admin.ModelAdmin):
    """
    these are the Expense model fields
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    """
    list_display = ('name', 'amount', 'timestamp', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'timestamp')
    ordering = ('-timestamp',)

    def category(self, obj):
        return obj.category.name if obj.category else 'No Category'

  
