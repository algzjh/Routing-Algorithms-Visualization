"""
视图 View 是 Django 的 MTV 架构模式的 V 部分，
主要负责处理用户请求和生成相应的响应内容，
然后在页面或其他类型文档中显示。
也可以理解为视图是 MVC 架构里面的 C 部分（控制器）
主要处理功能和业务上的逻辑
数据除了接受用户请求和返回响应内容之外，
还可以与模型（Model）实现数据交互（操作数据库）。
要想将数据库的数据展现在网页上，需要由视图、模型和模板共同实现
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json
import os
from .dijkstra import getDijkstra
from .randomgraph import createRandomGraph
from random import randrange


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
        if request.is_ajax():
            if request.POST['id'] == 'requestPlot':
                data_source_name = request.POST["data_source_name"]
                print("data_source_name: \n", data_source_name)
                if data_source_name == "1":
                    createRandomGraph()
                    temp_path = "RouteVisApp1/static/RouteVisApp1/data/graph-random.json"
                else:
                    temp_path = "RouteVisApp1/static/RouteVisApp1/data/example-graph.json"
                filename = os.path.join(settings.BASE_DIR, temp_path)
                graph_data = read_json_file(filename)
                start_node = request.POST["start_node"]
                end_node = request.POST["end_node"]
                alg_name = request.POST["alg_name"]
                result = {
                    "start_node": start_node,
                    "end_node": end_node,
                    "alg_name": alg_name,
                    "graph_data": graph_data
                }
                print("result: \n", result)
                return HttpResponse(json.dumps(result))
            elif request.POST['id'] == 'requestAlg':
                data_source_name = request.POST["data_source_name"]
                print("data_source_name: \n", data_source_name)
                if data_source_name == "1":
                    temp_path = "RouteVisApp1/static/RouteVisApp1/data/graph-random.json"
                else:
                    temp_path = "RouteVisApp1/static/RouteVisApp1/data/example-graph.json"
                filename = os.path.join(settings.BASE_DIR, temp_path)
                graph_data = read_json_file(filename)
                start_node = request.POST["start_node"]
                end_node = request.POST["end_node"]
                alg_name = request.POST["alg_name"]
                if alg_name == "0":
                    alg_result, add_list = getDijkstra(graph_data, start_node, end_node)
                    result = {
                        "alg_result": alg_result,
                        "add_list": add_list
                    }
                    print("dij-result: \n", result)
                    return HttpResponse(json.dumps(result))
        return HttpResponse(json.dumps({"message": "error"}))
    return render(request, 'RouteVisApp1/index.html')
