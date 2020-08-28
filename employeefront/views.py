from django.shortcuts import render
from django.contrib import messages

#HOME
def home(request):
	import requests
	import json
	employee_request = requests.get("http://nexcouremployees.courdevelops.com/employees/?format=json")
	employee = json.loads(employee_request.content)
	return render(request, 'home.html', {'employee': employee})
