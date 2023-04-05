import subprocess

import utils


class Runner:

    def __init__(self, program: str):
        self.program = program

    def __run_process(self, program_input: str = "") -> subprocess.CompletedProcess:
        return subprocess.run(
            [self.program, program_input.encode()],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

    def run(self, program_input: str = ""):
        result = self.__run_process(program_input)
        if result.returncode < 0:
            return result, utils.signals_return_codes[-result.returncode]
        return result, None


runner = Runner(program="../tests/binaries/bin/test_buffer_overflow")
print(runner.run(program_input="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
