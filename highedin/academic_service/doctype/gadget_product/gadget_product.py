# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.website.website_generator import WebsiteGenerator

from frappe.model.naming import getseries
from frappe.model.naming import make_autoname

class GadgetProduct(WebsiteGenerator):
	def autoname(self):
		temp = make_autoname('HEI-GPR-.######')
		self.product_id = (temp[:8] + str('%06d' %(int(temp[8:])+1))) 
	
