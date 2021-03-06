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
from tests._mock_data.contacts import MockContacts

class test_main(GaiaTestCase):
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = Contacts(self)
        self.messages   = Messages(self)

        
    def tearDown(self):
        self.UTILS.reportResults()

    def test_run(self):
    
        self.contacts.launch()
        self.messages.launch()
        self.UTILS.touchHomeButton()
        time.sleep(1)
        
        self.UTILS.holdHomeButton()
        
        self.UTILS.waitForElements(DOM.Home.cards_view, "App 'cards' list (task switcher)")
        
        x = self.UTILS.screenShotOnErr()
        self.UTILS.logResult("info", "Screenshot:", x)