# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname

class GadgetCollection(WebsiteGenerator):
	def autoname(self):
		temp = make_autoname('HEI-GCO-.######')
		self.collection_id = (temp[:8] + str('%06d' %(int(temp[8:])+1))) 
