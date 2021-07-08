from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')


# # function to display full password list

# def password_list(response):

#     data = PasswordList.objects.filter(user = response.user)
#     # user = get_object_or_404(PasswordList,pk = id)
    

#     # Delete data from list

#     # dynamically get id of data, pass to delete function n then execute
#     return render(response,'password.html',{'data':data})


