import argparse

# Create an ArgumentParser object to parse the fuzzer options
parser = argparse.ArgumentParser(description='Run the sfuzz fuzzer tool with options.')

# Add the fuzzer options as arguments to the ArgumentParser object
parser.add_argument('--jobs', type=int, help='number of parallel jobs to run')
parser.add_argument('--verbose', action='store_true', help='enable verbose output')
parser.add_argument('--chars', type=list, help='list of characters to use in fuzzing')
parser.add_argument('--output', type=str, help='output results to file')

# Parse the command line arguments to extract the fuzzer options
args = parser.parse_args()

# Access the fuzzer options as attributes of the 'args' object
num_jobs = args.jobs
verbose = args.verbose
char_list = args.chars
output_file = args.output

# Print the fuzzer options for verification
print(f'Number of parallel jobs: {num_jobs}')
print(f'Verbose output enabled: {verbose}')
print(f'Character list: {char_list}')
print(f'Output file: {output_file}')
