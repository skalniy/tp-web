from django.shortcuts import render
from django.core.paginator import Paginator

context = {
  'qtags' : [" "] * 3,
  'toptags' : [" "] * 20,
  'topusers' : [" "] * 10,
}

# Create your views here.
def index(request):
    questions = [
        {
            'title': 'title' + str(i),
            'id': i,
        } for i in range(1,100)
    ]
    context['questions'] = paginate(questions, request, 20)
    context['header'] = 'index'
    return render(request, './index.html', context)

def hot(request):
    questions = [
        {
            'title': 'title' + str(i),
            'id': i,
        } for i in range(1,100)
    ]
    context['questions'] = paginate(questions, request, 20)
    context['header'] = 'hot'
    return render(request, './index.html', context)

def tag(request, tag):
    questions = [
        {
            'title': 'title' + str(i),
            'id': i,
        } for i in range(1,100)
    ]
    context['questions'] = paginate(questions, request, 20)
    context['tag'] = tag
    context['header'] = 'tag'
    return render(request, './index.html', context)

def question(request, question_id):
    answers = [
        {
            'text': 'text' + str(i),
            'id': i,
        } for i in range(1,100)
    ]
    context['answers'] = paginate(answers, request, 30)
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

def paginate(objects_list, request, page_size):
    paginator = Paginator(objects_list, page_size)
    page = request.GET.get('page') if request.GET.get('page') else 1
    try:
        objects = paginator.page(page)
    except:
        objects = paginator.page(1)
    return objects
