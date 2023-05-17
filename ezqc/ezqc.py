import argparse
import numpy as np
from pbsq import run_pbsq


def parse_fastq_file(file_obj):
    while True:
        header = file_obj.readline().strip()
        if not header:
            break
        sequence = file_obj.readline().strip()
        file_obj.readline()
        quality_str = file_obj.readline().strip()
        yield header, sequence, quality_str

def main():
    # Create the argparse object and define the arguments
    parser = argparse.ArgumentParser(description="EZQC FastQ Quality Analyzer")
    parser.add_argument('reads', metavar='READ', nargs='+', help='input .fastq file(s)')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Process each .fastq file
    for file_path in args.reads:
        print(f"Processing file: {file_path}")

        headers = []
        sequences = []
        quality_strings = []

        with open(file_path, 'r') as fastq_file:
            for header, sequence, quality_str in parse_fastq_file(fastq_file):
                headers.append(header)
                sequences.append(sequence)
                quality_strings.append(quality_str)
        average_length_each_sequence = np.average([len(x) for x in quality_strings])

        
        run_pbsq(quality_strings, average_length_each_sequence)


if __name__ == '__main__':
    main()
