import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from .models import ResultLonger
import base64
import io

def create_graph(request):
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
  
def get_graph():
  buffer = io.BytesIO()
  plt.savefig(buffer, format='png', dpi=500)
  image_png = buffer.getvalue()
  graph = base64.b64encode(image_png)
  graph = graph.decode('utf-8')
  buffer.close()
  return graph