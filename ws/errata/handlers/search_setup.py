# -*- coding: utf-8 -*-

"""
.. module:: handlers.search.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - search issues endpoint.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
from errata import constants
from errata import db
from errata.utils.http import HTTPRequestHandler



class SearchSetupRequestHandler(HTTPRequestHandler):
    """Search issue request handler.

    """
    def __init__(self, application, request, **kwargs):
        """Instance constructor.

        """
        super(SearchSetupRequestHandler, self).__init__(application, request, **kwargs)

        self.states = constants.ISSUE_STATES


    def get(self):
        """HTTP GET handler.

        """
        def _set_data():
            """Pulls data from db.

            """
            # TODO pull required data from db.
            with db.session.create():
                pass


        def _set_output():
            """Sets response to be returned to client.

            """
            self.output_encoding = 'json'
            self.output = {
                'states': self.states
            }


        # Invoke tasks.
        self.invoke([], [
            _set_data,
            _set_output
            ])
