import os
import argparse
from time import sleep
from script import submission

def submit_solution(problem_code, username, password, file_path, language):
    submission(problem_code, username, password, file_path, language)

def main():
    parser = argparse.ArgumentParser(description="Codeforces Solution Submitter")

    parser.add_argument("problem_code", help="Codeforces problem code (e.g., 4A)")
    parser.add_argument("username", help="Your Codeforces username")
    parser.add_argument("password", help="Your Codeforces password")
    parser.add_argument("language", help="Programming language (e.g., 'PyPy 3.9.10 (7.3.9, 64bit)')")

    parser.add_argument("file_path", nargs='?', default=os.getcwd(), help="Path to the solution file")

    args = parser.parse_args()
    
    if os.path.isdir(args.file_path):
        print("PROVIDED DIR")
        args.file_path = os.path.join(args.file_path, f"{args.problem_code}.py")


    submit_solution(args.problem_code, args.username, args.password, args.file_path, args.language)

if __name__ == "__main__":
    main()