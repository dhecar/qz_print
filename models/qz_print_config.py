# -*- coding: utf-8 -*-
from osv import fields, osv


class QzConfig(osv.osv):

    _name = 'qz.config'
    _table = 'qz_config'
    _description = 'Qz Print configuration'

    _columns = {
        'printer': fields.char('Printer', size=100),
        'text_field': fields.char('Text Field', size=100),
        'barcode_field': fields.char('Barcode Field', size=100),


    }

QzConfig()
