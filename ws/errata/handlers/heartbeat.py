# -*- coding: utf-8 -*-

"""
.. module:: handlers.heartbeat.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - heartbeat endpoint.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
import datetime as dt

import tornado

from errata import utils

from errata import db



class HeartbeatRequestHandler(tornado.web.RequestHandler):
    """Operations heartbeat request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        self.output_encoding = 'json'
        self.output = {
            "message": "ERRATA web service is operational @ {}".format(dt.datetime.now())
        }
        utils.h.invoke(self)
