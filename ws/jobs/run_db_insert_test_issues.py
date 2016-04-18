# -*- coding: utf-8 -*-

"""
.. module:: run_db_insert_test_issues.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Inserts test issues into the errata db.

.. moduleauthor:: Atef Benasser <abenasser@ipsl.jussieu.fr>


"""
import argparse
import json
import os
import glob

from errata import db
from errata.db.models import Issue



# Define command line arguments.
_parser = argparse.ArgumentParser("Inserts test issues into errata database.")
_parser.add_argument(
    "-d", "--dir",
    help="Directory containing test issues in json file format",
    dest="input_dir",
    type=str
    )


def _insert(obj):
	"""Inserts an issue into db from a dictionary loaded from a json file.

	"""
	instance = Issue()
	instance.status = obj['state']

	db.session.insert(instance)


def _yield_issues(input_dir):
	"""Yields issues found in json files within input directory.

	"""
	for fpath in glob.iglob("{}/*.json".format(input_dir)):
		with open(fpath, 'r') as f:
			yield json.loads(f.read())


def _main(args):
    """Main entry point.

    """
    if not os.path.exists(args.input_dir):
        raise ValueError("Input directory is invalid.")

    with db.session.create():
    	for obj in _yield_issues(args.input_dir):
    		_insert(obj)



# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
