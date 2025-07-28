from functions.get_files_info import get_files_info


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
            print("Result for '{directory}' directory:")
        print(get_files_info(*args))


if __name__ == "__main__":
    test_get_files_info()
