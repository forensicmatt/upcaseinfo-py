import sys
sys.path.append("..")
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


if __name__ == '__main__':
    unittest.main()
