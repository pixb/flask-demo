#!/usr/bin/env python
import os
from app import create_app
app = create_app()

#def test():
#	"""Run the unit tests."""
#	import unittest
#	tests = unittest.TestLoader().discover('tests')
#	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
