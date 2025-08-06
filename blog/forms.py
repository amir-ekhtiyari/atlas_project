# forms.py
from django import forms
from django.core.validators import RegexValidator
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=11,
        required=True,
        label='شماره موبایل',
        validators=[
            RegexValidator(regex=r'^09\d{9}$', message='شماره موبایل باید با 09 شروع شود و 11 رقم باشد.')
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'مثلاً: 09123456789'
        })
    )

    SUBJECT_CHOICES = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش', 'گزارش'),
    )

    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        label='موضوع پیام',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'نام کامل',
            'email': 'ایمیل',
            'message': 'متن پیام'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خود را وارد کنید'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'پیام خود را وارد کنید...',
                'rows': 5
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        return phone  # می‌تونی اینجا لاگ بگیری یا کاری انجام بدی
