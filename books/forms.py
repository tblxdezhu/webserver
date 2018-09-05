#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04/09/2018 4:35 PM
# @Author  : Zhenxuan Xu
# @File    : forms.py
# @Software: Pycharm professional

from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='', max_length='20', widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Password', 'class': 'form-control'}))
