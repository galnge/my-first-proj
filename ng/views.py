from django.http import HttpResponse
import datetime

def current_datetime(request,name):
    html = f"<html><body>{name} ПИДОР </body></html>"
    return HttpResponse(html)
