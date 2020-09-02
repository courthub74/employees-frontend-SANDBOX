from django.shortcuts import render
from django.contrib import messages


#HOME
def emp1(request):
	import requests
	import json

	if request.method == 'POST':
		quote = request.POST['quote'] 

		if quote == "10001401":
			employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/1/?format=json")
			global direct1
			direct1 = json.loads(employee1.content)

			return render(request, 'home.html', {'quote': quote, 'direct1': direct1})

		else:
			if quote == "10001404":
				employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/2/?format=json")
				global direct2
				direct2 = json.loads(employee2.content)
				return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

			if quote == "10001407":
				employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/3/?format=json")
				global direct3
				direct3 = json.loads(employee3.content)
				return render(request, 'home3.html', {'quote': quote, 'direct3': direct3})
			

	else:
		nothingyet = "NexCour Employees List Goes Here..."
		return render(request, 'home.html', {'nothingyet': nothingyet})





# #HOME
# def emp2(request):
# 	import requests
# 	import json

# 	if request.method == 'POST':
# 		quote = request.POST['quote'] # or None

# 		if quote == "10001404":
# 			return render(request, 'home2.html', {})
# 			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/2/?format=json")
# 			global direct2
# 			direct2 = json.loads(employee2.content)

# 			return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

# 	else:
# 		nothingyet = "NexCour Employees List Goes Here..."
# 		return render(request, 'home2.html', {'nothingyet': nothingyet})


