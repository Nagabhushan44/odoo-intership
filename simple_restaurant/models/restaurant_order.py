from odoo import models, fields, api

class RestaurantOrder(models.Model):
    _name = 'restaurant.order'
    _description = 'Customer Order'

    name = fields.Char('Order Reference', default='New')
    customer_name = fields.Char('Customer Name', required=True)
    order_date = fields.Datetime('Order Time', default=fields.Datetime.now)
    order_lines = fields.One2many('restaurant.order.line', 'order_id', 'Items')
    total = fields.Float('Total Amount', compute='_compute_total')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Completed'),
        ('canceled', 'Canceled')
    ], default='draft')

    @api.depends('order_lines.subtotal')
    def _compute_total(self):
        for order in self:
            order.total = sum(line.subtotal for line in order.order_lines)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('restaurant.order') or 'New'
        return super().create(vals)

class RestaurantOrderLine(models.Model):
    _name = 'restaurant.order.line'
    _description = 'Order Line Item'

    order_id = fields.Many2one('restaurant.order', 'Order')
    menu_item_id = fields.Many2one('restaurant.menu.item', 'Item', required=True)
    quantity = fields.Integer('Qty', default=1)
    price = fields.Float('Unit Price', related='menu_item_id.price')
    subtotal = fields.Float('Subtotal', compute='_compute_subtotal')

    @api.depends('quantity', 'price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price