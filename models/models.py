
from odoo import api, fields, models
import time
import datetime
import logging
_logger = logging.getLogger(__name__)


class ModuleName(models.Model):
    _name = 'module.name'
    _description = 'New Description'

    name = fields.Char(string='Name')
