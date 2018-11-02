# -*- coding: UTF-8 -*-
from flask_wtf import Form
from wtforms import *
from wtforms.validators import DataRequired

class UserForm(Form):
    user = RadioField(
        label='用户类型',
        choices=((1, '学生'), (2, '教师')),
        coerce=int,
        default = 1
    )
    phonenumber = StringField(
        label = '手机号码',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    username = StringField(
        label = '用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    password = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )


class ClassForm(Form):
    vid = StringField(
        label = '直播流VID',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    teacher = StringField(
        label = '教师用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    title = StringField(
        label = '教室标题',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    thumbnail = StringField(
        label = '教室缩略图',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    password = PasswordField(
        label='教室密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
    url = StringField(
        label = '教室Url',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    visible = RadioField(
        label='是否可见',
        choices=(('yes', '是'), ('no', '否')),
        coerce=str,
        default = 'yes'
    )
    mode = RadioField(
        label='私密模式',
        choices=(('private', '私密'), ('protected', '密码进入'), ('public', '公开')),
        coerce=str,
        default = 'private'
    )
