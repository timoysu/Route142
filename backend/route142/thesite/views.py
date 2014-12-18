import json

from django.http import HttpResponse
from django.views.generic import TemplateView, View

from models import Point
from graph.graph import Graph


class IndexView(TemplateView):
    template_name = 'index.html'


class InfoQueryView(View):

    def get(self, *args, **kwargs):
        query = self.request.GET['query']
        results = Point.objects.filter(name__icontains=query)
        results_list = []
        for result in results:
            result_json = {}
            result_json['type'] = result.typ
            result_json['coordinates'] = [result.lat, result.lon]
            result_json['name'] = result.name
            results_list.append(result_json)
        return HttpResponse(json.dumps(results_list))


class NearPointsView(View):

    def get(self, *args, **kwargs):
        data = json.loads(self.request.GET['data'])
        nw = data['northwest']
        se = data['southeast']
        points = Point.objects.filter(
            lat__lte=nw[0], lat__gte=se[0], lon__gte=nw[1], lon__lte=se[1],
            is_landmark=True).\
            all()
        results_list = []
        for p in points:
            point = {'coordinates': [p.lat, p.lon], 'name': p.name,
                     'type': p.typ, 'is_landmark': p.is_landmark}
            results_list.append(point)
        return HttpResponse(json.dumps(results_list))


class GetPathView(View):

    def get(self, *args, **kwargs):
        source_id = self.request.GET['source']
        dest_id = self.request.GET['destination']
        g = Graph.get_instance()
        path = g.get_path(source_id, destination_id).path
        results_list = []
        if len(path) > 1:
            s = Point.objects.get(pk=path[0].id)
            index = 1
            while index < len(path) - 1:
                pass

    def parse_point(self, point):
        data = {
            'type': point.typ,
            'coordinates': [point.lat, point.lon],
            'name': point.name,
        }
        return data

    def parse_edge(self, source, dest):
        data = {
            'type': 'road',
            'start': [source.lat, source.lon], 
            'end': [dest.lat, dest.lon],
            traffic: 'light'
        }
        return data

