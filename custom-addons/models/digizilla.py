from odoo import models, fields

class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Digizilla Model'

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string='Gender',
        tracking=True
    )
    country = fields.Char(string='Country', tracking=True)
    joining_date = fields.Date(string='Joining Date', tracking=True)
    tags = fields.Char(string='Tags', tracking=True)
    customer_ids = fields.Many2many(
        'res.partner',
        string='Customers',
        tracking=True
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        tracking=True
    )
    notes = fields.Text(string='Notes')
    comments = fields.Char(string='Comments')
