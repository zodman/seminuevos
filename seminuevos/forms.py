# -*- coding: utf-8 -*-
__author__ = 'sergio'
import logging
from django import forms
from .models import SemiAccount

logger = logging.getLogger(__name__)





class SemiAccountForm(forms.ModelForm):
    class Meta:
        model = SemiAccount
        fields = ['dealer_id', 'dealer_user_id' ]



