import re
import os


def bump_version():
    with open("setup.py") as f:
        s = f.read()
    m = re.search(r'version="(.*)\.(.*)\.(.*)",', s)
    v1, v2, v3 = m.groups()
    oldv = "{}.{}.{}".format(v1, v2, v3)
    newv = "{}.{}.{}".format(v1, v2, str(int(v3) + 1))
    print("Current version is: {}, write new version, ctrl-c to exit".format(oldv))
    ans = input(newv)
    if ans:
        newv = ans
    s = s.replace(oldv, newv)
    with open("setup.py", "w") as f:
        f.write(s)
    return newv


def release():
    v = bump_version()
    ans = input("version bumped, commiting?(Y/n)")
    if ans in ("", "y", "yes"):
        os.system("git add setup.py")
        os.system("git commit -m 'new release'")
        os.system("git tag {}".format(v))
        ans = input("change committed, push to server?(Y/n)")
        if ans in ("", "y", "yes"):
            os.system("git push")
            os.system("git push --tags")
        ans = input("upload to pip?(Y/n)")
        if ans in ("", "y", "yes"):
            os.system("python setup.py sdist upload")


if __name__ == "__main__":
    release()
