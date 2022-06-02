from django.db import models
from Accounts.models import CustomUser


class CommentModel(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'