from odoo import models, fields, api
from odoo.exceptions import UserError

class Activity(models.Model):
    _inherit = 'mail.activity'

    @api.model
    def check_pending_activities(self):
        user = self.env.user
        activities = self.search([
            ('user_id', '=', user.id),
            ('state', '!=', 'preparado')
        ])
        if activities:
            raise UserError(f"Tienes {len(activities)} actividades pendientes.")

