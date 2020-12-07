from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages


#FRONTDOOR
def frontdoor(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('is Logged in'))
			return redirect('logged')
		else:
			messages.success(request, ('Error Logging In - Please Try Again...'))
			return redirect('frontdoor')
	else:
		return render(request, "authenticate/frontdoor.html", {})


#LOGGED IN
def logged(request):
	return render(request, "authenticate/logged.html", {})


#LOGOUT
def logout_user(request):
	logout(request)
	messages.success(request, ('NexCour Acct Has Been Logged Out'))
	return redirect('frontdoor')


#ACCOUNT
def user_acct(request):
	return render(request, "account/acct.html", {})


#PAYROLL
def payroll(request):
	return render(request, "payroll/payroll.html", {})

#PAYROLL LOGIN PAGE
def payroll_login(request):
	if request.method == "POST":
		pin_num = request.POST['paypin']
		if pin_num == "4321":
			messages.success(request, ('Logged in to Payroll'))
			return render(request, "payroll/payroll.html", {})
		else:
			messages.success(request, ('Wrong Pin, Try Again'))
			return render(request, "authenticate/paylogin.html", {})
	else:
		return render(request, "authenticate/paylogin.html", {})

	

		
#HOME
def emp1(request):
	import requests
	import json

	if request.method == 'POST':
		quote = request.POST['quote']
		quote = quote.upper() 


	# By Depts.

		if quote == "EXECUTIVES":

			#CEO
			employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/16/?format=json")
			direct1 = json.loads(employee1.content) 
			#COO
			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/17/?format=json")
			direct2 = json.loads(employee2.content)
			#CTO
			employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/18/?format=json")
			direct3 = json.loads(employee3.content)
			#CFO
			employee12 = requests.get("http://nexcouremployees.courdevelops.com/employees/28/?format=json")
			direct12 = json.loads(employee12.content)
			#CCO
			employee13 = requests.get("http://nexcouremployees.courdevelops.com/employees/29/?format=json")
			direct13 = json.loads(employee13.content)
			#CISO
			employee14 = requests.get("http://nexcouremployees.courdevelops.com/employees/30/?format=json")
			direct14 = json.loads(employee14.content)
			#CMO
			employee15 = requests.get("http://nexcouremployees.courdevelops.com/employees/31/?format=json")
			direct15 = json.loads(employee15.content)

			return render(request, 'departments/clevel.html', {'quote': quote, 'direct1': direct1, 'direct2': direct2, 'direct3': direct3,
				'direct12': direct12, 'direct13': direct13, 'direct14': direct14, 'direct15': direct15})


		if quote == "DEVELOPERS":
			#Lead Developer
			employee4 = requests.get("http://nexcouremployees.courdevelops.com/employees/19/?format=json")
			direct4 = json.loads(employee4.content)
			
			employee5 = requests.get("http://nexcouremployees.courdevelops.com/employees/20/?format=json")
			direct5 = json.loads(employee5.content)

			employee6 = requests.get("http://nexcouremployees.courdevelops.com/employees/21/?format=json")
			direct6 = json.loads(employee6.content)

			employee7 = requests.get("http://nexcouremployees.courdevelops.com/employees/22/?format=json")
			direct7 = json.loads(employee7.content)

			employee8 = requests.get("http://nexcouremployees.courdevelops.com/employees/24/?format=json")
			direct8 = json.loads(employee8.content)

			employee9 = requests.get("http://nexcouremployees.courdevelops.com/employees/25/?format=json")
			direct9 = json.loads(employee9.content)

			employee10 = requests.get("http://nexcouremployees.courdevelops.com/employees/26/?format=json")
			direct10 = json.loads(employee10.content)

			employee11 = requests.get("http://nexcouremployees.courdevelops.com/employees/27/?format=json")
			direct11 = json.loads(employee11.content)

			return render(request, 'departments/devs.html', {'quote': quote, 'direct4': direct4, 'direct5': direct5, 'direct6': direct6,
				'direct7': direct7, 'direct8': direct8, 'direct9': direct9, 'direct10': direct10, 'direct11': direct11})

	#############################################################################################################
		
	# By Individuals

		# By ID #
		if quote == "10002101":
			employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/16/?format=json")
			direct1 = json.loads(employee1.content) 
			return render(request, 'home1.html', {'quote': quote, 'direct1': direct1})

		# By Name
		if quote == "TIM FLURRY":
			employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/16/?format=json")
			direct1 = json.loads(employee1.content)
			return render(request, 'home1.html', {'quote': quote, 'direct1': direct1})

		# By Job Title
		if quote == "CEO":
			employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/16/?format=json")
			direct1 = json.loads(employee1.content)
			return render(request, 'home1.html', {'quote': quote, 'direct1': direct1})



	#############################################################################################################	

		# By ID #
		if quote == "10002102":
			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/17/?format=json")
			direct2 = json.loads(employee2.content)
			return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

		# By Name
		if quote == "SAMANTHA MITCHELL":
			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/17/?format=json")
			direct2 = json.loads(employee2.content)
			return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

		# By Job Title
		if quote == "COO":
			quote = quote.upper()
			employee2 = requests.get("http://nexcouremployees.courdevelops.com/employees/17/?format=json")
			direct2 = json.loads(employee2.content)
			return render(request, 'home2.html', {'quote': quote, 'direct2': direct2})

	#############################################################################################################	

		# By ID #
		if quote == "10002103":
			employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/18/?format=json")
			direct3 = json.loads(employee3.content)
			return render(request, 'home3.html', {'quote': quote, 'direct3': direct3})

		# By Name
		if quote == "JOHN GOLANY":
			employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/18/?format=json")
			direct3 = json.loads(employee3.content)
			return render(request, 'home3.html', {'quote': quote, 'direct3': direct3})

		# By Job Title
		if quote == "CTO":
			quote = quote.upper()
			employee3 = requests.get("http://nexcouremployees.courdevelops.com/employees/18/?format=json")
			direct3 = json.loads(employee3.content)
			return render(request, 'home3.html', {'quote': quote, 'direct3': direct3})

	#############################################################################################################	

		# By ID #
		if quote == "10002104":
			employee4 = requests.get("http://nexcouremployees.courdevelops.com/employees/19/?format=json")
			# global direct4
			direct4 = json.loads(employee4.content)
			return render(request, 'home4.html', {'quote': quote, 'direct4': direct4})

		# By Name
		if quote == "ALEXHANDER VOSIV":
			employee4 = requests.get("http://nexcouremployees.courdevelops.com/employees/19/?format=json")
			direct4 = json.loads(employee4.content)
			return render(request, 'home4.html', {'quote': quote, 'direct4': direct4})

		# By Job Title
		if quote == "LEAD DEVELOPER":
			employee4 = requests.get("http://nexcouremployees.courdevelops.com/employees/19/?format=json")
			direct4 = json.loads(employee4.content)
			return render(request, 'home4.html', {'quote': quote, 'direct4': direct4})

	#############################################################################################################	

		# By ID #
		if quote == "10002205":
			employee5 = requests.get("http://nexcouremployees.courdevelops.com/employees/20/?format=json")
			# global direct5
			direct5 = json.loads(employee5.content)
			return render(request, 'home5.html', {'quote': quote, 'direct5': direct5})

		# By Name
		if quote == "RITVIK PRASAD":
			employee5 = requests.get("http://nexcouremployees.courdevelops.com/employees/20/?format=json")
			direct5 = json.loads(employee5.content)
			return render(request, 'home5.html', {'quote': quote, 'direct5': direct5})

	#############################################################################################################	

		# By ID #
		if quote == "10002206":
			employee6 = requests.get("http://nexcouremployees.courdevelops.com/employees/21/?format=json")
			# global direct6
			direct6 = json.loads(employee6.content)
			return render(request, 'home6.html', {'quote': quote, 'direct6': direct6})

		# By Name
		if quote == "SAMANTHA OWENS":
			employee6 = requests.get("http://nexcouremployees.courdevelops.com/employees/21/?format=json")
			direct6 = json.loads(employee6.content)
			return render(request, 'home6.html', {'quote': quote, 'direct6': direct6})

	#############################################################################################################	

		# By ID #
		if quote == "10002215":
			employee7 = requests.get("http://nexcouremployees.courdevelops.com/employees/22/?format=json")
			# global direct7
			direct7 = json.loads(employee7.content)
			return render(request, 'home7.html', {'quote': quote, 'direct7': direct7})

		# By Name	
		if quote == "DARCY SMITH":
			employee7 = requests.get("http://nexcouremployees.courdevelops.com/employees/22/?format=json")
			direct7 = json.loads(employee7.content)
			return render(request, 'home7.html', {'quote': quote, 'direct7': direct7})	

	#############################################################################################################

		# By ID #
		if quote == "10002216":
			employee8 = requests.get("http://nexcouremployees.courdevelops.com/employees/24/?format=json")
			# global direct8
			direct8 = json.loads(employee8.content)
			return render(request, 'home8.html', {'quote': quote, 'direct8': direct8})

		# By Name
		if quote == "FRED GATES":
			employee8 = requests.get("http://nexcouremployees.courdevelops.com/employees/24/?format=json")
			direct8 = json.loads(employee8.content)
			return render(request, 'home8.html', {'quote': quote, 'direct8': direct8})

	#############################################################################################################

		# By ID #
		if quote == "10002217":
			employee9 = requests.get("http://nexcouremployees.courdevelops.com/employees/25/?format=json")
			# global direct9
			direct9 = json.loads(employee9.content)
			return render(request, 'home9.html', {'quote': quote, 'direct9': direct9})

		# By Name
		if quote == "KHARY STARS":
			employee9 = requests.get("http://nexcouremployees.courdevelops.com/employees/25/?format=json")
			direct9 = json.loads(employee9.content)
			return render(request, 'home9.html', {'quote': quote, 'direct9': direct9})

	#############################################################################################################

		# By ID #
		if quote == "10002218":
			employee10 = requests.get("http://nexcouremployees.courdevelops.com/employees/26/?format=json")
			# global direct10
			direct10 = json.loads(employee10.content)
			return render(request, 'home10.html', {'quote': quote, 'direct10': direct10})

		# By Name
		if quote == "MARK THOMPSON":
			employee10 = requests.get("http://nexcouremployees.courdevelops.com/employees/26/?format=json")
			direct10 = json.loads(employee10.content)
			return render(request, 'home10.html', {'quote': quote, 'direct10': direct10})

	#############################################################################################################

		# By ID #
		if quote == "10002219":
			employee11 = requests.get("http://nexcouremployees.courdevelops.com/employees/27/?format=json")
			#global direct11
			direct11 = json.loads(employee11.content)
			return render(request, 'home11.html', {'quote': quote, 'direct11': direct11})

		# By Name
		if quote == "REBECCA MOLEY":
			employee11 = requests.get("http://nexcouremployees.courdevelops.com/employees/27/?format=json")
			direct11 = json.loads(employee11.content)
			return render(request, 'home11.html', {'quote': quote, 'direct11': direct11})

	#############################################################################################################

		# By ID #
		if quote == "10003201":
			employee12 = requests.get("http://nexcouremployees.courdevelops.com/employees/28/?format=json")
			# global direct12
			direct12 = json.loads(employee12.content)
			return render(request, 'home12.html', {'quote': quote, 'direct12': direct12})

		# By Name
		if quote == "EMILY RICKETS":
			employee12 = requests.get("http://nexcouremployees.courdevelops.com/employees/28/?format=json")
			direct12 = json.loads(employee12.content)
			return render(request, 'home12.html', {'quote': quote, 'direct12': direct12})


		# By Job Title
		if quote == "CFO":
			quote = quote.upper()
			employee12 = requests.get("http://nexcouremployees.courdevelops.com/employees/28/?format=json")
			direct12 = json.loads(employee12.content)
			return render(request, 'home12.html', {'quote': quote, 'direct12': direct12})


	#############################################################################################################

		# By ID #
		if quote == "10003202":
			employee13 = requests.get("http://nexcouremployees.courdevelops.com/employees/29/?format=json")
			# global direct12
			direct13 = json.loads(employee13.content)
			return render(request, 'home13.html', {'quote': quote, 'direct13': direct13})

		# By Name
		if quote == "JAMILA VAUGHN":
			employee13 = requests.get("http://nexcouremployees.courdevelops.com/employees/29/?format=json")
			direct13 = json.loads(employee13.content)
			return render(request, 'home13.html', {'quote': quote, 'direct13': direct13})


		# By Job Title
		if quote == "CCO":
			quote = quote.upper()
			employee13 = requests.get("http://nexcouremployees.courdevelops.com/employees/29/?format=json")
			direct13 = json.loads(employee13.content)
			return render(request, 'home13.html', {'quote': quote, 'direct13': direct13})


	#############################################################################################################

		# By ID #
		if quote == "10003203":
			employee14 = requests.get("http://nexcouremployees.courdevelops.com/employees/30/?format=json")
			# global direct12
			direct14 = json.loads(employee14.content)
			return render(request, 'home14.html', {'quote': quote, 'direct14': direct14})

		# By Name
		if quote == "BRENDA MARTANI":
			employee14 = requests.get("http://nexcouremployees.courdevelops.com/employees/30/?format=json")
			direct14 = json.loads(employee14.content)
			return render(request, 'home14.html', {'quote': quote, 'direct14': direct14})

		# By Job Title
		if quote == "CISO":
			employee14 = requests.get("http://nexcouremployees.courdevelops.com/employees/30/?format=json")
			direct14 = json.loads(employee14.content)
			return render(request, 'home14.html', {'quote': quote, 'direct14': direct14})

	#############################################################################################################

		# By ID #
		if quote == "10003204":
			employee15 = requests.get("http://nexcouremployees.courdevelops.com/employees/31/?format=json")
			direct15 = json.loads(employee15.content)
			return render(request, 'home15.html', {'quote': quote, 'direct15': direct15})

		# By Name
		if quote == "MAI FONTANA":
			employee15 = requests.get("http://nexcouremployees.courdevelops.com/employees/31/?format=json")
			direct15 = json.loads(employee15.content)
			return render(request, 'home15.html', {'quote': quote, 'direct15': direct15})

		# By Job Title
		if quote == "CMO":
			quote = quote.upper()
			employee15 = requests.get("http://nexcouremployees.courdevelops.com/employees/31/?format=json")
			direct15 = json.loads(employee15.content)
			return render(request, 'home15.html', {'quote': quote, 'direct15': direct15})


	#############################################################################################################

	# ERROR page

		else:
			error1 = "error"
			return render(request, 'error.html', {'quote': quote, 'error1': error1})

	#############################################################################################################
		
	else:
		nothingyet = "NexCour Employee Database:"
		# For Portfolio just say:  These particular employees work for this ficticious company.  Enter either their ID or Name to get more info
		return render(request, 'home.html', {'nothingyet': nothingyet})




	#############################################################################################################

#Render to Payroll

#CEO
def payroll(request):
	import requests
	import json

	employee1 = requests.get("http://nexcouremployees.courdevelops.com/employees/16/?format=json")
	direct1 = json.loads(employee1.content) 
	return render(request, 'payroll/payroll.html', {'direct1': direct1})	




