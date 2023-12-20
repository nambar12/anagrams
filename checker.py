#!/usr/bin/python
import os
import sys
import time
import colorama
from colorama import Fore
import subprocess

checks = {
    '1_ang_5000_times.txt': 1,
    '100_5000_500.txt': 27,
    '10000_10000_50.txt': 334,
    '10_1000000_10.txt': 4
}


def check(program):
    total_time = 0
    for test in checks:
        check_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "checks", test)
        with open(check_file, 'rb') as file:
            start_time = time.time()
            process = subprocess.Popen(program, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=file)
            output, error = process.communicate()
            finish_time = time.time()
            output = output.decode('utf-8')
            error = error.decode('utf-8')
            output_result(output.strip(), error.strip(), test, finish_time - start_time)
            total_time += finish_time - start_time
    print(f"{Fore.YELLOW}Total time: {total_time:.2f} seconds{Fore.RESET}")


def output_result(output, error, test, test_time):
    if error != '':
        print(f"{Fore.RED}{error}{Fore.RESET}")
    status, color, diff = ('PASS', Fore.GREEN, '') if str(checks[test]) == output else ('FAIL', Fore.RED, f"{checks[test]} != {output}")
    print(f"{color}[{status}]{Fore.RESET} {test:<25} ({test_time:.2f}) {Fore.YELLOW}{diff}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: checker.py <program>", file=sys.stderr)
        exit(1)
    colorama.init(autoreset=True)
    executable = sys.argv[1] if os.path.isabs(sys.argv[1]) else os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1])
    if not os.path.exists(executable) and not os.access(executable, os.X_OK):
        print("Invalid program (or not executable) <program>", file=sys.stderr)
        exit(2)
    check(executable)


