# Copyright (C) Check Point Software Technologies LTD.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature

class AndroidInstalledApps(Signature):
    name = "application_installed_app"
    description = "Application installed  App (Dynamic)"
    severity = 2
    categories = ["android"]
    authors = ["Check Point Software Technologies LTD"]
    minimum = "0.5"

    def run(self):
        try:
            if "android/app/ApplicationPackageManager->installPackage" in self.results["droidmon"]:
                return True
            else:
                return False
        except:
            return False
#TODO:Add new signature