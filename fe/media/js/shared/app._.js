// --------------------------------------------------------
// $ :: JQuery nonconflict reference.
// See :: http://www.tvidesign.co.uk/blog/improve-your-jquery-25-excellent-tips.aspx#tip19
// --------------------------------------------------------
window.$ = window.$jq = jQuery.noConflict();

// --------------------------------------------------------
// core/main.js - Entry point.
// --------------------------------------------------------
(function (root, $, _, Backbone) {

    // ECMAScript 5 Strict Mode
    "use strict";

    // Root Application module.
    var APP = root.APP = {
        // Title.
        title: "ES-DOC Errata Search",

        // Name.
        NAME: "ES-DOC Errata Search",

        // Version.
        VERSION: '0.1.0.0',

        // Copyright statement.
        copyrightYear: new Date().getFullYear(),

        // Event dispatcher.
        events: _.extend({}, Backbone.Events),

        // Binds a function to an application event.
        on: function (eventType, eventHandler, context) {
            APP.events.on(eventType, eventHandler, context);
        },

        // Triggers an application event.
        trigger: function (eventType, eventArgs) {
            return APP.events.trigger(eventType, eventArgs);
        },

        // Utility functions.
        utils: {},

        // Views.
        views: {}
    };

    // Open splash page event handler.
    $('body > header img').click(function () {
        APP.utils.openURL(APP.defaults.homepage, true);
    });

    // Open support email event handler.
    $('.esdoc-support').click(function () {
        APP.utils.openSupportEmail();
    });

    // Commence setup when document has loaded.
    $(document).ready(function () {
        APP.trigger("setup:begin");
    });

}(
    this,
    this.$,
    this._,
    this.Backbone
));
