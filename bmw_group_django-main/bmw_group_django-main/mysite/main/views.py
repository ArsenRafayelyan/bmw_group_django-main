from django.shortcuts import render, redirect
from .models import HomeVideo, Subtitle, HomeName, Content, About, Contact
from .forms import ContactForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactForm()
    home_name = HomeName.objects.all()[0]
    one_video = HomeVideo.objects.all()[0]
    subtitle_list = Subtitle.objects.all()
    content_list = Content.objects.all()[:3]
    last_item = Content.objects.all()[3]
    about = About.objects.all()
    return render(request, 'main/index.html', context={
        'home_name':home_name,
        'one_video':one_video,
        'subtitle_list':subtitle_list,
        'content_list':content_list,
        'last_item':last_item,
        'about':about,
        'form':form
    })