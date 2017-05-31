"""
KTB Interface 
Copyright, Khai Ngo, 2017
No duplication or use without the author's permission
"""
import os
import requests
import json

COMMANDS = {"1"     :"Get all accounts",
            "2"     :"List all account id",
            "3"     :"Get an individual account info",
            "4"     :"Create an account",
            "5"     :"Update an account",
            "6"     :"Delete an account",
            "99"    :"List commands",
            "-1"    :"Quit" }
#NOTICE: Try to run the code with my API_KEY first, if it doesn't work then use yours
API_KEY = '6ae0131555a1884dd27093d45bc2dd9e'
class KTB_Interface(object):
    def __init__(self):
        os.system('clear')
        print "\t\t\t\tHi, Welcome To KTB Interface"
        self.help()
        self.run()

    def run(self):
        user_choice = self.checkError(raw_input("\nPlease enter the number of the command you want to select:"))
        
        while user_choice != -1:
            if user_choice:
                self.processCommand(user_choice)
                user_choice = self.checkError(raw_input("\nPlease enter the number of the next command you want to select:"))
            else:
                user_choice = self.checkError(raw_input("Invalid command, try again (type '99' for the list of commands): "))

    #Process the command based on the user_choice
    def processCommand(self, user_choice):
        if user_choice == 99:
            self.help()
        elif user_choice == 1:
            raw_mode = raw_input("What info you want to view ('all','account_id','type','nickname','reward','balance','customer_id'): ").replace(" ","")
            mode = raw_mode.split(',')
            url = 'http://api.reimaginebanking.com/accounts?key={}'.format(API_KEY)
            self.getAccountInfo(url, mode)
        elif user_choice == 2:
            url = 'http://api.reimaginebanking.com/accounts?key={}'.format(API_KEY)
            self.getAccountInfo(url,['account_id'])
        elif user_choice == 3:
            account_id = raw_input("Please enter an account ID:")
            url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(account_id,API_KEY)
            self.getAccountInfo(url)
        elif user_choice == 4:
            print Hello
            #TODO: Tomek's assignment
        elif user_choice == 5:
            #update account
            update_id = raw_input("Enter account ID you would like to update: ")
            url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(update_id,API_KEY)
            raw_update = raw_input("What object do you want to update? ('nickname', 'account number): ")
            update = raw_update.split(',')
            update_to = raw_input("Update to: ")
            self.updateAccount(url,update, update_to)
        elif user_choice == 6:
            #delete account
            target_id = raw_input("Enter account ID you would like to deleted ")
            url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(target_id,API_KEY)
            self.deleteAccount(url)
        
            
    def deleteAccount(self, url):
        response = requests.delete(url)
        if response.status_code == 404:
            print "Invalid ID"
        elif response.status_code == 200:
            print "Successfully Deleted Account"

    def updateAccount(self, url,update,update_to):
        if update == "nickname":
            payload = {
                    "nickname": "tesT"
                    }
        else:
            payload = {
                    "account_number": update_to
                    }
        response = requests.put(
                url,
                data=json.dumps(payload),
                headers={'content-type' : 'application/json'},
                )
        if response.status_code == 202:
            print "Successfully updated account"
        elif response.status_code == 404:
            print "Account does not exist"
        elif response.status_code == 400:
            print "Invalid fields to update"


    #Get info from account(s) based on the url and mode
    #   url : used to construct requests message   
    #   mode: what info you want to get ['all','account_id','type','nickname','reward','balance','customer_id']
    def getAccountInfo(self, url, mode = ['all']):
        response = requests.get(url)
        account_list = json.loads(response.text)
        if response.status_code == 200:
            if type(account_list) is list:
                for account in account_list:
                    self.printAccountInfo(account, mode)
                    print "-----------------------"
            else:
                self.printAccountInfo(account_list, mode)
        else:
            print "Invalid Account Id"


    def printAccountInfo(self,accountDict, mode = ['all']):
        if ('account_id' in mode) or ('all' in mode):
            print "Account_ID:{}".format(accountDict["_id"])
        if ('type' in mode) or ('all' in mode):
            print "Account_Type:{}".format(accountDict["type"])
        if ('nickname' in mode) or ('all' in mode):
            print "Account_Nickname:{}".format(accountDict["nickname"])
        if ('reward' in mode) or ('all' in mode):
            print "Account_Rewards:{}".format(accountDict["rewards"])
        if ('balance' in mode) or ('all' in mode):
            print "Account_Balance:{}".format(accountDict["balance"])
        if ('customer_id' in mode or 'all' in mode):
            print "Customer_ID:{}".format(accountDict["customer_id"])
      


    #Check if the user input is valid, it has to be only number and within the keyset of the commands
    def checkError(self,input):
        try:
            if input in COMMANDS:
                return int(input)
            else:
                return False
        except ValueError:
            return False

    def help(self):
        print "Here are the available commands: "
        self.printCommands()

    #Print available commands
    def printCommands(self):
        for key, command in sorted(COMMANDS.iteritems()):
            print " ({})\t: {}".format(key,command)
if __name__ == "__main__":
    run = KTB_Interface()
