from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class Word(models.Model):
	added_by = models.ForeignKey(User,null=1,on_delete=models.CASCADE)
	your_word = models.CharField(max_length=200)
	meaning = models.TextField()
	make_sentence = models.TextField()
	word_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.your_word

