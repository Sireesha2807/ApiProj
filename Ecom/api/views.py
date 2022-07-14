from rest_framework.response import Response # for json response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getdata(request):
    person = {'name':'siri','age':'25'}
    return Response(person)