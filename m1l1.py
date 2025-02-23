words ={
    "CRINGE": "an emmbarrasing action",
    "LOL": "laughing out loud"}
while True:
    text =input("write unnown word(all capital letters)")
    if text in words.keys():
        print(words[text])
    else:
        print("word not in dictionary, add it?")
      
        #command = input() DOESNT WORK
        #if command == "yes":
            #word = input("word")
            #meaning = input("meaning")
            #words.update({word : meaning})
        #else:
            
