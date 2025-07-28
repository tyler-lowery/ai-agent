from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


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


if __name__ == "__main__":
    #test_get_files_info()
    test_get_file_content()
