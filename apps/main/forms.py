# -*- coding: utf-8 -*-
from django import forms

class NumberInput(forms.widgets.TextInput):
        input_type = 'number'

class RangeInput(forms.widgets.TextInput):
    input_type = 'range'
