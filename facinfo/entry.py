import logging
from facinfo.arguments import parse_args
from facinfo.scrap import scrap

def set_verbosity(v_level):
    if v_level == 0:
        level = logging.CRITICAL
    if v_level == 1:
        level = logging.WARNING
    if v_level >= 2:
        level = logging.INFO

    logging.basicConfig(level=level)

def main():
    args = parse_args()

    # Set verbosity
    set_verbosity(args.verbosity)

    # Get the output file
    output_file = args.output
    if not output_file:
        output_file = f"./{args.university}_faculty.csv"
    print(f"Saving results in {output_file}")

    # Scrap -- main algo
    result_df = scrap(university=args.university)

    # Save file
    result_df.to_csv(output_file)
    print("Done!")


if __name__ == '__main__':
    main()

