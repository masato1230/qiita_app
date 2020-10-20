from django.shortcuts import render

def home(request):
  return render(request, 'qiita_app/home.html', {})