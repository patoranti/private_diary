from django import  forms

#formsクラスを継承
class InquiryForm(forms.Form):
    name = forms.CharField(label='名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名',max_length=30)
    message = forms.CharField(label='本文',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージを入力してください'