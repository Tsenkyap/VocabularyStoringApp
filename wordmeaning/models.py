from django.db import models
from datetime import datetime

class Word(models.Model):
	your_word = models.CharField(max_length=200)
	meaning = models.TextField()
	make_sentence = models.TextField()
	word_added = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.your_word

