import wikipedia


page = wikipedia.page("chatbot")
p = page.content


fh = open("ChatbotText.txt", "w") 
 
fh.write(p) 
 
fh.close()
print("Ok")
