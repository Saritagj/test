from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserForm
from .models import UserModel
import os
from django.conf import settings as conf
from django.core.files.storage import default_storage


# Create 
def create(request):
    # form = UserForm()
    try:

        if request.method == 'POST':
            form = UserForm(request.POST,request.FILES)
            # form = UserForm(request.POST)
            # print("-----------------------")
            # print(form)
            # img_path = os.path.join(conf.TEMP_IMAGE_DIR, str(request.FILES))
            # f = request.FILES

            # file_name_2 = default_storage.save(img_path, f)
            # file_url = default_storage.url(file_name_2)
            print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
            
            # for key, file in request.FILES.items():
            #     print('_____++++++++++++++++++++++')
            #     path = file.name
            #     print(path)
            #     print(key)
            # print(request.FILES.items())
            if form.is_valid():
                print("#########################")
                # instance = UserModel(image=request.FILES['docfile'])
                form.save()
                messages.success(request, 'User created')
                return redirect('read')
            else:
                print("$$$$$$$$$$$$$$")
        else:
            form = UserForm()
            
            print('_____________________________')
            print(form)

        context = {'form':form}
        
        return render(request, 'app/create.html', context)
    except Exception as e:
        print("----------------------------------")
        print(e)

# Read
def read(request):
    user_data = UserModel.objects.all()
    context = { 'user_data': user_data }
    return render(request, 'app/read.html', context)

# Update
def update(request, pk):
    get_user_data = get_object_or_404(UserModel, pk=pk)
    form = UserForm(instance=get_user_data)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=get_user_data)

        if form.is_valid():
            form.save()
            messages.success(request, 'User updated')
            return redirect('read')

    context = { 'form':form }
    return render(request, 'app/update.html', context)

# Delete
def delete(request, pk):
    get_user = get_object_or_404(UserModel, pk=pk)
    get_user.delete()
    messages.error(request, 'User deleted')
    return redirect('/')