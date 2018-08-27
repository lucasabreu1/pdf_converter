from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.core.files.storage import FileSystemStorage
from wand.image import Image
from django.conf import settings
import os
import time
import subprocess

#DESCOBRIR ONDE O WAND SALVA AS IMAGENS
def upload_pdf(request):
	if request.method == 'POST':
		file = request.FILES['myfile']
		s1,s2 = file.name.split('.')
		new_name=s1+'.jpg'

		buf = file.read()

		img = Image(blob=buf, resolution=200)

		img.format = 'jpeg'

		response = HttpResponse(img.make_blob(), content_type="application/jpeg")
		response['Content-Disposition'] = 'attachment; filename="{}"'.format(new_name)

		return response

	return render(request, 'converter/index.html')
