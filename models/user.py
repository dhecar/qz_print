from openerp.osv import orm, fields


class res_qz_users(orm.Model):
    """
    Users
    """
    _name = 'res.users'
    _inherit = 'res.users'

    _columns = {
        'epl_printer_id': fields.many2one('printing.printer',
                                     string='Default Label Printer'),
    }