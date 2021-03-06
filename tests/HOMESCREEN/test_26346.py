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

class test_main(GaiaTestCase):
    
    _URL         = "http://everlong.org/mozilla/packaged/"
    _appName     = "cool packaged app"
    _appOK       = True
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.Browser    = Browser(self)
        
        
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Ensure we have a connection.
        #
        self.UTILS.getNetworkConnection()
        
        #
        # Uninstall the app (if need be).
        #
        self.UTILS.uninstallApp(self._appName)
 
        #
        # Open the browser app.
        #
        self.Browser.launch()
         
        #
        # Open our URL.
        #
        self.Browser.open_url(self._URL)
         
        #
        # Install the app (this is a 'one-off' thing, so just keep the DOM spec here).
        #
        x = ('id', 'install-app') 
        install_btn = self.UTILS.getElement(x, "Install an app button")
        install_btn.tap()
         
        # Install button on the splash screen (switch to main frame to 'see' this).
        self.marionette.switch_to_frame()
 
        x = ('id', 'app-install-install-button')        
        install_btn = self.UTILS.getElement(x, "Install button", True, 30)
        install_btn.tap()
         
        # ... and switch back to brwoser to see the next splash screen(!)
        self.UTILS.switchToFrame(*DOM.Browser.frame_locator)
        btn = self.UTILS.getElement(DOM.GLOBAL.modal_alert_ok, "Ok button")
        btn.tap()
 
        #
        # Remove the app.
        #
        self.UTILS.uninstallApp(self._appName)
