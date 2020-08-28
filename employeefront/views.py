from django.shortcuts import render
from django.contrib import messages

#HOME
def home(request):
	import requests
	import json
	employee_request = requests.get("http://nexcouremployees.courdevelops.com/employees/?format=json")
	employee = json.loads(employee_request.content)
	if request.method == 'POST':
		quote = request.POST['quote']
		return render(request, 'home.html', {'quote': quote})
	else:
		return render(request, 'home.html', {})
