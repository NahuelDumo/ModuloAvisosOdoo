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
            # Aquí podrías utilizar otras formas de notificación si no quieres usar el módulo "web"
            message = f'Tienes {len(pending_activities)} actividades pendientes en el proyecto.\nPor favor revísalas.'
            user.notify_warning(message=message)

    @api.model
    def _login(self):
        """Override the login method to check for pending activities."""
        super(ResUsers, self)._login()
        self._check_pending_activities()
