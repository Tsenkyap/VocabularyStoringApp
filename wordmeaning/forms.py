from django.forms import ModelForm
from . models import Word

class WordForm(ModelForm):
	class Meta:
		model = Word
		fields = ('your_word','meaning','make_sentence' ,'word_added',)

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['your_word'].widget.attrs.update({'class' : 'textarea','placeholder':'word'})
		self.fields['meaning'].widget.attrs.update({'class':'textarea','placeholder':'write a meaning'})
		self.fields['make_sentence'].widget.attrs.update({'class':'textarea','placeholder':'write a sentence'})

