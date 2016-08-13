#!/usr/bin/env python

from migrate.versioning.shell import main

if __name__ == '__main__':
	main(url='postgresql://postgres@localhost:5432/add_one', debug='false', six="<module 'six' from '/usr/local/lib/python3.4/site-packages/six.py'>",
	repository = 'db_repository')
