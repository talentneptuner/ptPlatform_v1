from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户资料'

    def __str__(self):
        return self.username

    def get_data_for_label(self):
        return self.labelrecord_set.filter(has_done=False).values_list('id')

    def get_unlabeled_data_count(self):
        return self.labelrecord_set.filter(has_done=False).count()

    def get_labeled_data_count(self):
        return self.labelrecord_set.exclude(has_done=False).count()