from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Tag
from django.shortcuts import get_object_or_404

context = {
  'toptags' : [" "] * 20,
  'topusers' : [" "] * 10,
}

# Create your views here.
def index(request):
    questions = Question.objects.recent()
    context['questions'] = paginate(questions, request, 20)
    for q in context['questions']: q.taglist = q.tags.all()
    context['header'] = 'index'
    return render(request, './index.html', context)

def hot(request):
    questions = Question.objects.hot()
    context['questions'] =  paginate(questions, request, 20)
    for q in context['questions']: q.taglist = q.tags.all()
    context['header'] = 'hot'
    return render(request, './index.html', context)

def tag(request, tag):
    questions = get_object_or_404(Tag, pk=tag).question_set.all()
    context['questions'] = paginate(questions, request, 20)
    for q in context['questions']: q.taglist = q.tags.all()
    context['tag'] = tag
    context['header'] = 'tag'
    return render(request, './index.html', context)

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.taglist = question.tags.all()
    answers = question.answer_set.all()
    context['answers'] = paginate(answers, request, 30)
    context['question'] = question
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
