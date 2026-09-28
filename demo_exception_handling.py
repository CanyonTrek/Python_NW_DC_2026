#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO handle errors/exceptions
# gracefully using a try/except block
"""
    DocString
"""
import sys
import re

# Example of a USER function with optional parameters,
# and default values
def search_pattern(pattern: str = r"^(.)(.).\2\1$" ,file: str = r"f:\labs\words") -> None:
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as err:
        print(f"Error={err.args[0]}, {err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"Error={err.args[0]}, {err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(2)
    except Exception as err:
        print("Some other error occurred - investigate", file=sys.stderr)
    else:
        # Executes if try block SUCCEEDS!
        reobj = re.compile(pattern) # PRECOMPILE pattern ONLY ONCE!

        for line in fh_in:
            m = reobj.search(line) # Match precompiled pattern against str object
            if m:
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
        fh_in.close()
    finally:
        # Executes ALWAYS!
        print("And now for something completely different..")

    return None

def main():
    search_pattern(r"^.{19}$", r"f:\labs\words")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)