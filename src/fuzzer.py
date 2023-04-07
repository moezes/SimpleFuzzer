import random

from .runner import Runner


class Fuzzer:
    """
    The Fuzzer class generates input to provide to a program
    :param min_length: minimum length of payload
    :type min_length: int
    :param max_length: maximum length of payload
    :type max_length: int
    :param char_start: first character in the ASCII range used to generate payload
    :type char_start: int
    :param char_range: the ASCII range width for a character in payload
    :type char_range: int
    """

    def __init__(self, min_length: int = 10, max_length: int = 100,
                 char_start: int = 32, char_range: int = 32):
        self.min_length = min_length
        self.max_length = max_length
        self.char_start = char_start
        self.char_range = char_range

    def fuzz(self) -> str:
        """
        Generates a payload with random bytes of length between min_length and max_length, each byte in the ASCII range
        [char_start; char_start + 1]
        :returns: The payload
        :rtype: str
        """
        payload_len = random.randrange(self.min_length, self.max_length + 1)
        payload = ""
        for i in range(payload_len):
            payload += chr(random.randrange(self.char_start, self.char_start + self.char_range))
        return payload

    def run(self, runner: Runner):
        """
        Launch a runner with a generated payload
        :param runner: the runner to start
        :type runner: Runner
        :returns: The completed process and interruption type
        """
        return runner.run(self.fuzz())

    def runs(self, runner: Runner, trials: int = 10):
        """
        Runs <trials> times
        :param runner: the runner to use
        :type runner: Runner
        :param trials: number of runs to do
        :returns: The list of completed processes and interruption types
        """
        return [self.run(runner) for _ in range(trials)]
