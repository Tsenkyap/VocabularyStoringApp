from django.shortcuts import render,redirect
from . models import Word
from .forms import WordForm
from django.contrib import messages

def main(request):
	all_word = Word.objects.all()
	return render(request, 
				  'wordmeaning/home.html',
				  {'all_word':all_word})

def entries(request):
	if request.method == 'POST':
		wording = WordForm(request.POST)
		if wording.is_valid():
			wording.save()
			return redirect('main')
	else:
		wording = WordForm()
	
	context = {'wording' :wording}
	return render(request,'wordmeaning/word-form.html',context)





