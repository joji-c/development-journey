email_path="python-works\\file_works\\email_process\\email.txt"
gmail_path="python-works\\file_works\\email_process\\gmail.txt"
outloo_path="python-works\\file_works\\email_process\\outlook.txt"
yahoo_path="python-works\\file_works\\email_process\\yahoo.txt"

fr_email=open(email_path,"r")
fw_gmail=open(gmail_path,"w")
fw_outlook=open(outloo_path,"w")
fw_yahoo=open(yahoo_path,"w")

for line in fr_email:
    mail=line.rstrip("\n")
    if mail.endswith("@gmail.com"):
        fw_gmail.write(mail+"\n")
    elif mail.endswith("@outlook.com"):
        fw_outlook.write(mail+"\n")
    elif mail.endswith("@yahoo.com"):
        fw_yahoo.write(mail+"\n")

print("program ends")
fr_email.close()
fw_gmail.close()
fw_outlook.close()
fw_yahoo.close()
