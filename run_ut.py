#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'billyevans'

import ut

import unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(ut)
    unittest.TextTestRunner(verbosity=2).run(suite)
