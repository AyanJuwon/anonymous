from .models import Message
from django.shortcuts import render, HttpResponse, redirect
from .forms import MessageForm
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    return render(request, 'index.html')


def createMessage(request, user):

    # use django forms to get data and save it to the db

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            user = request.user
            mssg = form.cleaned_data['message']

            p = Message(int(user.id), mssg)
            p = Message.objects.create(user_id=int(user.id), message=mssg)

            print(user.id)
            print(id)
            print(user)
            p.save()

            saved = True
            # return redirect("createMessage",  {'form': form, 'saved': saved, 'user': user}, user=user)
            return render(request, 'index.html')
    else:
        form = MessageForm()
    return render(request, 'create.html', {'form': form})


# create page for user to view messages relating to them filter by date i guess
def userDashboard(response):

    data = Message.objects.filter(user=response.user)
    # user = get_object_or_404(PasswordList,pk = id)

    # dynamically get id of data, pass to delete function n then execute
    return render(response, 'view_posts.html', {'data': data})
