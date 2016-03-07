from django.forms import ModelForm
from .models import Super, IRLCity, Universe

class AddSuperForm(ModelForm):
	class Meta:
		model = Super
		fields = ('name', 'identity', 'origin_city','irl_city','company_universe')
		labels = {
			'name': 'Superhero Name',
			'identity': 'Identity',
			'origin_city': 'Origin City',
			'irl_city': 'Real Life City',
			'company_universe': 'Company/Universe',
		}

class AddIRLCityForm(ModelForm):
	class Meta:
		model = IRLCity
		fields = ('name', 'province', 'longitude', 'latitude')
		labels = { 
			'name': 'City Name',
			'province': 'Province/State',
			'longitude': 'Longitude',
			'latitude': 'Latitude',
		}

class AddUniverseForm(ModelForm):
	class Meta:
		model = Universe
		fields = ('company_name', 'origin_country')
		labels = {
			'company_name': 'Company',
			'origin_country': 'Company Country',
		}