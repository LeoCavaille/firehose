#   Copyright 2013 Red Hat, Inc.
#
#   This is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see
#   <http://www.gnu.org/licenses/>.

import os
import unittest

from firehose.parsers.cppcheck import parse_file
from firehose.report import Issue, Sut

FAKE_SUT = Sut()

class TestParseXml(unittest.TestCase):
    def test_example_001(self):
        a = parse_file(os.path.join(os.path.dirname(__file__),
                                    'example-output',
                                    'cppcheck-xml-v2',
                                    'example-001.xml'))
        self.assertEqual(a.metadata.generator.name, 'cppcheck')
        self.assertEqual(a.metadata.generator.version, '1.57')
        self.assertEqual(a.metadata.sut, None)
        self.assertEqual(a.metadata.file_, None)
        self.assertEqual(a.metadata.stats, None)
        self.assertEqual(len(a.results), 7)
        r0 = a.results[0]
        self.assertEqual(r0.cwe, None)
        self.assertEqual(r0.testid, 'uninitvar')
        self.assertEqual(r0.message.text, 'Uninitialized variable: ret')
        self.assertEqual(r0.notes, None)
        self.assertEqual(r0.location.file.givenpath,
                         'python-ethtool/etherinfo_obj.c')
        self.assertEqual(r0.location.file.abspath, None)
        self.assertEqual(r0.location.function, None)
        self.assertEqual(r0.location.line, 185)
        self.assertEqual(r0.trace, None)
