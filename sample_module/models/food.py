from odoo import models, fields

class Food(models.Model):
    _name = "food.food"
    _description = "Model For Food"

    name = fields.Char(string="Name")
    price = fields.Float(string="Standard Price")
    quantity = fields.Integer(string="Amount")
    review = fields.Text(string="Review Of The Food")
    is_satisfied = fields.Boolean(string="Satisfied/Not")
    check_in = fields.Date(string="Check In")
    served_time = fields.Datetime(string="Served Time")
    types = fields.Selection([('dine_in', 'Dine In'), ('delivery', 'Delivery')])
    images = fields.Binary(string="Images")
    blog = fields.Html(string="Blog")
    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    invoice_id = fields.Many2one('account.move', string="Related Invoice")

    sale_created = fields.Boolean(string="Sale Order Created")

    def create_sale_order(self):
        sale_order = self.env['sale.order'].create({
            'partner_id': 23
        })
        self.sale_created = True
        return sale_order

    def create_invoice(self):
        pass

    def create_contacts(self):
        pass

    def create_purchase_order(self):
        pass