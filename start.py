import os
import emailspammer.utils as utils
import emailspammer.spammer as spammer
from random import choice as rand_choice

def ENTIRE_PROGRAM():
    from_fn = "from.txt"
    to_fn = "to.txt"
    found_files = True
    # This is the default option
    if ((os.path.exists(from_fn)) and (os.path.exists(to_fn))) == False:
        found_files = False
    
    # If the default doesnt exit
    if found_files == False:
        from_fn = input("+ Enter the *from* email and password list file path: ")
        to_fn = input("+ Enter the *to* email file path or email address: ")
        try:
            splitted = to_fn.lower().split("@")
            print("+ To:", to_fn)
        except:
            with open(to_fn, "r", encoding="utf-8") as to_email_addr_file:
                to_fn = to_email_addr_file.read()
            print("+ To:", to_fn)
        with open(from_fn, "r", encoding="utf-8") as from_email_addr_file:
            from_fn = from_email_addr_file.readlines()

    # If default exits
    if found_files == True:
        with open(from_fn, "r", encoding="utf-8") as from_email_addr_file:
            from_fn = from_email_addr_file.readlines()
        with open(to_fn, "r", encoding="utf-8") as to_email_addr_file:
            to_fn = to_email_addr_file.read()
    
    # Clean versions if the email:pwd list
    all_emails_list = []
    for one_email in all_emails_list:
            all_emails_list.append((one_email.strip()))

    # Finding the email body
    # no_email_text_files_list = ["from.txt", "to.txt"]    
    # all_text_files = []
    # for one_file in os.listdir(os.getcwd()):
    #     if one_file.endswith("txt"):
    #         if (one_file.lower() in no_email_text_files_list) == False:
    #             all_text_files.append()
    all_text_files = []
    for one_file in os.listdir(os.getcwd()+"/emails"):
        all_text_files.append(str(one_file))

    # Sending the email address with a randomly picked email body and a subject
    for one_single_email in all_emails_list:
        now_using_file = rand_choice(all_text_files)
        with open(f"/emails/{now_using_file}", "r", encoding="utf-8") as email_bodey_content_file:
            email_body_content = email_bodey_content_file.read()
        spammer.send_email(email_address=str(one_single_email).split(":")[0],
                          email_password=str(one_single_email).split(":")[1],
                          to_email_address=str(to_fn),
                          subject=str(now_using_file),
                          body=str(email_body_content)
                          )

if __name__ == "__main__":
    ENTIRE_PROGRAM()



