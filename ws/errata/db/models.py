# -*- coding: utf-8 -*-
"""
.. module:: db.models.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - db tables.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
import datetime
import uuid

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import Unicode
from sqlalchemy import UniqueConstraint

from errata.db.utils import Entity



# Database schema.
_SCHEMA = 'errata'



class Issue(Entity):
    """An issue raised by an institute post-publication.

    """
    # SQLAlchemy directives.
    __tablename__ = 'tbl_issue'
    __table_args__ = (
        {'schema':_SCHEMA}
    )

    # TODO define columns
    uid = Column(Unicode(63), nullable=False, unique=True, default=uuid.uuid4())
    status = Column(Unicode(31), nullable=False)
    # NOTE: following columns already defined upon base class:
    #       id, row_create_date, row_update_date
    # E.G. https://github.com/ES-DOC/esdoc-api/esdoc_api/db/models/docs.py
