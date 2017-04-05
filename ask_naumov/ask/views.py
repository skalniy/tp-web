from django.shortcuts import render

context = {
  'questions' : [" "] * 20,
  'answers' : [" "] * 20,
  'qtags' : [" "] * 3,
  'toptags' : [" "] * 20,
  'topusers' : [" "] * 10,
}

# Create your views here.
def index(request):
    return render(request, './index.html', context)
