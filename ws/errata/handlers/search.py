# -*- coding: utf-8 -*-

"""
.. module:: handlers.search.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - search issues endpoint.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
import tornado

from errata import utils



class SearchRequestHandler(tornado.web.RequestHandler):
    """Issue search request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        self.output_encoding = 'json'
        self.output = {
            "message": "ERRATA web service: TODO: search for issues in db"
        }
        utils.h.invoke(self)
