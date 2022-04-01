# Imports: standard library
import os
import logging

# Imports: first party
from facinfo.scrap import scrap
from facinfo.arguments import parse_args


def set_verbosity(v_level: int):
    """
    Define verbosity level
    """
    if v_level == 0:
        level = logging.CRITICAL
    if v_level == 1:
        level = logging.WARNING
    if v_level >= 2:
        level = logging.INFO

    logging.basicConfig(level=level)


def main():
    """Main entry point"""
    args = parse_args()

    # Set verbosity
    set_verbosity(args.verbosity)

    # Get the output file
    output_file = args.output
    if not output_file:
        output_file = f"./{args.university}_faculty.csv"

    if not os.path.exists(os.path.dirname(output_file)):
        raise ValueError(f"Path {output_file} does not exist!")
    print(f"Saving results in {output_file}")

    # Scrap -- main algo
    result_df = scrap(university=args.university, max_n=args.max_n)

    # Save file
    result_df.to_csv(output_file)
    print("Done!")


if __name__ == "__main__":
    main()
