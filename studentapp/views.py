from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def home_view(request):

    if LoginDetail.objects.filter(email = request.POST.get('email'),
                                 password = request.POST.get('psw')):
        return render(request, 'features.html')
    return render(request,'home.html')

def features_view(request):
    dict = {
        'name' : name
    }
    return render(request,'features.html', context = dict)

def login_view(request):

    data = {}

    if(request.method == 'POST'):
        query_set = StudentDetail.objects.filter(application_no = request.POST.get('rollno'),
                                                father_name = request.POST.get('fname'),
                                                student_name = request.POST.get('sname'))
        info = {'qs':query_set}
        if query_set:
            return render(request, 'blank.html', context=info)
        else:
            data['result'] = 'invalid details'
            return render(request, 'login.html', context=data)
    return render(request, 'login.html')

def register_view(request):

    if (request.method == 'POST'):
        student_name = request.POST.get('Sname')
        father_name = request.POST.get('fathername')
        mother_name = request.POST.get('mothername')
        date_of_birth = request.POST.get('DOB')
        gender = request.POST.get('gender')
        email = request.POST.get('emailid')
        address = request.POST.get('address')
        higher_secondary_school_marks = request.POST.get('hssm')
        higher_secondary_school_name = request.POST.get('hssn')
        secondary_school_marks = request.POST.get('ssm')
        secdondary_school_name = request.POST.get('ssn')

        student_detail = StudentDetail()
        academics_detail = AcademicsDetail()

        #ORM queries
        student_detail.student_name = student_name
        student_detail.father_name = father_name
        student_detail.mother_name = mother_name
        student_detail.date_of_birth = date_of_birth
        student_detail.gender = gender
        student_detail.email = email
        student_detail.address = address

        student_detail.save()

        academics_detail.higher_secondary_school_marks = higher_secondary_school_marks
        academics_detail.higher_secondary_school_name = higher_secondary_school_name
        academics_detail.secondary_school_marks = secondary_school_marks
        academics_detail.secondary_school_marks = secondary_school_marks
        academics_detail.secdondary_school_name = secdondary_school_name

        academics_detail.save()

    #query_set = StudentDetail.objects.all()
    query_set = StudentDetail.objects.filter(application_no=1)
    info = { 'queryset': query_set }
    return render(request, 'register.html', context=info)

def signup_view(request):
    info = {}
    if (request.method == 'POST'):
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        user_name = request.POST.get('uname')
        birth_date = request.POST.get('date')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        address = request.POST.get('address')
        email = request.POST.get('email')
        info['first_name'] = first_name
        info['last_name'] = last_name
        info['user_name'] = user_name
        info['birth_date'] = birth_date
        info['city'] = city
        info['address'] = address
        info['email'] = email
        info['gender'] = gender
    if request.POST.get('edu1'):
        info['edu'] = request.POST.get('edu1')
    elif request.POST.get('edu1') and request.POST.get('edu2'):
        info['edu'] = request.POST.get('edu1') + request.POST.get('edu2')
    elif request.POST.get('edu1') and request.POST.get('edu2') and request.POST.get('edu3'):
        info['edu'] = request.POST.get('edu1') + request.POST.get('edu2') + request.POST.get('edu3')
    return render(request, 'signup.html', context= info )

def formula_view(request):
    simple_interest = {}

    if(request.method == 'POST'):
        principle = request.POST.get('Principle')
        principle = int(principle)
        rate = request.POST.get('Rate')
        rate = int(rate)
        time = request.POST.get('Time')
        time = int(time)
        simple_interest['result'] = (principle * rate * time / 100)
    return render(request,'formula.html', context = simple_interest)

name = ['Rimal', 'Felix', 'Akash', 'Yakubu']
address = ['Ludhiana', 'Jalandhar', 'Assam', 'Jalandhar']
info = zip(name, address)

def add_view(request):
    if (request.method == 'POST'):
        student_name = request.POST.get('Sname')
        father_name = request.POST.get('fathername')
        mother_name = request.POST.get('mothername')
        date_of_birth = request.POST.get('DOB')
        gender = request.POST.get('gender')
        email = request.POST.get('emailid')
        address = request.POST.get('address')
    
        student_detail = StudentDetail()

        student_detail.student_name = student_name
        student_detail.father_name = father_name
        student_detail.mother_name = mother_name
        student_detail.date_of_birth = date_of_birth
        student_detail.gender = gender
        student_detail.email = email
        student_detail.address = address

        student_detail.save()

    return render(request,'home.html')
