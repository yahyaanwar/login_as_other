from odoo import http, tools
from odoo.http import request
from odoo.service import security
from odoo.addons.web.controllers import home


class UserSwitcher(home.Home):
    @http.route('/web/switch-user', type='http', auth='user', sitemap=False)
    def switch_to_user(self, user_id):
        mode = tools.config.misc.get('login_as_other', {}).get('switch_mode')
        uid = request.env.user.id
        if mode and (request.env.user._is_system() or mode == 'sudo'):
            uid = request.session.uid = int(user_id)
            # invalidate session token cache as we've changed the uid
            request.env['res.users'].clear_caches()
            request.session.session_token = security.compute_session_token(request.session, request.env)

        return request.redirect(self._login_redirect(uid))
