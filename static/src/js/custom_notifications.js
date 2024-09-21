odoo.define('my_module.custom_notifications', function (require) {
    "use strict";

    var session = require('web.session');
    var ajax = require('web.ajax');

    session.user_has_group('base.group_user').then(function (has_group) {
        if (has_group) {
            ajax.jsonRpc('/my_module/notify', 'call', {}).then(function (result) {
                console.log(result);  // Puedes agregar lógica adicional aquí
            });
        }
    });
});
