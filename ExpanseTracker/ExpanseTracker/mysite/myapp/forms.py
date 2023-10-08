from django.forms import ModelForm
from .models import Expense
class ExpenseFrom(ModelForm):
    class Meta:
        model=Expense
        fields=('name','amount','category')
