import os

print("*** Please make sure, you are passing the correct path ****")
wd_path = input("Enter a working directory path: ")


def main():
    def check_path():
        """
        This function checks if the user has passed a path.
        Otherwise it will use the default demo path.
        """
        if wd_path:
            return os.chdir(wd_path)
        else:
            return os.chdir("./files_demo")

    check_path()

    # This listdir() method from os module checks files in the current working directory.
    for f in os.listdir():
        # isfile() method checks if it is a file or not.
        if os.path.isfile(f):
            # This splitext() does as it says, splits the extension from file name.
            f_name, f_ext = os.path.splitext(f)
            new_name = f_name.replace(".", "-") + f_ext
            os.rename(f, new_name)


if __name__ == "__main__":
    main()
