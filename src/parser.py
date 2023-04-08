import argparse
import subprocess

class SFuzzer:
    def __init__(self, num_jobs=None, verbose=False, char_list=None, output_file=None):
        self.num_jobs = num_jobs
        self.verbose = verbose
        self.char_list = char_list
        self.output_file = output_file
        
    def run(self):
        # Build the sfuzz command based on the options specified in the object
        sfuzz_command = ["sfuzz"]
        
        if self.num_jobs is not None:
            sfuzz_command += ["--jobs", str(self.num_jobs)]
        
        if self.verbose:
            sfuzz_command.append("--verbose")
        
        if self.char_list is not None:
            sfuzz_command += ["--chars", ",".join(self.char_list)]
        
        if self.output_file is not None:
            sfuzz_command += ["--output", self.output_file]
        
        # Run sfuzz with the specified options
        subprocess.run(sfuzz_command)
        
    @classmethod
    def from_args(cls):
        # Create an ArgumentParser object to parse the fuzzer options
        parser = argparse.ArgumentParser(description='Run the sfuzz fuzzer tool with options.')
        
        # Add the fuzzer options as arguments to the ArgumentParser object
        parser.add_argument('--jobs', type=int, help='number of parallel jobs to run')
        parser.add_argument('--verbose', action='store_true', help='enable verbose output')
        parser.add_argument('--chars', type=str, help='list of characters to use in fuzzing')
        parser.add_argument('--output', type=str, help='output results to file')
        
        # Parse the command line arguments to extract the fuzzer options
        args = parser.parse_args()
        
        # Create an SFuzzer object with the parsed options
        return cls(num_jobs=args.jobs, verbose=args.verbose, char_list=args.chars.split(','), output_file=args.output)

