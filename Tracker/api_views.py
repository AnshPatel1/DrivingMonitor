from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import  json

from Tracker.models import TrackerNode


class TrackerEndpointSet:
    @staticmethod
    @require_POST
    @csrf_exempt
    def post_current_location(request, node_id):
        data = json.loads(request.body.decode("utf-8"))
        node = TrackerNode.objects.get(id=node_id)

    @staticmethod
    @require_POST
    def post_trip_event(request, node_id):
        pass
