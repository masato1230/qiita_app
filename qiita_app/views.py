from django.shortcuts import render, redirect
from datetime import date
import requests
from collections import Counter
from .models import Result



def home(request):
  results = Result.objects.filter(date__date=date.today())[:10]
  logos = ["Python", "Ruby", "AWS", "CSS", "Rails", "JavaScript", "Docker", "PHP", "Laravel", "Swift", "MySQL", "Java", "Git", "HTML"]
  exist_logos = []

  # logo画像があるプログラミング言語をexist_logosに追加
  print(results)
  for result in results:
    print(result.key)
    print(result.value)
    if result.key in logos:
      exist_logos.append(result.key)
    # 最終更新日時の取得
    updated_date = result.date

  context = {
    'results': results,
    'exist_logos': exist_logos,
    'updated_date': updated_date,
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
              print(tag['name'])
  print(Counter(tag_list))
  results = Counter(tag_list).most_common(10)
  print(len(tag_list))
  print(res[1]['created_at'])
  print(res[-1]['created_at'])


  for result in results:
    print(result)
    result = Result(key=result[0], value=result[1])
    result.save()
    
  return redirect(home)
