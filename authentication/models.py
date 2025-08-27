from django.db import models
from django.contrib.auth.models import User

class AffiliateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='affiliate_profile')
    affiliate_code = models.CharField(max_length=12, unique=True)
    referred_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} ({self.affiliate_code})"

class AffiliateCommission(models.Model):
    affiliate = models.ForeignKey(AffiliateProfile, on_delete=models.CASCADE, related_name='commissions')
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='affiliate_commissions')
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=40.00)  # e.g., 10%
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Amount earned from this referral
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.affiliate.user.username} earned €{self.amount} from {self.referred_user.username} on {self.created_at.strftime('%Y-%m-%d')}"