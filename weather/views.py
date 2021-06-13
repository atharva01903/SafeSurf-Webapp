from django.shortcuts import render
import config
import requests
import pandas as pd
def index(request):
	if ('lat' in request.GET and 'lon' in request.GET):
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		api_key = "2027dab46bade426aaa9c65317f55026"
		lat = request.GET['lat']
		lon = request.GET['lon']
		complete_url=base_url+"lat="
		complete_url= complete_url+lat[1:]+"&lon="
		complete_url= complete_url+lon
		complete_url= complete_url[:-1]+"&appid="+config.api_key
		response = requests.get(complete_url)
		x = response.json()
		isNotABeach=False
		isUnsafe=False
		isPartlySafe=False
		weather=x['weather'][0]['id']
		if (x['main']['grnd_level']<1005):
			isNotABeach=True
		if(weather>800):
			isPartlySafe=True
		if(weather>=200 and weather<=500):
			isUnsafe=True
		context = {
			'weather_id':weather,
			'is_not_a_beach':isNotABeach,
			'is_unsafe':isUnsafe,
			'is_partly_safe':isPartlySafe,
			'google_api':config.API_KEY
		}
	else:
		context = {
			'google_api':config.API_KEY
		}
	return render(request, 'index.html', context)
