// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

var run = false

frappe.ui.form.on('Gadget Product', {
	// refresh: function(frm) {

	// },
	onload:	function(frm) { 
		console.log('frm:', frm);
		run = true
	},
	after_save: (self) => {
		self.doc.product_id = self.doc.name
		console.log('after:', self.doc.name, 'id:', self.doc.product_id);
		// self.save()
		if(run) self.save() 
		run = false

	},
});
