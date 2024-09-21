import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class MyModuleController(http.Controller):

    @http.route('/my_module/notify', type='json', auth='user')
    def notify_user(self):
        user = request.env.user
        tasks = request.env['project.task'].search([('user_id', '=', user.id)])

        if tasks:
            message = f'Tienes {len(tasks)} actividades pendientes.'
            request.env['bus.bus']._sendone(
                (request.env.cr.dbname, 'res.partner', user.partner_id.id),
                {
                    'type': 'simple_notification',
                    'title': 'Actividades Pendientes',
                    'message': message,
                    'sticky': False,
                }
            )
        return {'status': 'success'}
