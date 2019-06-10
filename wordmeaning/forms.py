from django import forms
from . models import Word

class WordForm(forms.ModelForm):
	class Meta:
		model = Word
		fields = ('your_word','meaning','make_sentence',)
		widgets = {
					'your_word': forms.TextInput(attrs={'class' : 'textarea','placeholder':'Word'}),
					'meaning': forms.TextInput(attrs={'class':'textarea','placeholder':'Place the Meaning'}),
					'make_sentence': forms.Textarea(attrs={'class' : 'textarea','placeholder':'Place your sentence'})

		}
	# def __init__(self,*args,**kwargs):
	# 	super().__init__(*args,**kwargs)
	# 	self.fields['your_word'].widget.attrs.update()
	# 	self.fields['meaning'].widget.attrs.update()
	# 	self.fields['make_sentence'].widget.attrs.update({'class':'textarea','placeholder':'write a sentence'})

