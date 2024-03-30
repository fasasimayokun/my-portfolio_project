from django.http import JsonResponse
import requests

def fetch_external_data(request):
    api_key = 'your-api-key'
    url = 'https://api.example.com/data'
    params = {'key': api_key, 'param1': 'value1'}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Process and integrate data with your models if needed
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch data from external API'}, status=500)