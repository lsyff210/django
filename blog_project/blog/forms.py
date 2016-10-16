# coding:utf-8
from django import forms
from models import Comment
from django.core.validators import ValidationError


class RegForm(forms.Form):
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
                               max_length=50, error_messages={"required": "username不能为空",})
    email = forms.EmailField(label='邮箱',
                             widget=forms.TextInput(attrs={"placeholder": "邮箱", "required": "required",}),
                             max_length=50, error_messages={"required": "email不能为空",})
    url = forms.URLField(label='个人网址', widget=forms.TextInput(attrs={"placeholder": "个人网址",}, ),
                         max_length=100, required=False, error_messages={"required": "请输入一个有效的网址",})

    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={"placeholder": "请输入密码", "required": "required",}),
                               max_length=20, min_length=6,
                               error_messages={"required": "password不能为空", 'min_length': '密码最少6位',}, )
    password1 = forms.CharField(label='重新输入密码',
                                widget=forms.PasswordInput(attrs={"placeholder": "请再次输入密码", "required": "required",}),
                                max_length=20, min_length=6,
                                error_messages={"required": "password不能为空", 'min_length': '密码最少6位',
                                                'clean': '您输入的密码不一致'}, )

    def clean(self):
        print 'clean_password'
        password_2 = self.cleaned_data['password1']
        password_1 = self.cleaned_data['password']
        if password_1 and password_2 and password_2 != password_1:
            raise forms.ValidationError('您输入的密码不一致')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
                               error_messages={"required": "用户名不能为空"},
                               max_length=50,
                               )

    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "请输入密码", "required": "required",}),
                               error_messages={"required": "password不能为空", 'min_length': '密码最少为6位'},
                               max_length=20, min_length=6, )


class CommentForm(forms.Form):
    username = forms.CharField(
        label='作者（必填）',
        widget=forms.TextInput(attrs={'name': "author", 'id': "author", 'size': "25", 'tabindex': "1",
                                      'class': "comment_input", "required": "required",}),
        error_messages={"required": "用户名不能为空"},
        max_length=50, required=False,
    )

    email = forms.EmailField(
        label='邮箱（必填）',
        widget=forms.TextInput(attrs={'name': "email", 'id': "author", 'size': "25", 'tabindex': "2",
                                      'class': "comment_input", "required": "required",}),
        error_messages={"required": "邮箱不能为空"},
        max_length=50, required=False,
    )
    url = forms.URLField(
        label='个人网址',
        widget=forms.TextInput(attrs={'name': "url", 'id': "url", 'size': "25", 'tabindex': "3",
                                      'class': "comment_input",}),
        error_messages={},
        max_length=50, required=False,
    )
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'name': "comment", 'id': "comment", 'cols': "25", 'rows': '5', 'tabindex': "4",
                                     'class': "message_input", "required": "required"}),
        error_messages={"required": "评论内容不能为空"},
        max_length=1000,
    )
    article = forms.CharField(
        label='',
        widget=forms.HiddenInput(attrs={'name': "article", 'id': "article", 'class': "comment_input",
                                        "required": "required"}),
        error_messages={"required": ""},
        max_length=10,
    )
    pid = forms.CharField(
        label='父级评论',
        widget=forms.HiddenInput(attrs={'name': "pid", 'id': "pid", 'class': "comment_input",}),
        error_messages={},
        max_length=10, required=False,
    )
    rid = forms.CharField(
        label='回复',
        widget=forms.HiddenInput(attrs={'name': "rid", 'id': "rid", 'class': "comment_input",}),
        error_messages={},
        max_length=10, required=False,
    )
