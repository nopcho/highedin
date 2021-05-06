// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

frappe.ui.form.on('Curriculum Course', 'onload', function (frm) {
    frm.set_query("num_type", function () {
	console.log(1)
        return {
            "filters": {
                "type_name": frm.doc.elo_cate
            }
        };

    });
    frm.set_query("elo_type", "course_elo", function (doc, cdt, cdn) {
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
