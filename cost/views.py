from django.shortcuts import render
import csv
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from csv import DictReader
import sys
import pprint
import os
from django.conf import settings

from .models import Exeldocument, Import_Data
from django.views.generic.edit import FormView
from .forms import FileFieldForm

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
