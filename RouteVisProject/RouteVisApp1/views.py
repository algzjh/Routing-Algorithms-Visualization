from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json
import os


def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


# Create your views here.
def index(request):
    temp_path = "RouteVisApp1/static/RouteVisApp1/data/example-graph.json"
    filename = os.path.join(settings.BASE_DIR, temp_path)
    temp_graph_data = read_json_file(filename)
    print(temp_graph_data)
    # render(request, template_name, context=None, content_type=None, status=None, using=None)
    # request: 浏览器向服务器发送的请求对象，包含用户信息、请求内容和请求方式
    # template_name：HTML模板文件名，用于生成HTML网页
    # context： 对HTML模板的变量赋值，以字典格式表示
    # content_type：响应数据的数据格式，一般使用默认值
    # status：HTTP状态码，默认为200
    # using：设置HTML模板转换生成HTML网页的模板引擎
    if request.method == 'POST':
        if request.is_ajax() and request.POST['id'] == 'requestPlot':
            temp_path = "RouteVisApp1/static/RouteVisApp1/data/example-graph.json"
            filename = os.path.join(settings.BASE_DIR, temp_path)
            graph_data = read_json_file(filename)
            start_node = request.POST["start_node"]
            end_node = request.POST["end_node"]
            result = {
                "start_node": start_node,
                "end_node": end_node,
                "graph_data": graph_data
            }
            print("result: \n", result)
            return HttpResponse(json.dumps(result))
        return HttpResponse(json.dumps({"message": "error"}))
    return render(request, 'RouteVisApp1/index.html')
