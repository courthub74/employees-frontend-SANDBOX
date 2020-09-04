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

		if quote == "James Henry":
			employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/1/?format=json")
			direct1 = json.loads(employee1.content)
			return render(request, 'home.html', {'quote': quote, 'direct1': direct1})	


	#############################################################################################################	

		if quote == "10001404":
			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/2/?format=json")
			global direct2
			direct2 = json.loads(employee2.content)
			return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

		if quote == "Debbie Michaels":
			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/2/?format=json")
			direct2 = json.loads(employee2.content)
			return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

	#############################################################################################################	

		if quote == "10001407":
			employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/3/?format=json")
			global direct3
			direct3 = json.loads(employee3.content)
			return render(request, 'home3.html', {'quote': quote, 'direct3': direct3})

		if quote == "DeSean Timms":
			employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/3/?format=json")
			direct3 = json.loads(employee3.content)
			return render(request, 'home3.html', {'quote': quote, 'direct3': direct3})

	#############################################################################################################	

		if quote == "10001410":
			employee4 = requests.get("http://nexcouremployees.courdevelops.com/employees/4/?format=json")
			global direct4
			direct4 = json.loads(employee4.content)
			return render(request, 'home4.html', {'quote': quote, 'direct4': direct4})

		if quote == "Brittany Samuels":
			employee4 = requests.get("http://nexcouremployees.courdevelops.com/employees/4/?format=json")
			direct4 = json.loads(employee4.content)
			return render(request, 'home4.html', {'quote': quote, 'direct4': direct4})

	#############################################################################################################	

		if quote == "10001413":
			employee5 = requests.get("http://nexcouremployees.courdevelops.com/employees/5/?format=json")
			global direct5
			direct5 = json.loads(employee5.content)
			return render(request, 'home5.html', {'quote': quote, 'direct5': direct5})

		if quote == "Nathan McCreary":
			employee5 = requests.get("http://nexcouremployees.courdevelops.com/employees/5/?format=json")
			direct5 = json.loads(employee5.content)
			return render(request, 'home5.html', {'quote': quote, 'direct5': direct5})

	#############################################################################################################	

		if quote == "10001501":
			employee6 = requests.get("http://nexcouremployees.courdevelops.com/employees/6/?format=json")
			global direct6
			direct6 = json.loads(employee6.content)
			return render(request, 'home6.html', {'quote': quote, 'direct6': direct6})

		if quote == "Amy Decker":
			employee6 = requests.get("http://nexcouremployees.courdevelops.com/employees/6/?format=json")
			direct6 = json.loads(employee6.content)
			return render(request, 'home6.html', {'quote': quote, 'direct6': direct6})	

	#############################################################################################################	

		if quote == "10001502":
			employee7 = requests.get("http://nexcouremployees.courdevelops.com/employees/7/?format=json")
			global direct7
			direct7 = json.loads(employee7.content)
			return render(request, 'home7.html', {'quote': quote, 'direct7': direct7})

		if quote == "Mark Johns":
			employee7 = requests.get("http://nexcouremployees.courdevelops.com/employees/7/?format=json")
			direct7 = json.loads(employee7.content)
			return render(request, 'home7.html', {'quote': quote, 'direct7': direct7})	

	#############################################################################################################

		if quote == "10001503":
			employee8 = requests.get("http://nexcouremployees.courdevelops.com/employees/8/?format=json")
			global direct8
			direct8 = json.loads(employee8.content)
			return render(request, 'home8.html', {'quote': quote, 'direct8': direct8})

		if quote == "April Samuelson":
			employee8 = requests.get("http://nexcouremployees.courdevelops.com/employees/8/?format=json")
			direct8 = json.loads(employee8.content)
			return render(request, 'home8.html', {'quote': quote, 'direct8': direct8})

	#############################################################################################################

	# ERROR page

		else:
			error1 = "error"
			return render(request, 'error.html', {'quote': quote, 'error1': error1})

	#############################################################################################################
		
	else:
		nothingyet = "NexCour Employee information:"
		# For Portfolio just say:  These particular employees work for this ficticious company.  Enter either their ID or Name to get more info
		return render(request, 'home.html', {'nothingyet': nothingyet})




