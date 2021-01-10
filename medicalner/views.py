from django.shortcuts import render,HttpResponse
from .forms import FeedForm
from . models import medicine
# Create your views here.

def someFunc(request):
    p=0
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['qry']:
                qry = form.cleaned_data['qry']
                if 'All' in form.cleaned_data['choice']:
                    print('alll')

                    d1 = medicine.objects.filter(sku_id__icontains=qry)
                    d2 = medicine.objects.filter(product_id__icontains=qry)
                    d3 = medicine.objects.filter(sku_name__icontains=qry)
                    #d4 = medicine.objects.filter(price=qry)
                    d5 = medicine.objects.filter(manufacturer_name__icontains=qry)
                    d6 = medicine.objects.filter(salt_name__icontains=qry)
                    d7 = medicine.objects.filter(drug_form__icontains=qry)
                    d8 = medicine.objects.filter(strength__icontains=qry)
                    d1 = d1.union(d2,d3,d5,d6,d7,d8,all=False)

                    if not d1:
                        return render(request, 'home.html', {'pform':FeedForm, 'error': 'NO RESULTS FOUND'})
                    return render(request, 'home.html', {'pform':FeedForm, 'data': d1})
                elif form.cleaned_data['choice']:
                    print(form.cleaned_data['choice'])
                    if 'sku_id' in form.cleaned_data['choice']:
                        d1 = medicine.objects.filter(sku_id__icontains=qry)
                        #return render(request,'results.html',{'data':d1})
                    if 'product_id' in form.cleaned_data['choice'] :
                        d2 = medicine.objects.filter(product_id__icontains=qry)
                        if 'd1' in locals():
                            d1 = d1.union(d2,all=False)
                        else:
                            d1 =d2
                        #return render(request, 'results.html', {'data': d1})
                    if "sku_name" in form.cleaned_data['choice']:
                        d2 = medicine.objects.filter(sku_name__icontains=qry)
                        if 'd1' in locals():
                            d1 = d1.union(d2,all=False)
                        else:
                            d1 = d2
                        #return render(request, 'results.html', {'data': d1})
                    if 'manufacturer_name' in form.cleaned_data['choice']:
                        d2 = medicine.objects.filter(manufacturer_name__icontains=qry)
                        if 'd1' in locals():
                            d1 = d1.union(d2,all=False)
                        else:
                            d1 =d2
                        #return render(request, 'results.html', {'data': d1})
                    if 'salt_name' in form.cleaned_data['choice'] :
                        d2 = medicine.objects.filter(salt_name__icontains=qry)
                        if 'd1' in locals():
                            d1 = d1.union(d2,all=False)
                        else:
                            d1 =d2
                        #return render(request, 'results.html', {'data': d1})
                    if 'drug_form' in form.cleaned_data['choice'] :
                        d2 = medicine.objects.filter(drug_form__icontains=qry)
                        if 'd1' in locals():
                            d1 = d1.union(d2,all=False)
                        else:
                            d1 =d2
                        #return render(request, 'results.html', {'data': d1})
                    elif 'strength' in form.cleaned_data['choice'] :
                        d2 = medicine.objects.filter(strength__icontains=qry)
                        if 'd1' in locals():
                            d1 = d1.union(d2,all=False)
                        else:
                            d1 =d2
                        #return render(request, 'results.html', {'data': d1})
                    if not 'd1' in locals():
                        return render(request, 'home.html', {'pform':FeedForm, 'error': "No results"})
                    return render(request, 'home.html', {'pform':FeedForm, 'data': d1})
                #, , ,'price', , ,,'pack_size' , ,'product_banned'  ,'unit','price_per_unit'



            return render(request, 'home.html', {'pform':FeedForm, 'error': "Invalid-----at least one of the fields should be filled "})


    return render(request,'home.html',{"pform":FeedForm})
