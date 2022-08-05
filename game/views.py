from django.http import HttpResponse


# Create your views here.

def index(request):
    line1 = '<h1 style="text-align: center">Hello,World</h1>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2F1114%2F022221105922%2F210222105922-7-1200.jpg&refer=http%3A%2F%2Fimg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662260247&t=9b30101fa10dea4d4fd09b6517b36eee" width=2000>'
    return HttpResponse(line1 + line2)
