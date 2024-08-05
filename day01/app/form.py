from django import forms
from .models import category,unit,item,supplier,Order,Employee

class categoryForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
          model = category
          fields = '__all__'
    
class TestForm(forms.Form):
    name = forms.CharField()    

class unitForm(forms.Form):
     name = forms.CharField()    
     class Meta:
          model = unit
          fields = '__all__'


class itemForm(forms.ModelForm):
    class Meta:
        model = item 
        fields ='__all__'

class supplierForm(forms.ModelForm):
    class Meta:
        model = supplier
        fields ='__all__'

class orderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields ='__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee        
        fields ='__all__'
        