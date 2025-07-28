from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def test_get_files_info():
    test_cases = [
        ["calculator", "."],
        ["calculator", "pkg"],
        ["calculator", "/bin"],
        ["calculator", "../"],
    ]
    for args in test_cases:
        working_directory = args[0]
        directory = args[1]
        if directory == ".":
            print("Result for current directory:")
        else:
            print(f"Result for '{directory}' directory:")
        print(get_files_info(*args))


def test_get_file_content():
    test_cases = [
        ["calculator", "main.py"],
        ["calculator", "pkg/calculator.py"],
        ["calculator", "/bin/cat"],
        ["calculator", "pkg/does_not_exist.py"],
    ]
    for args in test_cases:
        print(f"Contents of '{args[1]}':")
        print(get_file_content(*args))


def test_write_file():
    test_cases = [
        ["calculator", "lorem.txt", "wait, this isn't lorem ipsum"],
        ["calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"],
        ["calculator", "/tmp/temp.txt", "this should not be allowed"],
    ]
    for args in test_cases:
        print(f"Writing to file '{args[1]}':")
        print(write_file(*args))


def test_run_python_file():
    test_cases = [
        ["calculator", "main.py"],
        ["calculator", "main.py", ["3 + 5"]],
        ["calculator", "tests.py"],
        ["calculator", "../main.py"],
        ["calculator", "nonexistent.py"],
    ]
    for args in test_cases:
        if len(args) == 2:
            print(f"Running '{args[1]}' with no args:")
        if len(args) == 3:
            print(f"Running '{args[1]}' with args {args[2]}:")
        print(run_python_file(*args))
        


if __name__ == "__main__":
    #test_get_files_info()
    #test_get_file_content()
    #test_write_file()
    test_run_python_file()
