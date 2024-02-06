import re
import math
import os
from tqdm import tqdm
from ast import literal_eval

"""
This script parses memory dumps from the Big Blue Consumer Entertainment Bootloader shell and converts them from their
serial form into raw binary.

It automatically recognizes the offsets and number format (byte, 2byte, 4byte) from dump lines and, should they not
start at 0x0, it automatically truncates the output file to size.
"""

_offset_regex = r"^0x0*([0-9a-f]{1,8}) - 0x0*([0-9a-f]{1,8}):"  # Offset at start of line
_data_1_regex = r"0x([0-9a-f]{2})"  # 8 bit value
_data_2_regex = r"0x([0-9a-f]{4})"  # 16 bit value
_data_4_regex = r"0x([0-9a-f]{8})"  # 32 bit value

_input_file_name = ""
_infile_buffer = []

parsed_block_map = {
    # 0x0: bytearray()
    # offset: data pairs
}


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


while not _infile_buffer:
    _input_file_name = input("Please provide capture file name (e.g. ./minicom.cap):")
    try:
        with open(_input_file_name) as _infile_handle:
            _infile_buffer = _infile_handle.readlines()
    except FileNotFoundError:
        print("File not found!")
    # File not found = Retry!

for line in tqdm(_infile_buffer):

    foundLineOffset = re.findall(_offset_regex, line)

    if foundLineOffset:  # If line is not a RAM dump move to the next

        line = re.sub(_offset_regex, '', line)  # Cut away offsets to not interfere with the search for data

        offset = literal_eval(f'0x{foundLineOffset[0][0]}')

        foundData_4byte = re.findall(_data_4_regex, line)
        foundData_2byte = re.findall(_data_2_regex, line)
        foundData_1byte = re.findall(_data_1_regex, line)

        data_byteArray = bytearray()

        if foundData_4byte:  # We check for a 4byte value first because if the value is a 4byte, the others match too
            for data in foundData_4byte:
                data_byteArray += int(data, 16).to_bytes(4, 'little')
        elif foundData_2byte:
            for data in foundData_2byte:
                data_byteArray += int(data, 16).to_bytes(2, 'little')
        elif foundData_1byte:
            for data in foundData_1byte:
                data_byteArray += int(data, 16).to_bytes(1, 'little')
        else:
            raise ValueError("Found an offset but no data! Something has gone very wrong")

        if len(parsed_block_map) == 0:
            parsed_block_map[offset] = data_byteArray
        else:
            for existing_offset, existing_data in parsed_block_map.items():
                if offset == existing_offset + len(existing_data):
                    parsed_block_map[existing_offset] += data_byteArray
                    break
            else:
                parsed_block_map[offset] = data_byteArray

print(f'Found {len(parsed_block_map)} block(s) of memory:\n')
for existing_offset, existing_data in parsed_block_map.items():
    print(
        f'\t{existing_offset:#010x} - {(existing_offset + len(existing_data)):#010x} ({convert_size(len(existing_data))})')

_output_file_name = input(
    f'Please provide an output filename (padded with zeroes if necessary) [{_input_file_name}.bin]')

if not _output_file_name:
    _output_file_name = f'{_input_file_name}.bin'

if os.path.exists(_output_file_name):
    raise FileExistsError("Not overwriting an existing file, aborting!")

else:
    with open(_output_file_name, 'wb', ) as _outfile_handle:
        for offset, data in parsed_block_map.items():
            _outfile_handle.seek(offset)
            _outfile_handle.write(data)
            print(f'Wrote {convert_size(len(data))} at {offset:#010x}')
