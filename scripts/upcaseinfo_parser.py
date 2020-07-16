import sys
sys.path.append("..")
import json
from argparse import ArgumentParser
import logging
from upcaseinfo.info import UpcaseInfo

VERSION = "0.1.0"


def get_argument_parser() -> ArgumentParser:
    """Create an ArgumentParser which will parse arguments from
    the command line parameters passed to this tool.

    :return: The argument parser
    """
    usage = "Parse an $UpCase:$Info file and display the output. v{}".format(
        VERSION
    )

    arguments = ArgumentParser(
        description=usage
    )

    arguments.add_argument(
        "-s", "--source",
        dest="source",
        action="store",
        required=True,
        help="The source $UpCase:$Info file to parse."
    )

    arguments.add_argument(
        "-f", "--format",
        dest="format",
        action="store",
        choices=["text", "json"],
        default="json",
        required=True,
        help="The output format."
    )

    arguments.add_argument(
        "--logging",
        dest="logging",
        action="store",
        default="INFO",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"],
        help="Logging level [default=INFO]"
    )

    return arguments


def set_logging_level(logging_level: str):
    """Set the logging level to use.

    :param logging_level: The logging level's variable name as used in the logging lib.
    :return:
    """
    logging.basicConfig(
        level=getattr(logging, logging_level)
    )


def main():
    arg_parser = get_argument_parser()
    options = arg_parser.parse_args()

    set_logging_level(
        options.logging
    )

    source_file = options.source
    logging.info("parsing file: {}".format(source_file))

    with open(source_file, "rb") as file_handle:
        raw_buffer = file_handle.read()
        upcase_info = UpcaseInfo(raw_buffer)

        if options.format == "json":
            upcase_info_dict = upcase_info.to_dict()
            print(json.dumps(upcase_info_dict, indent=2))
        elif options.format == "text":
            print(str(upcase_info))
        else:
            raise Exception("Unhandled output format: {}".format(options.format))


if __name__ == "__main__":
    main()
