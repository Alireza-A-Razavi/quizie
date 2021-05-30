from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class Test(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=225)
	timestamp = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(blank=True, null=True)
	is_closed = models.BooleanField(default=False)
	show = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name, allow_unicode=True)
		super(Test, self).save(*args, **kwargs)




class Question(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	question = models.CharField(max_length=225)
	help_text = models.CharField(max_length=225, null=True, blank=True)
	show = models.BooleanField(default=True)




class TestAnswer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	test = models.ForeignKey("Test", on_delete=models.CASCADE)
	answers = models.ManyToManyField("Answer")
	timestamp = models.DateTimeField(auto_now_add=True)
	show = models.BooleanField(default=True)




class Answer(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey("Question", on_delete=models.CASCADE)
	show = models.BooleanField(default=True)

