#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from gaiatest   import GaiaTestCase
from OWDTestToolkit import *

#
# Imports particular to this test case.
#
import time

class test_main(GaiaTestCase):

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS     = UTILS(self)

        self.wifi_name  = self.UTILS.get_os_variable("GLOBAL_WIFI_NAME")
        self.wifi_user  = self.UTILS.get_os_variable("GLOBAL_WIFI_USERNAME")
        self.wifi_pass  = self.UTILS.get_os_variable("GLOBAL_WIFI_PASSWORD")
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Data conn icon is not in status bar yet.
        #
        self.data_layer.disable_wifi()
        
        self.UTILS.waitForNotElements(DOM.Statusbar.wifi, "Wifi icon in statusbar")
        self.UTILS.TEST(self.UTILS.isNetworkTypeEnabled("wifi") == False,
                         "Wifi is disabled before we start this test.")

        #
        # Enable wifi mode.
        #
        self.UTILS.toggleViaStatusBar("wifi")
        
        #
        # Connect to the wifi.
        #
        self.Settings.tap_wifi_network_name(self.wifi_name, self.wifi_user, self.wifi_pass)
           
        #
        # Tap specific wifi network (if it's not already connected).
        #
        self.UTILS.TEST(
                self.Settings.checkWifiLisetedAsConnected(self.wifi_name),
                "Wifi '" + self.wifi_name + "' is listed as 'connected' in wifi settings.", True)
        
        self.UTILS.goHome()

        #
        # Data icon is no longer visible in status bar.
        #
        self.UTILS.waitForElements(DOM.Statusbar.wifi, "Wifi icon in statusbar", True, 20, False)
        
        #
        # Disable wifi mode.
        #
        self.UTILS.toggleViaStatusBar("wifi")
        
        #
        # Data icon is no longer visible in status bar.
        #
        self.UTILS.waitForNotElements(DOM.Statusbar.wifi, "Wifi icon in statusbar")
        