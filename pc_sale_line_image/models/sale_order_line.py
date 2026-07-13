# Copyright 2026 Process Control Technology, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    line_image = fields.Image(
        string="Photo",
        max_width=1024,
        max_height=1024,
        help="Illustrative photo shown next to this line in the photo quotation report.",
    )
