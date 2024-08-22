from odoo import http
from odoo.http import request

class MyModuleController(http.Controller):

    @http.route('/my_module/show_notification', type='http', auth='user')
    def show_notification(self):
        message = request.env['my.module.cron'].get_pending_tasks_message()
        if message:
            request.session['notification_message'] = message
        return request.redirect('/web')

    @http.route('/web', type='http', auth='user')
    def web(self, **kwargs):
        response = super(MyModuleController, self).web(**kwargs)
        if 'notification_message' in request.session:
            message = request.session.pop('notification_message')
            response.qcontext['notification'] = message
        return response