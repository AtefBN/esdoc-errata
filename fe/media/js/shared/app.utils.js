// --------------------------------------------------------
// core.utils.js - misceallaneous helper functions used across applications.
// --------------------------------------------------------
(function (APP, _, console, window) {

    // ECMAScript 5 Strict Mode
    "use strict";

    // Opens the target url.
    // @url     URL to be opened.
    // @inTab   Flag indicating whether url will be opened in a new browser tab or not.
    APP.utils.openURL = function (url, inTab) {
        if (inTab === true) {
            window.open(url);
        } else {
            window.location = url;
        }
    };

    // Initializes a view.
    // @view        A view.
    APP.utils.initializeView = function (view) {
        // Bind intra-view event listeners.
        if (view.listeners) {
            _.each(_.keys(view.listeners), function (eventKey) {
                APP.utils.bind(eventKey, view);
            });
        }
    };

    // Returns an intra-view event handler.
    // @eventKey    Key of event being listened to.
    // @view        Event listener.
    var getIntraViewEventHandler = function (eventKey, view) {
        if (_.isFunction(view.listeners[eventKey])) {
            return view.listeners[eventKey];
        }
        return view[view.listeners[eventKey]];
    };

    // Binds a callback to an intra-view event.
    // @eventKey    Key of event being listened to.
    // @view        Event listener.
    APP.utils.bind = function (eventKey, view) {
        var handler;

        if (_.has(view.listeners, eventKey)) {
            handler = getIntraViewEventHandler(eventKey, view);
            APP.on(eventKey, handler, view);
        }
    };

    // Opens the target email.
    // @address         Target email address.
    // @subject         Target email subject.
    APP.utils.openEmail = function (address, subject, message) {
        var email = "mailto:{0}?subject={1}&body={2}";

        subject = subject || APP.constants.email.defaultSubject;
        message = message || APP.constants.email.defaultMessage;

        email = email.replace('{0}', address);
        email = email.replace('{1}', subject);
        email = email.replace('{2}', message);

        window.location.href = email;
    };

    // Opens module support email.
    // @module         Module for which a support email is being sent.
    APP.utils.openSupportEmail = function () {
        var subject;

        subject = "ES-DOC :: SUPPORT :: Search (v{0}) :: support question";
        subject = subject.replace("{0}", APP.version);
        APP.utils.openEmail(APP.constants.email.support, subject);
    };

    // Renders a view.
    // @Type          View type.
    // @options       View options.
    // @container     View container.
    APP.utils.render = function (Typeof, options, container) {
        var view;

        // Render view.
        view = new Typeof(options);
        view = view.render();

        // Append to container.
        if (!_.isUndefined(container)) {
            if (_.has(container, '$el')) {
                container.$el.append(view.$el);
            } else {
                container.append(view.$el);
            }
        }

        // Return render root.
        return container || view;
    };

    // Renders a set of views.
    // @types       Set of view types.
    // @options     Set of view options.
    // @container   Container view.
    APP.utils.renderAll = function (types, options, container) {
        _.each(types, function (ViewType) {
            APP.utils.render(ViewType, options, container);
        });
        return container;
    };

    // Returns URL query param value.
    // @name                URL query param name.
    // @defaultValue        URL query param default value.
    APP.utils.getURLParam = function (name, defaultValue) {
        var
            results = new RegExp('[\\?&]' + name + '=([^&#]*)').exec(window.location.href);
        if (!results) {
            return defaultValue;
        }
        return (results[1] || defaultValue).toUpperCase();
    };

}(
    this.APP,
    this._,
    this.console,
    this.window
));
