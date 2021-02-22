from {{ cookiecutter.base_app }}.common.command_set_settables import BaseSettables
from cmd2 import Cmd, Settable

class SettingCollisionError(Exception):
    """Raised when there is a setting collision"""
    ...


class ProduceSettables(BaseSettables):
    """ Defines settings required for Produce plugin """
    _name_ = 'ProduceSettable'
    _version_ = '0.1.0'

    def set(self, app: Cmd):
        """ Adds settings to cmd2 application"""

        #make sure there is not a setting collision
        if hasattr(app, 'special_setting'):
            raise SettingCollisionError

        app.special_setting = 33
        app.add_settable(Settable('special_setting', int, 
            'Special Setting'))
