from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

def home(request):
    return HttpResponse("Bine ai venit la Proiectul Meu Django!")

def get_data(request):
    response = requests.get('https://api.agify.io/?name=michael')
    data = response.json()
    return JsonResponse(data)

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payload = {'name': name}
        response = requests.post('https://api.agify.io/', data=payload)
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=400)
