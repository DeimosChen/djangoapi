from . import models
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError


class UserSerializer(ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = models.User
        fields = ('username', 'password', 'id')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        # 获取用户对象
        user = self._login_validation(attrs)
        # 签发token
        token = self._get_token(user)
        self.context['token'] = token
        self.context['username'] = user.username
        self.context['login_type'] = self.login_type

        return attrs

    def _login_validation(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        import re
        # 校验用户名是否存在
        if re.match('^1[3-9][0-9]{9}$', username):
            user = models.User.objects.filter(phone=username).first()
            login_type = 0
        elif re.match('.+@.+', username):
            user = models.User.objects.filter(email=username).first()
            login_type = 1
        else:
            user = models.User.objects.filter(username=username).first()
            login_type = 2
        # 校验密码
        if user:
            ret = user.check_password(password)
            if ret:
                self.login_type = login_type
                return user
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户名不存在')

    def _get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
        payload = jwt_payload_handler(user)
        # 获取payload
        token = jwt_encode_handler(payload)
        # 获取token
        return token
