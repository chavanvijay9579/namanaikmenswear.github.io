from django.shortcuts import render,HttpResponse



# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')


    

def contact(request):
   

    return render(request, 'contact.html')
      