from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Garuda Eleven',
        'name' : 'Msy Aulya Salsabila Putri',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
