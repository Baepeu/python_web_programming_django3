from django import forms

class AddCouponForm(forms.Form):
    code = forms.CharField(label='Your Coupon Code')