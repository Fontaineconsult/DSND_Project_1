import os


testdir = os.path.join(os.getcwd(), "testdir")


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

    return walk_dir(suffix, path)


if __name__ == "__main__":
    print("Searching testdir for files ending in .c")
    files = find_files(".c", testdir)
    print("The Following Files were found ending in .c")
    for file in files:
        print(file)




