from cliez.component import Component


class DemoComponent(Component):
    # un-comment this can disable global options
    # exclude_global_option = True

    def run(self, options):
        self.print_message('database config is %s' % self.settings.DATABASE)
        pass

    @classmethod
    def add_arguments(cls):
        """
        sub parser document
        """
        return [
            (('hello',), dict(help='require argument')),
            (('world',),
             dict(nargs='?', default='world', help='optional argument')),
            (('--bool',), dict(action='store_true', help='a bool value.')),
        ]
        pass

    pass
