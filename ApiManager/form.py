# from django import forms
# from captcha.fields import CaptchaField
#
#
# class RegisterForm(forms.Form):
#     # 不能为空
#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, min_length=6, max_length=20)
#     # 出错信息
#     captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})