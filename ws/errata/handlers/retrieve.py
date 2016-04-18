# -*- coding: utf-8 -*-

"""
.. module:: handlers.retrieve.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - retrieve issue endpoint.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
import tornado

from errata import db
from errata import utils



# Query parameter names.
_PARAM_UID = 'uid'



class RetrieveRequestHandler(tornado.web.RequestHandler):
    """Retrieve issue request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        def _decode_request():
            """Decodes request.

            """
            self.uid = self.get_argument(_PARAM_UID)


        def _set_data():
            """Pulls data from db.

            """
            with db.session.create():
                self.issue = {
                    "status": "New",
                    "uid": self.uid
                }


        def _set_output():
            """Sets response to be returned to client.

            """
            self.output_encoding = 'json'
            self.output = {
                'issue': self.issue
            }


        # Invoke tasks.
        utils.h.invoke(self, [
            _decode_request,
            _set_data,
            _set_output
        ])
