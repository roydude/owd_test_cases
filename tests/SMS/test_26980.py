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
    
    _TestMsg     = "Test message."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.messages   = Messages(self)
        self.Email      = Email(self)

        self.USER1  = self.UTILS.get_os_variable("GMAIL_1_USER")
        self.EMAIL1 = self.UTILS.get_os_variable("GMAIL_1_EMAIL")
        self.PASS1  = self.UTILS.get_os_variable("GMAIL_1_PASS")
         
        self.num1 = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM")
        self.emailAddy = self.UTILS.get_os_variable("GMAIL_2_EMAIL")

        self.cont = MockContacts().Contact_1
        self.cont["email"]["value"] = self.emailAddy
        self.data_layer.insert_contact(self.cont)        
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Set up email account.
        #
        self.UTILS.getNetworkConnection()
        
        self.Email.launch()
        self.Email.setupAccount(self.USER1, self.EMAIL1, self.PASS1)
 
        #
        # Launch messages app.
        #
        self.messages.launch()
        
        #
        # Create and send a new test message.
        #
        self.messages.createAndSendSMS([self.num1], "Email %s one." % self.emailAddy)
        x = self.messages.waitForReceivedMsgInThisThread()
        
        #
        # Tap the email link.
        #
        _link = x.find_element("tag name", "a")
        _link.tap()
        
        #
        # Switch to email frame and verify the email address is in the To field.
        #
        self.UTILS.switchToFrame(*DOM.Email.frame_locator)
        x = self.UTILS.getElement(DOM.Email.compose_to_from_contacts, "To field")
        self.UTILS.TEST(x.text == self.emailAddy, 
                        "To field contains '%s' (it was '%s')." %
                        (self.emailAddy, self.emailAddy))