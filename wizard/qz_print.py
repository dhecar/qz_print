# -*- coding: utf-8 -*-
from osv import fields, osv


class QzPrint(osv.osv):

    _name = 'qz.print'
    _description = 'Qz Print Labels'

    _columns = {
        'copies': fields.char('Num of Copy:', size=4),
    }


    #def get_spool(self, cr, uid, context=None):
    #def get_selection(self, rows, columns, ids, model):


    #def prepare_epl_data(self, cr, uid, context=None)
    #def send_epl_data(self, cr, uid, context=None)

QzPrint()
