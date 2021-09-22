from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

from django.contrib.auth.models import User

class UserAddWindow(BaseEditWindow):
    def _init_components(self):
        super()._init_components()

        self.field__last_login = ext.ExtDateField(
            label=u'Был последний раз',
            name='last_login',
            allow_blank=True,
            anchor='100%')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Суперпользователь',
            name='is_superuser'
        )

        self.field__username = ext.ExtStringField(
            label=u'Логин',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=True,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=True,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'Email',
            name='email',
            allow_blank=True,
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'В штате',
            name='is_staff'
        )

        self.field__is_active = ext.ExtCheckBox(
            label=u'Активен',
            name='is_active'
        )

        self.field__date_joined = ext.ExtDateField(
            label=u'Дата регистрации',
            name='date_joined',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super()._do_layout()
        self.form.items.extend((
            self.field__last_login,
            self.field__is_superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super().set_params(params)
        self.height = 'auto'

