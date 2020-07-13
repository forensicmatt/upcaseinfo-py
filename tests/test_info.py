import sys
sys.path.append("..")
import json
import unittest
from upcaseinfo.info import UpcaseInfo


class TestUpcaseInfo(unittest.TestCase):
    def test_upcase_info_parsing(self):
        # Read testfile into buffer
        testfile = "../testdata/Info"
        with open(testfile, "rb") as fh:
            upcase_info_buffer = fh.read()

        # Parse buffer into UpcaseInfo object
        upcaseinfo = UpcaseInfo(upcase_info_buffer)

        # Validate the known values
        self.assertEqual(32, upcaseinfo.len)
        self.assertEqual(0, upcaseinfo.filler)
        self.assertEqual(15770619046507800844, upcaseinfo.crc)
        self.assertEqual(10, upcaseinfo.osmajor)
        self.assertEqual(0, upcaseinfo.osminor)
        self.assertEqual(16299, upcaseinfo.build)
        self.assertEqual(0, upcaseinfo.packmajor)
        self.assertEqual(0, upcaseinfo.packminor)

        upcaseinfo_dict = upcaseinfo.to_dict()
        self.assertEqual(16299, upcaseinfo_dict["build"])

        info_json_str = json.dumps(upcaseinfo_dict)
        self.assertEqual(
            ('{"len": 32, "filler": 0, "crc": 15770619046507800844, "osmajor": 10, '
             '"osminor": 0, "build": 16299, "packmajor": 0, "packminor": 0}'),
            info_json_str
        )

        self.assertEqual(
            ("crc: 15770619046507800844\n"
             "osmajor: 10\n"
             "osminor: 0\n"
             "build: 16299\n"
             "packmajor: 0\n"
             "packminor: 0"
             ),
            str(upcaseinfo)
        )


if __name__ == '__main__':
    unittest.main()
