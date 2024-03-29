# -*- coding: utf-8 -*-

"""
.. module:: handlers.heartbeat.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - heartbeat endpoint.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
import datetime as dt

from errata.utils.http import HTTPRequestHandler



class HeartbeatRequestHandler(HTTPRequestHandler):
    """Operations heartbeat request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        def _set_output():
            """Sets response to be returned to client.

            """
            self.output = {
                "message": "ERRATA web service is operational @ {}".format(dt.datetime.now()),
                "status": 0
            }

        # Invoke tasks.
        self.invoke([], _set_output)
