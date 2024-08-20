odoo.define('activity_notification.ActivityNotification', function (require) {
    "use strict";

    var session = require('web.session');
    var rpc = require('web.rpc');
    var core = require('web.core');
    var Dialog = require('web.Dialog');

    session.user_has_group('base.group_user').then(function(has_group) {
        if (has_group) {
            rpc.query({
                model: 'mail.activity',
                method: 'get_pending_activities',
                args: [],
            }).then(function(activities) {
                if (activities.length > 0) {
                    var message = "Tienes " + activities.length + " actividades pendientes.";
                    Dialog.alert(this, message, {
                        title: 'Notificación de Actividades',
                    });
                }
            });
        }
    });
});
