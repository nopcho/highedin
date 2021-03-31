// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gadget Collection', {
	// refresh: function(frm) {

	// }
	onload:	function(frm) { 
		console.log('frm:', frm);
		run = true
		console.log(frm);
	},
	after_save: (self) => {
		console.log(self.doc);
		self.doc.collection_id = self.doc.name
		console.log('after:', self.doc.name, 'id:', self.doc.collection_id);
		// self.save()
		if(run) self.save() 
		run = false

	},
});
