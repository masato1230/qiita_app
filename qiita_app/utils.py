import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from .models import ResultLonger

def get_graph(request):
  graph = plt.figure()
  results = ResultLonger.objects.all().order_by("-id")[86:100]
  x = []
  y = []
  for result in results:
    print(result.key)
    print(result.value)
    x.append(result.key)
    y.append(result.value)
  plt.rcParams["font.size"] = 6
  plt.bar(x,y)
  graph.savefig("img.png")
  
  return graph
