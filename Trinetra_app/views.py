import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CareerForm


# Create your views here.
def Base(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'base.html', {'Current_year': Current_year})


def Home(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'home.html', {
        'Current_year': Current_year})  # for passing current year from base function call that function in this


def About(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'about.html', {'Current_year': Current_year})


def service(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'services.html', {'Current_year': Current_year})


def contact_us(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'contact_us.html', {'Current_year': Current_year})


def career(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'career.html', {'Current_year': Current_year})


def Career_form(request):
    Current_year = datetime.datetime.now().year

    if request.method == 'POST':

        full_name = request.POST.get('inputName')
        email = request.POST.get('inputEmail')
        address = request.POST.get('inputAddress')
        address_2 = request.POST.get('inputAddress2')
        phone = request.POST.get('inputphone')
        position = request.POST.get('inputPosition')
        experience = request.POST.get('inputExperience')
        attachment = request.FILES.get('inputattach')

        print(full_name, email, address, address_2, phone, position, experience, attachment)

        # Save the form data to the database
        applicant = CareerForm(
            full_name=full_name,
            email=email,
            address=address,
            address2=address_2,
            phone=phone,
            choose_position=position,
            year_of_experience=experience,
            resume=attachment
        )

        applicant.save()

        # Display a success message
        messages.success(request, 'Your form has been submitted successfully!')
        return redirect('career_form')  # Redirect to a success page or another URL
    else:
        # Handle GET request or other methods
        pass

    return render(request, 'carrer_form.html', {'Current_year': Current_year})


def Enterprise_acess_control_systems(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'Enterprise_access_control.html', {'Current_year': Current_year})


def Enterprise_video_servillance(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'video_servillance_solution.html', {'Current_year': Current_year})


def Enterprise_fire_alaram_detection(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'fire_alarm_detection_system.html', {'Current_year': Current_year})


def Enterprise_Data_center_solution(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'datacenter_solution.html', {'Current_year': Current_year})


def integrated_security(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'integrated_security_solution.html', {'Current_year': Current_year})


def visitor_management_systems(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'visitor_managemet_system.html', {'Current_year': Current_year})


def Barier_basedd_solution(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'barrier_based_solutions.html', {'Current_year': Current_year})


def touchless_access(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'tochless_access_soltuon.html', {'Current_year': Current_year})


def Enterprise_Web_development(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'Enterprise_web_development.html', {'Current_year': Current_year})


def Enterprise_digital_marketing(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'Enterprise_degital_marketing.html', {'Current_year': Current_year})


def Enterprise_web_designing(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'enterprise_web_designing.html', {'Current_year': Current_year})


def Enterprise_App_development(request):
    Current_year = datetime.datetime.now().year
    return render(request, 'Enterprise_app_development.html', {'Current_year': Current_year})
