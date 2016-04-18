============================
ES-DOC Errata DB Commands
============================

errata-db-install
----------------------------

Installs errata PostgreSQL database.

errata-db-reset
----------------------------

Uninstalls and reinstalls errata PostgreSQL database.  Used during development when database schema changes.

errata-db-uninstall
----------------------------

Drops errata PostgreSQL database.  Called during development as part of a database reset.

errata-db-insert-test-issues [INPUT-DIR]
----------------------------

Inserts tests issues into database from all JSON files within input directory.

**INPUT-DIR**

	Directory within which are issue JSON files.  Defaults to contents of https://github.com/ES-DOC/esdoc-errata/test-data.
