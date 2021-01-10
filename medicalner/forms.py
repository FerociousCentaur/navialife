from django import forms
from django.core.exceptions import ValidationError

class FeedForm(forms.Form):
    CHOICES = [
        ('All','ALL'),
        ('sku_id','Sku id'),
        ('product_id','Product Id'),
        ("sku_name","Sku name"),
                ('manufacturer_name','Manufacturer name'),
                ('salt_name', 'Salt name'),
                ('drug_form', 'Drug form'),
                ('pack_size','Pack size'),
                ('strength','Strength'),

    ]
    qry = forms.CharField(required=True,  widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    choice = forms.MultipleChoiceField(choices=CHOICES, required=True)#,widget=forms.SelectMultiple())


   # def clean(self):
    #    if not (self.sku_id or self.product_id or self.sku_name or self.price or self.manufacturer_name or self.salt_name or self.pack_size or self.strength):
     #       raise ValidationError("You must specify either email or telephone")