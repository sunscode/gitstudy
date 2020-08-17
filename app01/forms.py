from django import forms
import hashlib
from app01 import models
from django.core.exceptions import ValidationError


class RegForm(forms.ModelForm):
    # username = forms.CharField()
    password = forms.CharField(error_messages={'required': '这是必填项'},
                               widget=forms.PasswordInput(attrs={'placeholder': '密码', 'type': 'password'}), label='密码',
                               min_length=6)
    re_pwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '确认密码', 'type': 'password'}),
                             label='确认密码', min_length=6)

    class Meta:  # Meta只针对默认生成的字段是有效的  而对于自己手动生成的字段无效 如在下面的error_message写下password，是无法生效的
        model = models.User  # 注意 这里是model 而不是models
        fields = '__all__'  # 这里意思就是指定所有的字段
        exclude = ['last_time']  # 这个一般和__all__一起用，表示除了哪些是不用填写进去的
        # fields = ['username', 'password']  # 这里指定了是哪几个  到时候就会对应的生成哪几个
        widgets = {
            'password': forms.PasswordInput,
            'username': forms.TextInput(attrs={'placeholder': '用户名', 'autocomplete': 'off'}),  # autocomplete的作用就是自动填充内容
            'position': forms.TextInput(attrs={'placeholder': '职位'}),
            # 'company': forms.Select(attrs={'placeholder': '公司'}),
            'phone': forms.TextInput(attrs={'placeholder': '手机号'}),
        }
        error_messages = {
            'username': {
                'required': '必填项',
            },
        }

    def clean_phone(self):  # 加上局部钩子
        import re
        phone = self.cleaned_data.get('phone')
        if re.match(r'^1[3-9]\d{9}$', phone):
            return phone
        raise ValidationError('手机号格式不正确')

    def clean(self):  # 加上全局钩子
        self._validate_unique = True  # 加上 数据库要去校验唯一  就不会在数据库层面来报错了
        password = self.cleaned_data.get('password', '')  # 这里给个空字符串为了防止不输入 两个都是null 出问题 用空字符串和null就会不一样
        re_pwd = self.cleaned_data.get('re_pwd')

        if password == re_pwd:
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            # print(md5.hexdigest)
            self.cleaned_data['password'] = md5.hexdigest()
            return self.cleaned_data
        self.add_error('re_pwd', '两次密码不一致')
        return ValidationError('两次密码不一致')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义的操作
        field = self.fields['company']

        choices = field.choices
        choices[0] = ('', '选择公司')
        field.choices = choices


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = "__all__"
        exclude = ['detail']

        # 加上下面的这个作用就是让你自己的css生效，而不仅仅是显示原来的那种
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


