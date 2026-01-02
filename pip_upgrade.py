#!/usr/bin/env python3

import argparse
import subprocess
import json
import sys

parser = argparse.ArgumentParser(prog="pip_upgrade", description="Python packages upgrade script", epilog="(c)Ivaylo Vasilev")
parser.add_argument("--version", action="version", version="Python packages upgrade script v0.1 | (c)Ivaylo Vasilev", help="show program version")
args = parser.parse_args()


def main():
    # convert the returned string from get_outdated_packages() to JSON object
    outdated_packages = json.loads(get_outdated_packages())
    if len(outdated_packages) == 0:
        print("No packages to upgrade")
        sys.exit(0)
    # make a list with the packages for upgrade
    print("Package(s) to upgrade:")
    print("=" * 22)
    packages = []
    for key in outdated_packages:
        print(f"{key['name']}: {key['version']} -> {key['latest_version']} ({key['latest_filetype']})")
        packages.append(key['name'])
    
    # upgrade each package from the list
    confirmation = input("Upgrade package(s)? [y/n]: ").strip().lower()
    if confirmation == "y":
        for package in packages:
            upgrade_package(package)
    elif confirmation == "n":
        print("No package(s) will be upgraded")
        sys.exit(0)
    else:
        print("error: invalid input")
        sys.exit(1)


# list the outdated Python packages using pip
# if in virtualenv with global access will not list the globally-installed packages
def get_outdated_packages():
    command = "pip list --local --outdated --format=json"
    try:
        outdated_pkgs = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    except subprocess.CalledProcessError:
        print("error: check for packages upgrade failed")
        sys.exit(1)

    # return only the command output from the CompletedProcess object
    return outdated_pkgs.stdout.decode()


def upgrade_package(package):
    command = f"pip install --upgrade {package}"
    subprocess.run(command, shell=True, stdout=None, stderr=None)

    return


if __name__ == "__main__":
    main()
