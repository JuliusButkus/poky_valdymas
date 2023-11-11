from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


User = get_user_model()

class News(models.Model):
    name = models.CharField(_('name in English language'), max_length=100)
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name=_("news"),
    )
    
    class Meta:
        verbose_name = _("type")
        verbose_name_plural = _("types")

    def __str__(self):
        return self.name_en

    def get_absolute_url(self):
        return reverse("type_detail", kwargs={"pk": self.pk})
