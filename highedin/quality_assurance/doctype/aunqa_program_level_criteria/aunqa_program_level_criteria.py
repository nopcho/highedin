# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class AUNQAProgramLevelCriteria(Document):
	def setnumber(self):
		self.criterion_no = self.name