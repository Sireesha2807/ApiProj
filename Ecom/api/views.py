from rest_framework.response import Response # for json response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import Itemserializer


@api_view(['GET'])
def getdata(request):
    items = Item.objects.all()
    serializer = Itemserializer(items, many=True)
    return Response(serializer.data)


