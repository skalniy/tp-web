from django.shortcuts import render

context = {
  'qtags' : [" "] * 3,
  'toptags' : [" "] * 20,
  'topusers' : [" "] * 10,
}

# Create your views here.
def index(request):
    context['questions'] = [" "] * 20
    context['qtags'] = [" "] * 3
    return render(request, './index.html', context)

def hot(request):
    context['questions'] = [" "] * 20
    context['qtags'] = [" "] * 3
    return render(request, './hot.html', context)

def tag(request, tag):
    context['questions'] = [" "] * 20
    context['tag'] = tag
    context['qtags'] = [" "] * 3
    return render(request, './tag.html', context)

def question(request, question_id):
    context['qtags'] = [" "] * 3
    context['answers'] = [" "] * 20
    context['question_id'] = question_id
    return render(request, './question.html', context)

def login(request):
    return render(request, './login.html', context)

def signup(request):
    return render(request, './signup.html', context)

def ask(request):
    return render(request, './ask.html', context)

def settings(request):
    return render(request, './settings.html', context)
