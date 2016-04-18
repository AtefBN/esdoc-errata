# -*- coding: utf-8 -*-
"""
.. module:: db.dao.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - db data access.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
from errata.db.session import query
from errata.db.models import Issue
from errata.db.utils import text_filter



def get_issue(uid):
    """Returns an issue.

    :param str uid: Issue unique identifier.

    :returns: First matching issue.
    :rtype: db.models.Issue

    """
    qry = query(Issue)
    qry = text_filter(qry, Issue.uid, uid)

    return qry.first()


def get_issues(status=None):
    """Returns an issue.

    :param str status: Issue status filter field.

    :returns: First matching issue.
    :rtype: db.models.Issue

    """
    qry = query(Issue)
    if status:
        qry = text_filter(qry, Issue.status, status)

    return qry.all()
