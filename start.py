import os
import emailspammer.utils as utils
import emailspammer.spammer as spammer

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
    
    # Start the main functionality of the program

    

    print(from_fn[0].strip())
    print(type(from_fn))




if __name__ == "__main__":
    ENTIRE_PROGRAM()



