# Copyright (C) Check Point Software Technologies LTD.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature

class AndroidRegisteredReceiver(Signature):
    name = "application_registered_receiver_runtime"
    description = "Application Registered Receiver In Runtime (Dynamic)"
    severity = 2
    categories = ["android"]
    authors = ["Check Point Software Technologies LTD"]
    minimum = "0.5"

    def run(self):
        try:
            if "registered_receivers" in self.results["droidmon"]:
                return True
            else:
                return False
        except:
            return False
