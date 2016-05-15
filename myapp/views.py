from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def breathe(request):
    return render(request, 'breathing_exercise.html')

def welcome(request):
    return render(request, 'intro.html')
#return render(request, 'welcome.html')

def submit_name(request):
    name = request.POST.get('name', 'Anonymous')
    return render(request, 'how-old-are-you.html', {'name': name})

def submit_age(request):
    age = request.GET.get('age', -1)
    return redirect('/cbt/your-symptoms')

def intro(request):
    return render(request, 'intro.html')

def intro2(request):
    return render(request, 'intro2.html')

def intro3(request):
    return render(request, 'intro3.html')

def getting_started(request):
    return render(request, 'getting_started.html')

def your_symptoms(request):
    return render(request, 'your_symptoms.html')

def how_to_use(request):
    return render(request, 'how_to_use.html')

def how_to_after_an_episode(request):
    return render(request, 'after_an_episode.html')

def post_episode(request):
    return render(request, 'post_episode.html')

def monitoring_your_progress(request):
    return render(request, 'monitoring_your_progress.html')

def what_is_cbt(request):
    return render(request, 'what_is_cbt.html')

def what_is_fnd(request):
    return render(request, 'what_is_fnd.html')

def fin(request):
    return render(request, 'fin.html')

def relaxing_sounds(request):
    return render(request, 'relaxing_sounds.html')

def finger_exercises(request):
    return render(request, 'finger_exercises.html')

def inspiration(request):
    return render(request, 'inspiration.html')

def post_episode_details_submitted(request):
    return render(request, 'post_episode_details_submitted.html')

def day_log(request):
    return render(request, 'day_log.html')
