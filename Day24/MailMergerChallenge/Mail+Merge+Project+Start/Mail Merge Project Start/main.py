#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f1 = open(r"Day24\MailMergerChallenge\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt")
letter = f1.read()
f2 = open(r"Day24\MailMergerChallenge\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt")
names = f2.readlines()
for name in names:
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    with open(f"Day24/MailMergerChallenge/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/for{name}.txt","w") as f:
        f.write(new_letter)
        f.close()
f1.close()
f2.close()  