from django.shortcuts import render, redirect
from datetime import date, datetime, timezone, timedelta
import requests
from collections import Counter
from .models import Result, ResultLonger
from . import utils



def home(request):
  results = Result.objects.all().order_by("-id")[:10]
  results_ordered = []
  updated_date = None
  for result in reversed(results):
    results_ordered.append(result)
  results = results_ordered
  logos = ["Python", "Ruby", "AWS", "CSS", "Rails", "JavaScript", "Docker", "PHP", "Laravel", "Swift", "MySQL", "Java", "Git", "HTML"]
  exist_logos = []
  need_update = False

  # logo画像があるプログラミング言語をexist_logosに追加
  for result in results:
    if result.key in logos:
      exist_logos.append(result.key)
    # 最終更新日時の取得
    updated_date = result.date

  if updated_date:
    if datetime.now(timezone.utc) - updated_date > timedelta(hours=10):
      need_update = True
  else:
    need_update = True

  context = {
    'results': results,
    'exist_logos': exist_logos,
    'updated_date': updated_date,
    'need_update': need_update,
  }
  return render(request, 'qiita_app/home.html', context)

# ランキングを更新するためのアクション
def update(request):
  PER_PAGE = "100"
  tag_list = []
  ACCESS_TOKEN = "Bearer f339bc4f73e81b17c450325c0d52c44db52f160a"

  for page in range(1, 10):
    page = str(page)
    url = "https://qiita.com/api/v2/items?page=" + page + "&per_page=" + PER_PAGE
    res = requests.get(url, headers={"Authorization": ACCESS_TOKEN}).json()
    for i in range(int(PER_PAGE)):
      tags = res[i]['tags']
      for tag in tags:
        tag_list.append(tag['name'])
  results = Counter(tag_list).most_common(10)


  for result in results:
    result = Result(key=result[0], value=result[1])
    result.save()
  
  return redirect(home)


def longer(request):
  results = ResultLonger.objects.all().order_by("-id")[:100]
  results_ordered = []
  updated_date = None
  for result in reversed(results):
    results_ordered.append(result)
  results = results_ordered
  logos = ["Python", "Ruby", "AWS", "CSS", "Rails", "JavaScript", "Docker", "PHP", "Laravel", "Swift", "MySQL", "Java", "Git", "HTML"]
  exist_logos = []
  need_update = False

  for result in results:
    if result.key in logos:
      exist_logos.append(result.key)
    # 最終更新日時の取得
    updated_date = result.date

  if updated_date:
    if datetime.now(timezone.utc) - updated_date > timedelta(hours=10):
      need_update = True
  else:
    need_update = True

  context = {
    'results': results,
    'exist_logos': exist_logos,
    'updated_date': updated_date,
    'need_update': need_update,
  }

  return render(request, 'qiita_app/longer.html', context)

# ランキングを更新するためのアクション
def longerUpdate(request):
  PER_PAGE = "30"
  tag_list = []
  ACCESS_TOKEN = "Bearer f339bc4f73e81b17c450325c0d52c44db52f160a"

  for page in range(1, 20):
    page = str(page)
    url = "https://qiita.com/api/v2/items?page=" + page + "&per_page=" + PER_PAGE
    res = requests.get(url, headers={"Authorization": ACCESS_TOKEN}).json()
    for i in range(int(PER_PAGE)):
      tags = res[i]['tags']
      for tag in tags:
        tag_list.append(tag['name'])
  results = Counter(tag_list).most_common(100)

  for result in results:
    result = ResultLonger(key=result[0], value=result[1])
    result.save()
  return redirect(longer)


def graph(request):
  utils.create_graph(request)
  graph = utils.get_graph()
  return render(request, 'qiita_app/graph.html', {'graph': graph})