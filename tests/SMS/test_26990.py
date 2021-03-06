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
    
    _TestMsg     = "Test message."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.messages   = Messages(self)

        self.num1 = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM_SHORT")
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Launch messages app.
        #
        self.messages.launch()
        
        #
        # Create and send a new test message.
        #
        self.messages.createAndSendSMS([self.num1], "Test message")
        
        #
        # The returned message won't come to this thread, so just tap the header.
        #
        x = self.UTILS.getElement(DOM.Messages.message_header, "Thread header (edit header)")
        x.tap()

        #
        # Verify that the options appear.
        #
        self.UTILS.waitForElements(DOM.Messages.header_call_btn, "Call button")
        self.UTILS.waitForElements(DOM.Messages.header_create_new_contact_btn, "Create new contact button")
        self.UTILS.waitForElements(DOM.Messages.header_add_to_contact_btn, "Add to existing contact button")
        self.UTILS.waitForElements(DOM.Messages.header_cancel_btn, "Cancel button")
                
        
        
        
        