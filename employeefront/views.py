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
		employee_direct = requests.get("http://nexcouremployees.courdevelops.com/employees/" + quote + "?format=json")
		direct = json.loads(employee_direct.content)

		employee1_direct = requests.get("http://nexcouremployees.courdevelops.com/employees/" + quote)
		employee1 = json.loads(employee1_direct.content)
		
	
		return render(request, 'home.html', {'quote': quote, 'direct': direct, 'employee1': employee1})
	else:
		return render(request, 'home.html', {})
