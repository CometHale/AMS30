from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Super, IRLCity, Universe
from .forms import AddSuperForm, AddIRLCityForm, AddUniverseForm
from django.contrib import messages
import pyexcel as excel
import pyexcel.ext.xlsx

def super_exist(possible_super_name):
		exist = False
		supers = Super.objects.all()
		for sup in supers: 
			if sup.name == possible_super_name:
				exist = True
				return exist
		return exist

def irl_city_exist(possible_city_name):
	exist = False
	cities = IRLCity.objects.all()
	for city in cities:
		if city.name == possible_city_name:
			exist = True
			return exist
	return exist

def universe_exist(possible_bang_name):
	exist = False
	universes = Universe.objects.all()
	for universe in universes: 
		if universe.company_name == possible_bang_name:
			exist = True
			return exist
	return exist

def index(request):
	input_from_excel()
	supers_list = Super.objects.order_by('-name')[:5]
	template = loader.get_template('supers/index.html')
	context = {
		'supers_list':supers_list,
	}

	return HttpResponse(template.render(context,request))

def detail(request, super_id):
	cur_super = Super.objects.get(id=super_id)
	template = loader.get_template('supers/detail.html')
	context = {
		'cur_super': cur_super,
	}
	return HttpResponse(template.render(context,request))

def add_super(request):
	in_db = False

	if request.method == 'POST':
		form = AddSuperForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['super_name']
			supers = Super.objects.all()
			for sup in supers:
				if name == sup.name:
					error = "Superhero already registered!"
					messages.error(request,error)
					in_db = True

			if not in_db:
				ident  = form.cleaned_data['identity']
				orig_city = form.cleaned_data['orig_city']
				orig_state = form.cleaned_data['orig_state']
				irl_cit = form.cleaned_data['irl_cit']
				first_ap = form.cleaned_data['first_appearance']
				comp = form.cleaned_data['company_universe']
				desc = form.cleaned_data['description']

				new_super = Super.objects.create(name=name, identity=identity, origin_city=orig_city, 
					origin_state=orig_state, irl_city=irl_cit, first_appearance=first_ap, company_universe=comp, description=desc)
				new_super.save()

				success = "%s has joined the ranks of the Super Coalition!" %(name)
				messages.success(request, success)

				template = loader.get_template('supers/detail.html')
				context = {
					'cur_super': new_super
				}
				return HttpResponseRedirect(template)
		# else:
	form = AddSuperForm()
	return render(request, 'supers/add_super.html', {'form': form})

def add_irl_city(request):
	in_db = False

	if request.method == 'POST':
		form = AddIRLCityForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			cities = IRLCity.objects.all()
			for city in cities: 
				if city.name == name:
					error = "City already mapped!"
					messages.error(request,error)
					in_db = True
			if not in_db:
				province = form.cleaned_data['province']
				longitude = form.cleaned_data['longitude']
				latitude = form.cleaned_data['latitude']
				new_city = IRLCity.objects.create(name=name, province=province, latitude= latitude, longitude=longitude)
				new_city.save()

				success = " City successfully mapped!"
				messages.success(request, success)
				return HttpResponseRedirect('supers/index.html') # have this redirect to whatever page was previously seen i.e. index or 
				#Add Super form depending
	form = AddIRLCityForm()
	return render(request, 'supers/add_city.html', {'form':form})

def big_bang(request):
	in_db = False

	if request.method == 'POST':
		form.AddUniverseForm(request.POST)
		if form.is_valid():
			company_name = form.cleaned_data['company_name']
			universes = Universe.objects.all()
			for universe in universes:
				if universe.company_name == company_name:
					error = "Universe already in the Multiverse!"
					messages.error(request, error)
					in_db = True
			if not in_db:
				origin_country = form.cleaned_data['origin_country']
				big_bang = Universe.objects.create(company_name=company_name, origin_country=origin_country)

				big_bang.save()
				success = "A Big Bang has occurred--- new Universe created!"
				messages.success(request, success)
				return HttpResponseRedirect('supers/index.html')# have this redirect to whatever page was previously seen i.e. index or 
				#Add Super form depending
	form = AddUniverseForm()
	return render(request, 'supers/big_bang.html', {'form':form})

def input_from_excel():
	input_sheet = excel.get_sheet(file_name="supers_data.xlsx", name_columns_by_row=0)
	records = excel.to_array(input_sheet.rows())
	for record in records:
		if not irl_city_exist(record[3]) and record[5] != '' and record[6] != '':
			new_irl_city = IRLCity.objects.create(name=record[3], province=record[4], latitude=record[5] , longitude=record[6])
			new_irl_city.save()
		if not universe_exist(record[2]):
			new_bang = Universe.objects.create(company_name=record[2], origin_country=record[8])
			new_bang.save()
		if not super_exist(record[0]):
			if record[3] != '':
				city = IRLCity.objects.get(name=record[3])
				universe = Universe.objects.get(company_name=record[2])
				new_super = Super.objects.create(name=record[0],identity=record[7],origin_city=record[1],irl_city=city, company_universe=universe)
				new_super.save()
		# print "%s - %s - %s - %s - %s - %s - %s - %s - %s" %(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7])
