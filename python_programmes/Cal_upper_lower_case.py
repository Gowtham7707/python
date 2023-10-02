

#Based on the String we can calculate Upper and Lower case

def string_test(str):
    d={'Upper':0,'Lower':0}
    for i in str:
        if i.isupper():
            d['Upper']+=1
        elif i.islower():
            d['Lower']+=1
        else:
            pass 
    print("upper case letters: ",d['Upper'])
    print("Lower case letters: ",d['Lower'])
string_test("This is Gowtham")               
