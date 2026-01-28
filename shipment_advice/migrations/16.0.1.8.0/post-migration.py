# Copyright 2026 Binhex - Rolando Pérez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    # force recomputation to generate missing picking sequences for shipment
    # advices
    ShipmentAdvice = env["shipment.advice"]
    shipment_advices = ShipmentAdvice.search([])
    env.add_to_compute(
        ShipmentAdvice._fields["planned_picking_order_ids"], shipment_advices
    )
