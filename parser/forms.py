from  django import forms
from . import parser , models


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('games', 'games'),   
    )

    media_type = forms.CharField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type'
        ]
    
    def parse_data(self):
        if self.data['media_type'] == 'games':
            game_data = parser.parser()
            for i in game_data:
                models.Game.objects.create(**i)
        



