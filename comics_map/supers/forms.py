from django.forms import ModelForm
from .models import Super, IRLCity, Universe

class AddSuperForm(ModelForm):
	class Meta:
		model = Super
		fields = ('name', 'identity', 'origin_city', 'origin_state', 'irl_city', 'first_appearance', 'company_universe', 'description')
		labels = {
			'name': 'Superhero Name',
			'identity': 'Identity',
			'origin_city': 'Origin City',
			'origin_state': 'Origin State',
			'irl_city': 'Real Life City',
			'first_appearance': 'Date of First Appearance',
			'company_universe': 'Company/Universe',
			'description': 'Description',
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