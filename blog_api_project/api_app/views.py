from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  
from .models import Item
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import Item

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer






@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        file_upload = request.FILES.get('file_upload')

        item = Item(name=name, description=description, file_upload=file_upload)
        try:
            item.full_clean()
            item.save()
            return JsonResponse({"success": "Item created successfully"})
        except ValidationError as e:
            return JsonResponse({"err": str(e)}, status=400) 
    else:
        return JsonResponse({"err": "Invalid request method"}, status=405)


