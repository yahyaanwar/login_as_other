{
    'name': 'Login As Other',
    'description': 'Switch to other user.',
    'category': 'Extra Rights',
    'website': 'yahyaanwar.github.io',
    'support': 'k3ic8zwya@mozmail.com',
    'version': '1.0',
    'license': 'OPL-1',
    'price': 0, 'currency': 'USD',
    'author': 'Yahya Anwar Ramadhan',
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': [
        'base',
    ],
    'external_dependencies': {
        'python': [
        ],
        'bin': [
        ],
    },
    'data': [
    ],
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [
            '/login_as_other/static/src/components/user_switcher.scss',
            '/login_as_other/static/src/components/user_switcher.js',
            '/login_as_other/static/src/components/user_switcher.xml',
        ],
    },
    'images': [
    ],
    'post_load': 'apply_patch',
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
}