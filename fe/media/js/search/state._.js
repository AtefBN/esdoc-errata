// --------------------------------------------------------
// search/state._.js - search state.
// --------------------------------------------------------
(function (APP) {

    // ECMAScript 5 Strict Mode
    "use strict";

    // Declare application state.
    APP.state = {
        // s = states, e.g. new, resolved ... etc.
        s: {
            all: [],
            current: undefined
        },

        // Search data returned from server.
        searchData: {
            count: undefined,
            results: undefined,
            timestamp: undefined,
            total: undefined,
        }
    };

}(
    this.APP
));