from django.shortcuts import render
from django.contrib import messages


#HOME
def emp1(request):
	import requests
	import json

	if request.method == 'POST':
		quote = request.POST['quote'] 
		# quote = quote.lower()

		# By ID #
		if quote == "10002101":
			employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/16/?format=json")
			global direct1
			direct1 = json.loads(employee1.content) 
			return render(request, 'home.html', {'quote': quote, 'direct1': direct1})

		# By Name
		if quote == "Tim Flurry":
			employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/16/?format=json")
			direct1 = json.loads(employee1.content)
			return render(request, 'home.html', {'quote': quote, 'direct1': direct1})

		# By Job Title
		if quote == "CEO":
			employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/16/?format=json")
			direct1 = json.loads(employee1.content)
			return render(request, 'home.html', {'quote': quote, 'direct1': direct1})		


	#############################################################################################################	

		# By ID #
		if quote == "10002102":
			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/17/?format=json")
			global direct2
			direct2 = json.loads(employee2.content)
			return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

		# By Name
		if quote == "Samantha Mitchell":
			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/17/?format=json")
			direct2 = json.loads(employee2.content)
			return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

		# By Job Title
		if quote == "COO":
			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/17/?format=json")
			direct2 = json.loads(employee2.content)
			return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

	#############################################################################################################	

		# By ID #
		if quote == "10002103":
			employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/18/?format=json")
			global direct3
			direct3 = json.loads(employee3.content)
			return render(request, 'home3.html', {'quote': quote, 'direct3': direct3})

		# By Name
		if quote == "John Golany":
			employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/18/?format=json")
			direct3 = json.loads(employee3.content)
			return render(request, 'home3.html', {'quote': quote, 'direct3': direct3})

		# By Job Title
		if quote == "CTO":
			employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/18/?format=json")
			direct3 = json.loads(employee3.content)
			return render(request, 'home3.html', {'quote': quote, 'direct3': direct3})

	#############################################################################################################	

		# By ID #
		if quote == "10002104":
			employee4 = requests.get("http://nexcouremployees.courdevelops.com/employees/19/?format=json")
			global direct4
			direct4 = json.loads(employee4.content)
			return render(request, 'home4.html', {'quote': quote, 'direct4': direct4})

		# By Name
		if quote == "Alexhander Vosiv":
			employee4 = requests.get("http://nexcouremployees.courdevelops.com/employees/19/?format=json")
			direct4 = json.loads(employee4.content)
			return render(request, 'home4.html', {'quote': quote, 'direct4': direct4})

		# By Job Title
		if quote == "Lead Developer":
			employee4 = requests.get("http://nexcouremployees.courdevelops.com/employees/19/?format=json")
			direct4 = json.loads(employee4.content)
			return render(request, 'home4.html', {'quote': quote, 'direct4': direct4})

	#############################################################################################################	

		# By ID #
		if quote == "10002205":
			employee5 = requests.get("http://nexcouremployees.courdevelops.com/employees/20/?format=json")
			global direct5
			direct5 = json.loads(employee5.content)
			return render(request, 'home5.html', {'quote': quote, 'direct5': direct5})

		# By Name
		if quote == "Ritvik Prasad":
			employee5 = requests.get("http://nexcouremployees.courdevelops.com/employees/20/?format=json")
			direct5 = json.loads(employee5.content)
			return render(request, 'home5.html', {'quote': quote, 'direct5': direct5})

		# By Job Title
		if quote == "Senior Full Stack Development":
			employee5 = requests.get("http://nexcouremployees.courdevelops.com/employees/20/?format=json")
			direct5 = json.loads(employee5.content)
			return render(request, 'home5.html', {'quote': quote, 'direct5': direct5})

	#############################################################################################################	

		# By ID #
		if quote == "10002206":
			employee6 = requests.get("http://nexcouremployees.courdevelops.com/employees/21/?format=json")
			global direct6
			direct6 = json.loads(employee6.content)
			return render(request, 'home6.html', {'quote': quote, 'direct6': direct6})

		# By Name
		if quote == "Samantha Owens":
			employee6 = requests.get("http://nexcouremployees.courdevelops.com/employees/21/?format=json")
			direct6 = json.loads(employee6.content)
			return render(request, 'home6.html', {'quote': quote, 'direct6': direct6})

		# By Job Title
		if quote == "Full Stack Development":
			employee6 = requests.get("http://nexcouremployees.courdevelops.com/employees/21/?format=json")
			direct6 = json.loads(employee6.content)
			return render(request, 'home6.html', {'quote': quote, 'direct6': direct6})	

	#############################################################################################################	

		# By ID #
		if quote == "10002215":
			employee7 = requests.get("http://nexcouremployees.courdevelops.com/employees/22/?format=json")
			global direct7
			direct7 = json.loads(employee7.content)
			return render(request, 'home7.html', {'quote': quote, 'direct7': direct7})

		# By Name	
		if quote == "Darcy Smith":
			employee7 = requests.get("http://nexcouremployees.courdevelops.com/employees/22/?format=json")
			direct7 = json.loads(employee7.content)
			return render(request, 'home7.html', {'quote': quote, 'direct7': direct7})	

		# By Job Title	
		if quote == "Front-end Development":
			employee7 = requests.get("http://nexcouremployees.courdevelops.com/employees/22/?format=json")
			direct7 = json.loads(employee7.content)
			return render(request, 'home7.html', {'quote': quote, 'direct7': direct7})	

	#############################################################################################################

		# By ID #
		if quote == "10002216":
			employee8 = requests.get("http://nexcouremployees.courdevelops.com/employees/24/?format=json")
			global direct8
			direct8 = json.loads(employee8.content)
			return render(request, 'home8.html', {'quote': quote, 'direct8': direct8})

		# By Name
		if quote == "Fred Gates":
			employee8 = requests.get("http://nexcouremployees.courdevelops.com/employees/24/?format=json")
			direct8 = json.loads(employee8.content)
			return render(request, 'home8.html', {'quote': quote, 'direct8': direct8})

		# By Job Title
		if quote == "Back-end Development":
			employee8 = requests.get("http://nexcouremployees.courdevelops.com/employees/24/?format=json")
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




