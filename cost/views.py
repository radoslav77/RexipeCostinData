from django.shortcuts import render
import csv
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from pathlib import Path

from .models import Exeldocument
from django.views.generic.edit import FormView
from .forms import FileFieldForm
# Create your views here.


def index(request):
    files = Exeldocument.objects.filter(title='ritter')
    csv_files = []

    for file in files:
        csv_files.append(file)
    # print(csv_files)
    for ex in csv_files:
        excel_sheet = ex.doc
        print(ex.doc)
        path = Path(ex.doc)
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['first_name'], row['last_name'])
        for d in excel_sheet:
            # print(d)
            '''
            with open(d, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    print(row['Description'], row['Unit Size'])
                  # print(', '.join(row))
                  '''
    return render(request, 'cost/index.html')


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
