from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django import forms


class DocForm(forms.Form):
    document = forms.FileInput()

def index(request):
    template = loader.get_template("index.html")
    if request.method == "POST":
    # create a form instance and populate it with data from the request:
        form = DocForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DocForm()
    context = {"form": form}
    return HttpResponse(template.render(context, request))