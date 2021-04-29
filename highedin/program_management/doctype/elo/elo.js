// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

frappe.ui.form.on('Elo', 'onload', function(frm){
	frm.set_query('elo_type', function() {
		return {
		   "filters" : {
			"type_name" : frm.doc.elo_category
			}
		};
	});
});

