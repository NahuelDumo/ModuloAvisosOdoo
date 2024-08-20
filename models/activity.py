from odoo import models, fields, api

class Activity(models.Model):
    _inherit = 'mail.activity'

    @api.model
    def get_pending_activities(self):
        user = self.env.user
        activities = self.search([
            ('user_id', '=', user.id),
            ('state', '!=', 'preparado')
        ])
        return activities
