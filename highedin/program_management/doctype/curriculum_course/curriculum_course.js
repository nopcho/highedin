// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

frappe.ui.form.on('Curriculum Course', 'onload', function(frm){
	frm.set_query("num_type", function() {
		return {
			"filters" : {
				"type_name" : frm.doc.elo_cate 
			}
			};
			
		});
});
