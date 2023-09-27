from django.shortcuts import render, redirect
from . models import StudentData
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse



def student_home_data(request):
    return render(request, 'base.html')  

def student_login_logout_data(request):
    return render(request, 'front.html')  



def student_show_data(request):
    data = StudentData.objects.all()
    data_dict = {'showdata' : data}
    if request.method == "POST":
        Name = request.POST['name']
        Address = request.POST['address']
        Contact = request.POST['contact']
        data = StudentData(student_name=Name, student_address= Address, student_contact=Contact)
        data.save()
    return render(request, 'table.html', data_dict)




def student_create_data(request):
    if request.method == "POST":
        Name = request.POST['name']
        Address = request.POST['address']
        Contact = request.POST['contact']
        data = StudentData(student_name=Name, student_address= Address, student_contact=Contact)
        data.save()
        print(data)
        return redirect('showdata')
    return render(request, 'form.html')




def student_edit_data(request, id):
    data = StudentData.objects.get(id = id)
    data_dict = {'editdata' : data}
    print(data.student_name)
    if request.method == "POST":
        Name = request.POST['name']
        Address = request.POST['address']
        Contact = request.POST['contact']
        data.student_name = Name
        data.student_address = Address
        data.student_contact = Contact
        data.save()
        print(data)
        return redirect('showdata')
    return render(request, 'edit.html', data_dict)
    


def student_del_data(request,id):
    data = StudentData.objects.get(id = id)
    data.delete()
    return redirect('showdata')
# Create your views here.


def signupModal(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if len(username)<5:
                messages.error(request, 'username must be greater than five character please try again and enter five character user name!')
                return redirect('loginsignup')
            if pass1 != pass2:
                messages.error(request, 'enter password do not match please try again!')
                return redirect('loginsignup')
            myuser = User.objects.create_user(username,email,pass1)
            myuser.save()
            messages.success(request, "account created")
            return redirect('loginsignup')  
    except:
        return HttpResponse(request, '404- Bad request')
        

def loginModal(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        myuser = authenticate(username=loginusername,password=loginpassword)
        
        if myuser is not None:
            login(request,myuser)
            messages.success(request, 'login sucessfully')
            return redirect('home')
        else:
            messages.error(request, "given details not match we can't cotinue your Login Please check details and try again to Login!")
            return redirect('loginsignup')
    return HttpResponse("404 Bad Request")
        


def logoutModal(request):
    logout(request)
    messages.success(request, 'logout sucessfully')
    return redirect('loginsignup')
    

