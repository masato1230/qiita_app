from django.shortcuts import render
import requests
from collections import Counter



def home(request):
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
      print(res[-1]['created_at'])
  print(Counter(tag_list))
  resulut = Counter(tag_list)
  print(len(tag_list))
  
  return render(request, 'qiita_app/home.html', {'result': resulut})

  