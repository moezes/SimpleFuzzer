from sfuzz.fuzzers.random import RandomFuzzer
from .cfg import CFG
from .coverage import Coverage
from .runner import Runner


def get_fuzzer():
    runner = Runner("./tests/binaries/bin/test_buffer_overflow")
    fuzzer = RandomFuzzer()
    fuzzer.set_runner(runner)
    return fuzzer


def run_coverage():
    fuzzer = get_fuzzer()
    with Coverage() as cv:
        fuzzer.runs()
    print(cv.coverage())


def test(a: int, b: int, c: int):
    if a == 5:
        print("hello")
        if b == 1:
            print("of")
    else:
        if c == -5:
            print("hackers")
        else:
            print("world")


def run_cfg():
    cfg = CFG(fn=test)
    print(cfg.get_annotations())


def run_fuzzer():
    fuzzer = get_fuzzer()
    print(fuzzer.run())


def main():
    run_fuzzer()


if __name__ == "__main__":
    main()
