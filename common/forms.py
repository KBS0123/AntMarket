from django import forms

class LoginForm(forms.Form):
	    username = forms.CharField()
	    password = forms.CharField(widget=forms.PasswordInput)
	    #widget=forms.PasswordInput -> password HTML 엘리먼트 렌더링 type="password"처리