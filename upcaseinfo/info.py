import struct


class UpcaseInfo(object):
    """This class represents the UPCASEINFO data structure.
    Reference: https://github.com/vitalif/ntfs-3g/blob/04d4b37a9a6c992d89c93193d0abdd13ab1f2931/ntfsprogs/mkntfs.c#L168
    """
    def __init__(self, buffer: bytes):
        """Create the UpcaseInfo from a given buffer.
        """
        self.len = struct.unpack("<I", buffer[0:4])[0]
        # Ensure that the buffer has the required size
        if len(buffer) < self.len:
            raise Exception(
                "The length of the UpcaseInfo is larger than the provided buffer size of {}".format(
                    len(buffer)
                )
            )

        self.filler = struct.unpack("<I", buffer[4:8])[0]
        self.crc = struct.unpack("<Q", buffer[8:16])[0]
        self.osmajor = struct.unpack("<I", buffer[16:20])[0]
        self.osminor = struct.unpack("<I", buffer[20:24])[0]
        self.build = struct.unpack("<I", buffer[24:28])[0]
        self.packmajor = struct.unpack("<H", buffer[28:30])[0]
        self.packminor = struct.unpack("<H", buffer[30:32])[0]
