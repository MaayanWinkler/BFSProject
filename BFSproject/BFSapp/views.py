from django.shortcuts import render , redirect ,HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Measurement

# Create your views here.
 
def user_login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/form')
        else:
            context = {
            "error": 'Email or Password was wrong.',
            }
            print("ERROR")
    return render(request, "login.html", {})



def check_user(request):
    print("*******************************************************")
    if request.method == "POST":
        if check_parameters(request.POST.get("email"), request.POST.get("password")):
            return render(request, "form.html", {"name": request.POST.get("username")})
        else:
            return render(request, "login.html",{})

def fill_form(request):    
    if request.POST:
        cycle = request.POST['cycle']
        diet = request.POST['diet']
        date = request.POST['date']
        temperature = request.POST['temperature']
        larvae_weight = request.POST['larvae_weight']
        before_dry = request.POST['before_dry']
        after_dry = request.POST['after_dry']
        
        Measurement.objects.create(
            cycle = cycle,
            diet = diet,
            date = date,
            temperature = temperature,
            larvae_weight = larvae_weight,
            before_dry = before_dry,
            after_dry = after_dry,
        )

    return render(request, "form.html",{})

def get_reports(request):
    all_measurements = Measurement.objects.get_queryset()
    return render(request, "reports.html",{})

def get_reports(request):
    # Replace this with your actual data retrieval logic
    all_measurements = [
        {'col1': 'Value 1', 'col2': 'Value 2', 'col3': 'Value 3', 'col4': 'Value 4', 'col5': 'Value 5', 'col6': 'Value 6', 'col7': 'Value 7'},
        {'col1': 'Value 8', 'col2': 'Value 9', 'col3': 'Value 10', 'col4': 'Value 11', 'col5': 'Value 12', 'col6': 'Value 13', 'col7': 'Value 14'},
        # Add more data as needed
    ]
    all_measurements = Measurement.objects.all()
    data = []

    for item in all_measurements:
        row_dict = {
            'col1': item.cycle,
            'col2': item.diet,
            'col3': item.date,
            'col4': item.temperature,
            'col5': item.larvae_weight,
            'col6': item.before_dry,
            'col7': item.after_dry,
        }
    data.append(row_dict)

    return render(request, 'reports.html', {'data_from_server': data})

def filter_view(request):
    # Handle user input for filtering
    filter_option = request.GET.get('filter_option', '')  # Get the selected filter option from the query string
    
    queryset = []

    # Apply filtering based on the selected option
    if filter_option == 'cycle':
        queryset = Measurement.objects.filter(cycle=request.GET.get('filter_text'))
    elif filter_option == 'diet':
        queryset = Measurement.objects.filter(diet__icontains=request.GET.get('filter_text', ''))
    elif filter_option == 'temperature':
        queryset = Measurement.objects.filter(field4__icontains=request.GET.get('filter_text', ''))
    else:
        queryset = Measurement.objects.all()

    data = []

    if queryset.__len__() > 0:
        for item in queryset:
            row_dict = {
                'col1': item.cycle,
                'col2': item.diet,
                'col3': item.date,
                'col4': item.temperature,
                'col5': item.larvae_weight,
                'col6': item.before_dry,
                'col7': item.after_dry,
            }
        data.append(row_dict)

    return render(request, 'filter.html', {'data_from_server': data})
