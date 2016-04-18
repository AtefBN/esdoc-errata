# -*- coding: utf-8 -*-
"""

.. module:: app.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - web-service entry point.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
import json

import tornado.web

from errata import handlers
from errata.utils import config
from errata.utils import convert
from errata.utils.logger import log_web as log



# Ensure that tornado will encode json correctly (i.e. handle dates/UUID's).
json._default_encoder = convert.JSONEncoder()


def _get_endpoints():
    """Returns map of application endpoints to handlers.

    """
    endpoints = {
        (r'/', handlers.HeartbeatRequestHandler),
        (r'/issue/retrieve', handlers.RetrieveRequestHandler),
        (r'/issue/search', handlers.SearchRequestHandler)
    }

    log("Endpoint to handler mappings:")
    for url, handler in sorted(endpoints, key=lambda ep: ep[0]):
        log("{0} ---> {1}".format(url, handler))

    return endpoints


def _get_settings():
    """Returns application settings.

    """
    return {
        "cookie_secret": config.cookie_secret
    }


def _get_app():
    """Returns application instance.

    """
    return tornado.web.Application(_get_endpoints(),
                                   debug=(config.mode == 'dev'),
                                   **_get_settings())


def run():
    """Runs web service.

    """
    log("Initializing")

    # Run web-service.
    app = _get_app()
    app.listen(config.port)
    log("Ready")
    tornado.ioloop.IOLoop.instance().start()


def stop():
    """Stops web service.

    """
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.add_callback(lambda x: x.stop(), ioloop)
