# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
#email_three = open("email_three.txt", "r").read()
#email_four = open("email_four.txt", "r").read()

#print(email_one)
#print(email_two)
#print(email_three)
#print(email_four)

#defining lists
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#function replace_censor_term takes one parameter, censor_term, and censors the term from email one.
#It will censor the terms with asterisks (*) for each character.

def replace_censor_term(censor_term):
    replacing_string = ""
    for character in censor_term:
        replacing_string += "*"
    censored_email_one = email_one.replace(censor_term, replacing_string)
    return censored_email_one

#print(replace_censor_term("learning algorithms"))

def replace_censor_list(censor_list):
    for term in censor_list:
        replacing_string = ""
        for character in term:
            replacing_string += "*"
            censored_email_two = email_two.replace(term, replacing_string)
    return censored_email_two


print(replace_censor_list(proprietary_terms))
