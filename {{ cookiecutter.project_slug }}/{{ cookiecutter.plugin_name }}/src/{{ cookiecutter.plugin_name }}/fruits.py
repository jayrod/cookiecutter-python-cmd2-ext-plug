from cmd2 import CommandSet, with_default_category, Statement
from {{ cookiecutter.base_app }}.common.base_plugin import BaseCommandSet

@with_default_category('Fruits')
class LoadableFruits(CommandSet, BaseCommandSet):
    def __init__(self):
        super().__init__()


    def do_apple(self, _: Statement):
        spec_setting = self._cmd.special_setting
        self._cmd.poutput('Apple')
        self._cmd.poutput(f'Special setting : {spec_setting}')

    def do_banana(self, _: Statement):
        self._cmd.poutput('Banana')

    def do_really_like_apples(self, _:Statement):
        apple_setting = self._cmd.config['apple'].getboolean('like')

        if apple_setting:
            self._cmd.poutput('I really, really Like apples')
        else:
            self._cmd.poutput('I really, really do not Like apples')

        
