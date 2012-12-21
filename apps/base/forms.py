# -*- coding: utf-8 -*-
from django import forms
from crispy_forms import layout,bootstrap,helper

class NumberInput(forms.widgets.TextInput):
        input_type = 'number'

class RangeInput(forms.widgets.TextInput):
    input_type = 'range'

class SearchInput(forms.widgets.TextInput):
    input_type = 'search'

class EmailInput(forms.widgets.TextInput):
    input_type = 'email'

class CrispyForm(forms.Form):

    copy = forms.IntegerField(
            label=u'打印份数',
            initial=1,
            required=False,
            widget=NumberInput(attrs={'min': '1', 'max': '100', 'step': '1'}),
            help_text=u'每张标签要打印的副本数目',
            )

    def __init__(self, *args, **kwargs):
        self.helper = helper.FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.html5_required = True
        self.helper.form_id = 'id_form'
        self.helper.layout = layout.Layout(
            'label',
            'text',
            'copy',
            bootstrap.FormActions(
                layout.Submit('submit', u'打印'),
                layout.Reset('reset', u'重置'),
                ),
            )
        super(CrispyForm, self).__init__(*args, **kwargs)
