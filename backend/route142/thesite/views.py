import json

from django.http import HttpResponse
from django.views.generic import TemplateView, View

from models import Point

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