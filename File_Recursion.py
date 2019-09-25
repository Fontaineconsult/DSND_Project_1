import os


testdir = os.path.join(os.getcwd(), "testdir")
testdir_1 = os.path.join(os.getcwd(), "testdir_1")
testdir_2 = os.path.join(os.getcwd(), "testdir_2")

def find_files(suffix, path):




    def walk_dir(suffix, path):

        files = []

        for each in os.listdir(path):
            test_path = os.path.join(path, each)
            if os.path.isdir(test_path):

                next_dir = walk_dir(suffix, test_path)
                for dir in next_dir:
                    files.append(dir)

            if os.path.isfile(test_path):

                if each[-2:] == suffix:
                    files.append(os.path.join(test_path, each))
        return files

    files = walk_dir(suffix, path)

    if len(files) == 0:
        return "No {} found".format(suffix)
    else:
        return files


if __name__ == "__main__":
    print("Searching testdir for files ending in .c")
    files = find_files(".c", testdir)
    print("The Following Files were found ending in .c")
    for file in files:
        print(file)

    print("\n")

    print("Searching testdir_1 for files ending in .c. testdir_1 includes files without extensions and invalid extensions")
    files = find_files(".c", testdir_1)
    print("The Following Files were found ending in .c")
    for file in files:
        print(file)

    print("\n")

    print("Searching testdir_2 for files ending in .c. testdir_2 contains no .C files")
    files = find_files(".c", testdir_2)
    print("The Following Files were found ending in .c")
    print(files)