import datetime

from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

from shelf.models import game_platforms, game_statuses, game_ratings

class GameForm(forms.Form):
    title = forms.CharField(max_length=200)
    release_date = forms.DateField(
        initial=datetime.date.today,
        required=False,
        widget=DatePickerInput(options={"format": "DD/MM/YYYY", "showClear": True})
    )
    platform = forms.ChoiceField(choices=game_platforms)
    status = forms.ChoiceField(choices=game_statuses)
    rating = forms.ChoiceField(choices=game_ratings)

    def __init__(self, *args, **kwargs):
        disable_title = kwargs.pop("disable_title", None)
        super(GameForm, self).__init__(*args, **kwargs)

        if disable_title:
            self.fields["title"].disabled = True
