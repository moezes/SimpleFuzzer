import subprocess
from typing import Tuple, Union

from sfuzz.runner import Runner


class Fuzzer:

    def __init__(self):
        self.runner = None

    def fuzz(self):
        return ""

    def set_runner(self, runner: Runner):
        self.runner = runner

    def run(self, runner: Runner = None) -> Tuple[subprocess.CompletedProcess, Union[str, None]]:
        """
        Launch a runner with a generated payload
        :param runner: the runner to start
        :type runner: Runner
        :returns: The completed process and interruption type
        """
        if runner is not None:
            return runner.run(self.fuzz())
        elif self.runner is not None:
            return self.runner.run(self.fuzz())

        raise Exception("You need to specify a runner.")

    def runs(self, runner: Runner = None, trials: int = 10):
        """
        Runs <trials> times
        :param runner: the runner to use
        :type runner: Runner
        :param trials: number of runs to do
        :returns: The list of completed processes and interruption types
        """
        return [self.run(runner) for _ in range(trials)]
