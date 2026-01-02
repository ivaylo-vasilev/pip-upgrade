# pip-upgrade
Python script to upgrade all installed packages using pip command
---

**pip_upgrade.py** is script written in *Python* that performs an upgrade to ***all*** installed packages using the **pip** command. I needed to have a solution to upgrade all the packages I am using with a single command. The tool that I use for installing, managing, and uninstalling the packages in my system is **pip** and I am working in a *virtualenv* with access to globally-installed packages. That is the most common way in Linux distributions. So I needed to "see" only the user-site packages or those installed within the virtualenv. Once I list them and find which ones need an upgrade I need a proper way to pass their names in **pip** and perform an upgrade for each one.

So my Python script, **pip_upgrade.py**, is doing all this with *a single command*:
```
$ pip_upgrade.py
```

It will get the outdated packages listing only the ones installed by the user within the virtualenv and after a confirmation will upgrade each of the packages. The upgrade is done by **pip** so no additional packages or programs are required for this script to run.

---

If you have any ideas or sugestions for additional features or improvements, do not hesitate to contact me.
