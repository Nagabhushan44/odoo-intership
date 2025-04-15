from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Food(models.Model):
    _name = "food.food"
    _description = "Food Items"

    # Fields with unique labels
    partner_id = fields.Many2one('res.partner', string="Customer Name", required=True)
    name = fields.Char(string="Food Name", help='Name of the food item')
    price = fields.Float(string="Price")
    quantity = fields.Float(string="Quantity")
    review = fields.Text(string="Customer Review")
    is_satisfied = fields.Boolean(string="Satisfied Customer")
    check_in = fields.Datetime(string="Check-in Time")
    served_time = fields.Datetime(string="Served Time")
    types = fields.Selection([
        ('veg', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
        ('vegan', 'Vegan')
    ], string="Food Type")
    images = fields.Binary(string="Food Image")
    blog = fields.Html(string="Food Blog")
    date_of_birth = fields.Date(string="Chef's Birth Date")
    age = fields.Integer(string="Chef's Age", compute="_compute_age")
    
    # Related fields
    sale_order_id = fields.Many2one('sale.order', string="Sale Order", readonly=True)
    invoice_id = fields.Many2one('account.move', string="Invoice", readonly=True)
    sale_created = fields.Boolean(string="Sale Created")

    # Allow field parameters in views
    def _valid_field_parameter(self, field, name):
        return name in ['invisible', 'readonly', 'required'] or super()._valid_field_parameter(field, name)

    # Proper batch create method
    @api.model_create_multi
    def create(self, vals_list):
        """Override create method to handle batch creation"""
        for vals in vals_list:
            if 'review' not in vals:
                vals['review'] = "Default review text"
            if 'is_satisfied' not in vals:
                vals['is_satisfied'] = True
        return super().create(vals_list)

    # Button action methods
    def create_sale_order(self):
        """Create sale order from food item"""
        self.ensure_one()
        # Implementation here
        return {
            'type': 'ir.actions.act_window_close'
        }

    def purchase_records(self):
        """Show purchase records"""
        self.ensure_one()
        # Implementation here
        return {
            'type': 'ir.actions.act_window_close'
        }

    def change_the_record(self):
        """Modify record values"""
        self.ensure_one()
        # Implementation here
        return {
            'type': 'ir.actions.act_window_close'
        }

    def delet_the_rec(self):
        """Delete current record"""
        self.ensure_one()
        self.unlink()
        return {
            'type': 'ir.actions.act_window_close'
        }

    # Compute age from birth date
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                rec.age = today.year - rec.date_of_birth.year - (
                    (today.month, today.day) < 
                    (rec.date_of_birth.month, rec.date_of_birth.day)
                )
            else:
                rec.age = 0