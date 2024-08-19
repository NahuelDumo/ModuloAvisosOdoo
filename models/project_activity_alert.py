from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    def _check_pending_activities(self):
        user = self.env.user
        pending_activities = self.env['project.task'].search([
            ('user_id', '=', user.id),
            ('stage_id.fold', '=', False),
            ('date_deadline', '<=', fields.Date.today()),
        ])

        if pending_activities:
            # Mostrar notificación al usuario
            message = f'Tienes {len(pending_activities)} actividades pendientes en el proyecto.\nPor favor revísalas.'
            # Utilizar un método de notificación sin el módulo "web"
            # Puedes usar la funcionalidad 'notify' si no quieres usar el módulo web
            user.notify_warning(message=message)

    @api.model
    def _login(self):
        """Override the login method to check for pending activities."""
        result = super(ResUsers, self)._login()
        self._check_pending_activities()
        return result
