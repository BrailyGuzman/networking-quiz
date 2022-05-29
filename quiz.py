import time

print("Welcome To The Networking Quiz! \nYou are Able to research any answers you don't know, remember that we learn from our mistakes! :)")

ready = input("Are you ready? Y/N: ")
if ready == "Y" or "y":
    print("Alright! Starting The 10 Questions Quiz!")
else:
    quit()



def quiz():
    question_1 = "1) What does IP stands for?"
    print(question_1)
    response_1 = input("Enter: ")
    if (response_1) == "Internet Protocol" or "internet protocol":
        print("Correct!")
    else:
        print("Incorrect!")
    
    time.sleep(1)

    question_2 = "2) What does TCP stands for?"
    print(question_2)
    response_2 = input("Enter: ")
    if (response_2) == "Internet Protocol" or "internet protocol":
        print("Correct!")
    else:
        print("Incorrect!")

    time.sleep(1)

    question_3 = "3) What does UDP stands for?"
    print(question_3)
    response_3 = input("Enter: ")
    if (response_3) == "User Datagram Protocol" or "user datagram protocol":
        print("Correct!")
    else:
        print("Incorrect!")
    
    time.sleep(1)

    question_4 = "4) What does DNS stands for?"
    print(question_4)
    response_4 = input("Enter: ")
    if (response_4) == "Domain Name System" or "domain name system":
        print("Correct!")
    else:
        print("Incorrect!")
    
    time.sleep(1)

    question_5 = "5) What does HTTP stands for?"
    print(question_5)
    response_5 = input("Enter: ")
    if (response_5) == "Hypertext Transfer Protocol" or "hypertext transfer protocol":
        print("Correct!")
    else:
        print("Incorrect!")

    time.sleep(1)

    question_6 = "6) What does OSI stands for?"
    print(question_6)
    response_6 = input("Enter: ")
    if (response_6) == "Open System Protocol" or "open system protocol":
        print("Correct!")
    else:
        print("Incorrect!")
    
    time.sleep(1)

    question_7 = "7) What does VPN stands for?"
    print(question_7)
    response_7 = input("Enter: ")
    if (response_7) == "Virtual Private Network" or "virtual private network":
        print("Correct!")
    else:
        print("Incorrect!")
    
    time.sleep(1)

    question_8 = "8) What does DHCP stand for?"
    print(question_8)
    response_8 = input("Enter: ")
    if (response_8) == "Dynamic Host Configuration Protocol" or "dynamic host configuration protocol":
        print("Correct!")
    else:
        print("Incorrect!")
    
    time.sleep(1)

    question_9 = "9) What does LAN stand for?"
    print(question_9)
    response_9 = input("Enter: ")
    if response_9 == "Local Area Network" or "local area network":
        print("Correct!")
    else:
        print("Incorrect!")
    
    time.sleep(1)

    question_10 = "10) What does FTP stand for?"
    print(question_10)
    response_10 = input("Enter: ")
    if (response_10) == "File Transfer Protocol" or "file transfer protocol":
        print("Correct")
    else:
        print("Incorrect!")
    
    time.sleep(1)
    print("You Have Completed The 10 Networking Questions Quiz")
    time.sleep(3)
    quit()
quiz()
