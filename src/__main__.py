from .fuzzer import Fuzzer
from .runner import Runner


def main():
    runner = Runner("./tests/binaries/bin/test_buffer_overflow")
    fuzzer = Fuzzer()
    print(fuzzer.runs(runner))


if __name__ == "__main__":
    main()
