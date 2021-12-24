from django.shortcuts import render
import csv
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import pandas as pd
from csv import DictReader
import sys
import pprint
import os
from django.conf import settings

from .models import Exeldocument
from django.views.generic.edit import FormView
from .forms import FileFieldForm

# Create your views here.


dir_name = "/media/"


def index(request):

    files = Exeldocument.objects.filter(title='ritter')
    csv_files = []
    field_names = []
    #new_path = settings.MEDIA_ROOT + file

    # print(new_path)
    def csv_dict_list(variables_file):
        new_try = csv.DictReader(open(
            'C:/Users/home/Desktop/django projects/Costing/RecipeCosting/media/media/SupplierPriceListExport_1009451_12-23-202117-09-42.csv', newline=''))
        dict_list = []
        for line in new_try:
            dict_list.append(line)
        return dict_list

    device_values = csv_dict_list(sys.argv[1])
    pprint.pprint(device_values)
    '''
        spamreader = csv.reader(f, delimiter=' ', quotechar='|')
        reader = csv.DictReader(f)
        order_dict_list = list(reader)[0]
        dict_csv = dict(order_dict_list)
        csv_files.append(dict_csv)
        print(dict_csv)
        # for row in spamreader:
        # csv_files.append(row)
        #dict_from_csv = {rows[0]: rows[1] for rows in spamreader}
        # print(dict_from_csv)
        '''
    # open file in read mode
    with open('C:/Users/home/Desktop/django projects/Costing/RecipeCosting/media/media/SupplierPriceListExport_1009451_12-23-202117-09-42.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
    # get column names from a csv file
        column_names = csv_dict_reader.fieldnames
        # field_names.append(column_names)
        # print(column_names)

    # for line in csv_files:
        # print(line)

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
