// --------------------------------------------------------
// search/view._.js - Main page view.
// --------------------------------------------------------
(function (APP, _, Backbone, $) {

    // ECMAScript 5 Strict Mode
    "use strict";

    // Main module level view.
    APP.views.MainView = Backbone.View.extend({
        // Backbone: view event handlers.
        events : {

        },

        // Backbone: view initializer.
        initialize : function () {
            APP.events.on("state:issueListUpdate", this._updateStatisticsInfo, this);
            APP.events.on("state:issueListUpdate", this._updateGrid, this);
        },

        // Backbone: view renderer.
        render : function () {
            APP.utils.renderTemplate("page-header", APP, this);

            return this;
        },

        // Updates results grid.
        _updateGrid: function () {
            this._replaceNode('tbody', 'grid-body-template', MOD.state);
        },

        // Utility function to replace a page DOM node.
        _replaceNode: function (nodeSelector, template, templateData) {
            this.$(nodeSelector).replaceWith(APP.utils.renderTemplate(template, templateData));
        }
    });

}(
    this.APP,
    this._,
    this.Backbone,
    this.$
));
