# CS61002: Algorithms and Programming 1 
# Name: Shiva Jaligama
# Date: 10/28/2016
# Lab: project1.py


import glob
l =[]
g = glob.glob('*.txt')
p ={}
q = 0
def compute(d):
    r = []
    s = []
    #It asks to enter number of questions we would like to have
    y = int(input('Enter the total number of questions: '))
    j=True
    while j:
        if y > len(d):
            #If entered number exceedes total number of questions
            print 'Invalid number of questions'
            y = int(input('Enter the total number of questions: '))
        else:
            j=False
    for input1,output1 in d.iteritems():
        #It asks meaning of the word from text file
        print 'What is the meaning of '+ input1 +' in spanish'
        z = raw_input('The answer is: ')
        if z == output1:
            global q
            print 'The entered answer is correct answer'
            q=q+1
        else:
            print' The entered answer is wrong answer'
            #These two appends wrong answer into list
            r.append(input1)
            s.append(output1)
            q=q+1
        if q >= y:
            print 'The quiz is completed'
            break
        
    f_open = open("wrong.txt","w")
    for i,j in enumerate(r):
        wrong = r[i]+"-"+s[i]+'\n'
        f_open.write(wrong)
    f_open.close()
    
def check():
    global l
    lambda s
    while True:
        #This reads the filename
        x = raw_input('enter the filename: ')
        
        if x in g:
            #this prints the file that is selected
            print 'the selected file is: ',x
            f = open(x)
            for vocab in f.readlines():
                print vocab
                l = map(s: s.strip(), l)
                print s
                print l
                #Converting to dictionary
                d = dict(map(str,a.split('-')) for a in l)
                #It print the total words
            print "the total number of words in file is: ",len(l)
            compute(d)
            break
        else:
            print 'the file is unavailable'
check()

    


