from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect


from django.contrib.auth.decorators import login_required
from .models import Image
from django.db.models import Q


@login_required
def gallery_view(request):
   
    filter_term = request.GET.get('filter', '') 
    images = Image.objects.filter(
        Q(title__icontains=filter_term) | Q(description__icontains=filter_term)
    ).order_by('-uploaded_at') 

    return render(request, 'gallery/gallery.html', {'images': images})


@login_required
def upload_image(request):
  
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image_file = request.FILES.get('image')

        if image_file and title:
            Image.objects.create(
                title=title,
                description=description,
                image=image_file,
                uploaded_by=request.user
            )
            return redirect('gallery')  

    return render(request, 'gallery/upload_image.html')


@login_required
def like_image(request, image_id):
 
    image = get_object_or_404(Image, id=image_id)
    if request.user in image.likes.all():
        image.likes.remove(request.user)  
    else:
        image.likes.add(request.user) 
    return redirect('gallery')

@login_required
def dislike_image(request, image_id):
 
    image = get_object_or_404(Image, id=image_id)
    if request.user in image.dislikes.all():
        image.dislikes.remove(request.user) 
    else:
        image.dislikes.add(request.user)  
    return redirect('gallery')

@login_required
def delete_image(request, image_id):

    image = get_object_or_404(Image, id=image_id)
    if image.uploaded_by == request.user or request.user.is_superuser:
        image.delete()
    return redirect('gallery')


def register(request):
  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gallery')  
    else:
        form = UserCreationForm()

    return render(request, 'gallery/register.html', {'form': form})


def custom_login(request):
   
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('gallery') 
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  
    return redirect('gallery/login.html') 

@login_required
def profile(request):
   
    user_images = Image.objects.filter(uploaded_by=request.user).order_by('-uploaded_at')
    return render(request, 'gallery/profile.html', {'user_images': user_images})
