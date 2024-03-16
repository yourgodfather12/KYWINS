from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ImageUploadForm
from .models import Image

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('upload_image')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_form.html', {'form': form})

def images_by_county(request):
    images = Image.objects.select_related('girl__county').all()
    return render(request, 'images_by_county.html', {'images': images})

# Additional views for authentication, permissions, etc. can be added here
