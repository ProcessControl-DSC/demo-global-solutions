# Copyright 2026 Process Control Technology, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
{
    "name": "PC Sale Line Image",
    "version": "19.0.1.0.0",
    "summary": "Add a photo per quotation line and a photo-enabled quotation report",
    "description": """
Presupuestos con foto por línea
===============================

Añade un campo de imagen a cada línea del presupuesto/pedido de venta y
publica un informe de presupuesto adicional que muestra la foto junto a cada
partida. Pensado para presupuestos de reforma, donde ilustrar cada partida con
una imagen aporta claridad al cliente.

* Campo imagen en la línea de venta (editable en el formulario del presupuesto).
* Informe "Presupuesto con fotos" independiente del informe estándar, para
  poder ofrecer ambos formatos.
""",
    "author": "Process Control Technology, S.L.",
    "website": "https://www.processcontrol.es",
    "category": "Sales/Sales",
    "license": "LGPL-3",
    "depends": ["sale_management"],
    "data": [
        "views/sale_order_views.xml",
        "reports/sale_report_photos.xml",
    ],
    "installable": True,
    "application": False,
}
