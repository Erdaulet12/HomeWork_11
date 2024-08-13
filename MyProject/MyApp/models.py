from django.db import models


class SMS(models.Model):
	sender = models.CharField(max_length=100)
	receiver = models.CharField(max_length=100)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"SMS from {self.sender} to {self.receiver} at {self.timestamp}"
