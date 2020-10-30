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
#proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#function replace_censor_term takes one parameter, censor_term, and censors the term from email one.
#It will censor the terms with asterisks (*) for each character. It will add a space if censor term has a space.

def censor_one(input_text, censor_term):
    censored_item = ""
    for i in range(0, len(censor_term)):
        if censor_term[i] == " ":
            censored_item += " "
        else:
            censored_item += "*"
    return input_text.replace(censor_term, censored_item)


print(censor_one(email_one, "learning algorithms"))

#this was my initial try which worked but it also added an asterisk where there was a space
#def censor_one(input_text, censor_term):
#    censored_item = ""
#    for i in range(0, len(censor_term)):
#            censored_item += "*"
#    censored_email_one = input_text.replace(censor_term, censored_item)
#    return censored_email_one

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_two(input_text, censor_list):
    for word in censor_list:
        censored_word = ""
        for i in range(0, len(word)):
            if word[i] == " ":
                censored_word += " "
            else:
                censored_word += "X"
        input_text = input_text.replace(word, censored_word)
    return input_text


print(censor_two(email_two, proprietary_terms))
