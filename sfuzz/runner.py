import subprocess
from typing import Tuple, Union, List

from .utils import *


class Runner:
    """
    The Runner class runs a program in a new process.
    :param program: the program or a list of programs
    :type program: Union[str, List[str]]
    """

    def __init__(self, program: Union[str, List[str]]):
        self.program = program

    def __run_process(self, program_input: str = "") -> subprocess.CompletedProcess:
        """
        Starts a new process from a program name
        :param program_input: the arguments for the program
        :type program_input: str
        :returns: The completed process
        :rtype: subprocess.CompletedProcess
        """
        return subprocess.run(
            [self.program, program_input.encode()],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

    def run(self, program_input: str = "") -> Tuple[subprocess.CompletedProcess, Union[str | None]]:
        """
        Starts new process and returns interruption type or None
        :param program_input: The arguments for standard input
        :type program_input: str
        :returns The completed process and interruption type
        :rtype Tuple[subprocess.CompletedProcess, Union[str | None]]
        """
        result = self.__run_process(program_input)
        if result.returncode < 0:
            return result, signals_return_codes[-result.returncode]
        return result, None
