from django.shortcuts import render,redirect,get_object_or_404
from . models import Word
from .forms import WordForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required



def main(request):
	all_word = Word.objects.all().order_by('-word_added')
	return render(request, 
				  'wordmeaning/home.html',
				  {'all_word':all_word})
@login_required()
def entries(request):
	if request.method == 'POST':
		wording = WordForm(request.POST)
		if wording.is_valid():
			word = wording.save(commit=False)
			print(word.added_by)
			word.added_by = request.user
			word.save()
			messages.success(request,'Successfully added')
			return redirect('wordmeaning:main')
	else:
		wording = WordForm()
	
	context = {'wording' :wording}
	return render(request,'wordmeaning/word-form.html',context)

def username_check(user):
    return user.username

@user_passes_test(username_check)
@login_required()
def update_entries(request,pk):
	obj_instance = get_object_or_404(Word,pk=pk)
	if request.method == 'POST':
		form = WordForm(request.POST or None,instance=obj_instance)
		if form.is_valid():
			form.save()
			messages.success(request,'Updated Successfully')
			return redirect('wordmeaning:main')
	else:
		form = WordForm(instance=obj_instance)
	context = {'form': form}
	return render(request,'wordmeaning/update_form.html',context)

@user_passes_test(username_check)
@login_required()
def delete_entries(request,pk):
	obj_instance = get_object_or_404(Word,pk=pk)
	if request.method == 'POST':
		obj_instance.delete()
		messages.error(request,'Deleted Successfully')
		return redirect('wordmeaning:main')
	context = {'obj_instance': obj_instance}
	return render(request,'wordmeaning/delete_form.html',context)






