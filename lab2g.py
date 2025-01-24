#!/usr/bin/env python3
#Author: Prativa Lamichhane
#Author ID: 167520220
#Date Created: 2025/01/24
import sys

def main():
    if len(sys.argv) > 1:
        try:
            timer = int(sys.argv[1])
        except ValueError:
            print("Error: Argument must be an integer.")
            return
    else:
        timer = 3

    while timer > 0:
        print(timer)
        timer -= 1

    print("blast off!")

if __name__ == "__main__":
    main()


