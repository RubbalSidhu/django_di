from django.http import HttpResponse
from django.views import View

class ContactView(View):
    # Logic which needs to be pulled out from the views (Ex. formatting logic). This can be wired in urls.py
    formatter = None

    def get(self, request):
        return HttpResponse(self.formatter.format('Rubbal Sidhu'))
