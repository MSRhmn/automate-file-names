import os


def main():
    os.chdir("./files_demo")

    for f in os.listdir():
        if os.path.isfile(f):
            f_name, f_ext = os.path.splitext(f)
            new_name = f_name.replace(".", "-") + f_ext
            os.rename(f, new_name)


if __name__ == "__main__":
    main()
