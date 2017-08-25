
#Password strength checker : Create a function to accept a string  and verify if it conforms to the following format
#between 8 to 12 characters long, atleast 1 upper case character,
#atleast 1 number and 1 special character which can be one of '@','#','$','#' ,'%','&'


#Create a function to verify if password length is between 8 to 12 characters
def lengthCheck(password):
    password_length = len(password)
    if(password_length >= 8 or password_length <=12 ):
        return True
    else:
        print 'Password has to be between 8 to 12 characaters long'
        return False


#Create a function to verify if password has atleast 1 upper case character
def caseCheck(password):
    for letter in password:
        if letter.isupper():
            return True
    print 'Atleast 1 character has to be upper case'
    return False

#Create a function to verify if the password has atleast 1 number
def numberCheck(password):
    for letter in password:
        if letter.isdigit():
            return True
    print 'Need atleast 1 number in the password'
    return False


#Create a function to verify if the pass word has atleast 1 of '@','#','$','#' ,'%','&'
def specialCharCheck(password):
    for letter in password:
        if letter in ('@','#','$','#' ,'%','&'):
            return True
    print "Need one of the following '@','#','$','#' ,'%','&' characters in the password"
    return False


#PasswordChecker function which checks for all the password restrictions but calling their corresponding methods
def passwordChecker(password):
    if (lengthCheck(password) and caseCheck(password) and numberCheck(password) and specialCharCheck(password)):
        print 'Password is STRONG!!'


    else:
        print 'Password is WEAK!!'



password = raw_input('Enter Password >>')
passwordChecker(password)
