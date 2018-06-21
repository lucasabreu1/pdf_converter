from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.core.files.storage import FileSystemStorage
from wand.image import Image
from django.conf import settings

import ipdb; ipdb.set_trace()
#DESCOBRIR ONDE O WAND SALVA AS IMAGENS
def upload_pdf(request):
	if request.method == 'POST':
		file = request.FILES['myfile']
		s1,s2 = file.name.split('.')
		new_name=s1+'.jpg'
		file.seek(0)
		with Image(file=file, resolution=300) as img:
			print("pages= ", len(img.sequence))
			with img.convert("jpg") as converted:
				global new_name
				converted.save(filename=new_name)


	return render(request, 'converter/index.html')