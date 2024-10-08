from odoo import models, fields, api
from datetime import datetime, timedelta

class project_task(models.Model):
    _inherit = 'project.task'

    # Custom field to track tasks nearing their due date
    is_due_soon = fields.Boolean(string='Due Soon', compute='_compute_due_soon', store=True)

    @api.depends('date_deadline')
    def _compute_due_soon(self):
        for record in self:
            if record.date_deadline:
                due_date = datetime.strptime(record.date_deadline, '%Y-%m-%d')
                if due_date - datetime.now() <= timedelta(hours=24):
                    record.is_due_soon = True
                else:
                    record.is_due_soon = False