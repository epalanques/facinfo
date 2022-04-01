# Imports: standard library
import argparse


def parse_args():
    """Argument parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "university",
        help="Select the university. Available are: BU (bioinfo) and MIT (MECHE)",
        choices=["MIT", "BU"],
    )
    parser.add_argument(
        "--output",
        "-o",
        help="path of the output file with the faculty list",
    )
    parser.add_argument(
        "--verbosity",
        "-v",
        action="count",
        default=0,
        help="Verbosity level. Defaults to quiet. -v gives warnings. -vv gives info",
    )
    return parser.parse_args()
