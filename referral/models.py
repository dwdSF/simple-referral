from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserReferral(models.Model):
    ''' A model that implements a referral system '''

    referrer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='referred'  # люди которых пригласил
    )
    referred = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='referrer'   # кто пригласил
    )

    def __str__(self):
        return f'{self.referrer} пригласил {self.referred}'

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'referrals'
        unique_together = (('referrer', 'referred'),)
