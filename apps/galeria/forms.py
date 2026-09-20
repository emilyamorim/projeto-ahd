from django import forms
from .models import Album

class UploadFotoForm(forms.Form):
    album = forms.ModelChoiceField(
        queryset=Album.objects.none(),
        required=False,
        label="Álbum de destino",
        empty_label="selecione um álbum",
    )

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        if usuario is not None:
            self.fields["album"].queryset = Album.objects.filter(usuario=usuario)