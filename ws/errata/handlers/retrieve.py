# -*- coding: utf-8 -*-

"""
.. module:: handlers.retrieve.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - retrieve issue endpoint.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
import tornado

from errata import utils



class RetrieveRequestHandler(tornado.web.RequestHandler):
    """Retrieve issue request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        self.output_encoding = 'json'
        self.output = {
            "message": "ERRATA web service: TODO: retrieve issue from db"
        }
        utils.h.invoke(self)
