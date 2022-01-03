from django import forms

from . import models


class Postform(forms.ModelForm):
    class Meta:
        model = models.post
        fields = ['mood' , 'nickname' , 'message' , 'del_pass']


    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.base_fields['mood'].label = '現在心情'
        self.base_fields['nickname'].label = '你的暱稱'
        self.base_fields['message'].label = '心情留言'
        self.base_fields['del_pass'].label = '設定密碼'self.base_fields['mood'].label = '現在心情'