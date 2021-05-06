// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

frappe.ui.form.on('Plo Category', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Plo Category', 'onload', function (frm) {
    frm.set_query("elo_type", "list", function (doc, cdt, cdn) {
        console.log(2)
        let d = locals[cdt][cdn];
        console.log(d)
        return {
            "filters": {
                "type_name" : d.elo_catagory
                }
        };
    });
});
