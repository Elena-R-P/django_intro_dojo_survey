from django.shortcuts import render

def index(request):
    locations = [
        'San Jose',
        'Chicago',
        'Seattle',
    ]
    languages = [
        'Java',
        'Python',
        'C#',
        'MERN'
    ]
    dojo_locations = {
        'locations': locations,
        'languages' : languages
    }
    return render(request, 'index.html', dojo_locations)

def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    city_from_form = request.POST['city']
    lang_from_form = request.POST['lang']
    comment_from_form = request.POST['comment']
    context = {
        "name_on_template" : name_from_form,
        "city_on_template" : city_from_form,
        "lang_on_template" : lang_from_form,
        "comment_on_template" : comment_from_form
    }
    return render(request,"show.html",context)