from odoo import models, fields

class MenuItem(models.Model):
    _name = 'restaurant.menu.item'
    _description = 'Menu Item'

    name = fields.Char('Item Name', required=True)
    category = fields.Selection([
        ('food', 'Food'),
        ('drink', 'Drink'),
        ('dessert', 'Dessert')
    ], required=True)
    price = fields.Float('Price', required=True)
    active = fields.Boolean('Available', default=True)
    description = fields.Text('Description')