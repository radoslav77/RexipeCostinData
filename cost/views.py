from django.shortcuts import render, redirect
import csv
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
from csv import DictReader
import sys
import pprint
import os
from django.conf import settings

from .models import Exeldocument, Import_Data, Recipe
from django.views.generic.edit import FormView
from .forms import FileFieldForm, RecipeForm

# Create your views here.


dir_name = "/media/"


def index(request):

    files = Exeldocument.objects.filter(title='ritter')
    csv_files = []
    field_names = []
    dic_data = {}
    # new_path = settings.MEDIA_ROOT + file

    # print(new_path)
    def csv_dict_list(variables_file):
        new_try = csv.DictReader(open(
            'C:/Users/home/Desktop/django projects/Costing/RecipeCosting/media/media/SupplierPriceListExport_1009453_12-23-202117-11-48.csv', newline=''))
        dict_list = []
        for line in new_try:
            dict_list.append(line)
        return dict_list

    device_values = csv_dict_list(sys.argv[1])
    # pprint.pprint(device_values)
    csv_files.append(device_values)
    unit_type = []

    for line in device_values:
        dic_data.update(line)
        for field in line:
            #c = line[field]
            name = []
            unit = []

            price = []
            unit_type.append({
                'Title': line['Description'],
                'Unit': line['Unit Size'],
                'Price': line['Price']
            })
        # data = Import_Data(name=line['Description'], unit=line['Unit Size'], unit_type=line['Unit Measure'],
        #                   price=line['Price'], company='Solstis')
        # print(data)
        # data.save()

    return render(request, 'cost/index.html', {
        'csv': files,
        'rows': device_values,
    })


def some_view_api(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C',
                    '"Testing"', "Here's a quote"])
    print(response)
    return response


def upload_file(request):
    if request.method == 'POST':
        form = FileFieldForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'cost/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = FileFieldForm()
    return render(request, 'cost/upload.html', {'form': form})


def recipe_upload(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        print(form)
        if form.is_valid:
            data = form.save(commit=False)
            data.save()

            return redirect('index')

    return render(request, 'cost/recipe-upload.html', {
        'form': RecipeForm()
    })


def recipe(request):
    recipe_data = Recipe.objects.all()
    title = []
    method = []
    for ing in recipe_data:

        title.append(ing.title)
        method.append(ing.method)
    # print(ingr_lines)

    ing = []
    ingr = []
    for i in recipe_data:
        ingr = i.recipe.split(',')
        ing.append(ingr[0:-1])

        for j in ing:
            i = j[0][0]
            ingr.append(i[0:-1])
    data = Import_Data.objects.all()
    a = []
    for i in ingr:
        print(i)
        for d in data:

            if d.name in i:

                a.append(i)

    print(a)

    # print(data)
    print(ingr[0])
    return render(request, 'cost/recipe.html', {
        'ing': ingr,
        'method': method[0],
        'title': title[0]
    })


# API data

def api_data_cost(request):
    data = Import_Data.objects.all()
    dic_data = []
    for d in data:
        dic_data.append({
            'Name': d.name,
            'Unit': d.unit,
            'Type': d.unit_type,
            'Price': d.price,
            'Company': d.company
        })

    return HttpResponse(json.dumps(dic_data), content_type="application/json")


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = 'index.html'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
