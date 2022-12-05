import operator
letters =["a" , "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
stopWords = ['able', 'about', 'above', 'abroad', 'according', 'accordingly', 'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against', 'ago', 'ahead', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'alongside', 'already', 'also', 'although', 'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', "aren't", 'around', 'as', "a's", 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', "can't", 'caption', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', "c'mon", 'co', 'co.', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', "c's", 'currently', 'dare', "daren't", 'definitely', 'described', 'despite', 'did', "didn't", 'different', 'directly', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far', 'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'forever', 'former', 'formerly', 'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'had', "hadn't", 'half', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', "here's", 'hereupon', 'hers', 'herself', "he's", 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'hundred', "i'd", 'ie', 'if', 'ignored', "i'll", "i'm", 'immediate', 'in', 'inasmuch', 'inc', 'inc.', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", 'its', "it's", 'itself', "i've", 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked', 'likely', 'likewise', 'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', "mayn't", 'me', 'mean', 'meantime', 'meanwhile', 'merely', 'might', "mightn't", 'mine', 'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', "mustn't", 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', "needn't", 'needs', 'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'no-one', 'nor', 'normally', 'not', 'nothing', 'notwithstanding', 'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', "one's", 'only', 'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought', "oughtn't", 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'someday', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that's", "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', "there'd", 'therefore', 'therein', "there'll", "there're", 'theres', "there's", 'thereupon', "there've", 'these', 'they', "they'd", "they'll", "they're", "they've", 'thing', 'things', 'think', 'third', 'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', "t's", 'twice', 'two', 'un', 'under', 'underneath', 'undoing', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", 'welcome', 'well', "we'll", 'went', 'were', "we're", "weren't", "we've", 'what', 'whatever', "what'll", "what's", "what've", 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', "where's", 'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while', 'whilst', 'whither', 'who', "who'd", 'whoever', 'whole', "who'll", 'whom', 'whomever', "who's", 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', "won't", 'would', "wouldn't", 'yes', 'yet', 'you', "you'd", "you'll", 'your', "you're", 'yours', 'yourself', 'yourselves', "you've", 'zero', 'a', "how's", 'i', "when's", "why's", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'I', 'www', 'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt', 'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give', 'hasnt', 'herse', 'himse', 'interest', 'itse”', 'mill', 'move', 'myse”', 'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten', 'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance', 'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah', 'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent', 'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol', 'briefly', 'ca', 'date', 'ed', 'effect', 'et-al', 'ff', 'fix', 'gave', 'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately', 'importance', 'important', 'index', 'information', 'invention', 'itd', 'keys', 'kg', 'km', 'largely', 'lets', 'line', "'ll", 'means', 'mg', 'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted', 'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages', 'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran', 'readily', 'ref', 'refs', 'related', 'research', 'resulted', 'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'slightly', 'somethan', 'specifically', 'state', 'states', 'stop', 'strongly', 'substantially', 'successfully', 'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto', 'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til', 'tip', 'ts', 'ups', 'usefully', 'usefulness', "'ve", 'vol', 'vols', 'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words', 'world', 'youd', 'youre']

Book =  "book_1.txt"
Book_1 = "book_1.txt"
Book_2 = "book_2.txt"
Word_Order = 2
File_Output = "python homework output of first function.txt"
File_Output2 = "python homework output of second function.txt"
    


def Word_Order_Frequency_One_Book (Book, Word_Order, File_Output  ):
    
    # function stops if these conditions bloks cannot work out . 
    if (type(Book) != str) or ( Word_Order != 1 and Word_Order != 2 ) or ( type(File_Output) != str ) :        
        return
    
    try:
        f1 = open(Book, 'r',  encoding='utf-8-sig' )
        text = f1.read()        # text contains whole book as a string
        f1.close()
    except:
        return
    
    
        
    text = text.lower()
    textList = text.split()     # textList contains all words separately
    
    
    deleteWords = []        # contains words that will be deleted
    for i in range(0, len(textList)): 
        
        
        # without this if-blok , program cannot see some stop words .
        if ("." in textList[i] ) or ("“" in textList[i] ) or (":" in textList[i] ) or ('"' in textList[i] ) or (";" in textList[i] ) or ("," in textList[i] )  or ("(" in textList[i] )  or (")" in textList[i] )  or ("-" in textList[i] )  or ("_" in textList[i] )  or ("'" in textList[i] )  or ("!" in textList[i] )or ("]" in textList[i] ) or ("[" in textList[i] ) or ("}" in textList[i] ) or ("{" in textList[i] ) or ("|" in textList[i] ) or ("/" in textList[i] ) or ("”" in textList[i] ) or  ("#" in textList[i] ) or ("*" in textList[i] ) or ("@" in textList[i] ) or ("&" in textList[i] )  :
            j=0
            while j < len( textList[i] ):
                if textList[i][j] not in letters:
                
                    kelime = textList[i]
                    symbol = textList[i][j]
                    kelime = kelime.replace( symbol , "")
                    textList[i] = kelime
                    j-=1
                
                j+=1
          
            
        if textList[i] in stopWords:
            deleteWords.append(textList[i])
            
            
            
    for i in range(0, len(deleteWords)):
        textList.remove(deleteWords[i])
    # stop words were deleted .
    
   
    
    # delete unwanted symbols part
    i=0
    while i < len(textList):
        j=0
        while j < len( textList[i] ):
            if textList[i][j] not in letters:
                
                kelime = textList[i]
                symbol = textList[i][j]
                kelime = kelime.replace( symbol , "")
                textList[i] = kelime
                j-=1
                
            j+=1
        i+=1
        
    # textList was prepared correctly.    
        
        
    # what is Words_Order ?
    if Word_Order == 1:
                
        # these dictionary variables keep the words and their frequency .
        mydict = {}
        for i in range(0,len(textList)):
            kackere = 0
            kelime = textList[i]
        
            if (kelime not in mydict) and kelime != "":
                kackere += 1
                mydict.update( {kelime : kackere} )
                
            elif (kelime in mydict) and kelime != "" :
                kackere = mydict[ kelime ] + 1
                mydict[kelime] = kackere
        
        
        
    elif Word_Order == 2:
        
        mydict = {}
        for i in range(0, len(textList)-1 ):    # len(textList)-1
            kackere = 0
            if textList[i] != "" and textList[i+1] !="":
                
                kelime = textList[i] +" "+ textList[i+1]
                if (kelime not in mydict) and kelime != "":
                    kackere += 1
                    mydict.update( {kelime : kackere} )
                
                elif (kelime in mydict) and kelime != "" :
                    kackere = mydict[ kelime ] + 1
                    mydict[kelime] = kackere
            
            
            
        
        
    # function prints data into the file .        
    fOutput = open( File_Output , "w" ,  encoding='utf-8-sig')
    
    fOutput.write("| word      |  word      | \n")
    fOutput.write("| order     |  order     | \n")
    fOutput.write("| sequence  |  frequency | \n\n")
    
    
    # without this feature , program takes more than ten minutes . 
    sorted_D = dict (  sorted( mydict.items() , key= operator.itemgetter(1),reverse=True)   )
    
    keyList = list(sorted_D.keys())
    for i in range (0 , 200 ):   
        fOutput.write( keyList[i] )
        fOutput.write(" - - - - - - ")
        fOutput.write( str( sorted_D[ keyList[i] ] ) )
        fOutput.write("\n")
    
    fOutput.close()
      
def Word_Order_Frequency_Two_Books (Book_1, Book_2, Word_Order, File_Output2 ):
    
    # function stops if these conditions bloks cannot work out . 
    if (type(Book_1) != str) or (type(Book_2) != str) or ( Word_Order != 1 and Word_Order != 2 ) or ( type(File_Output) != str ) :        
        return
    
    try:
        f1 = open(Book_1, 'r',  encoding='utf-8-sig' )
        text1 = f1.read()        # text contains whole book as string
        f1.close()
    
        f2 = open(Book_2, 'r',  encoding='utf-8-sig' )
        text2 = f2.read()        # text contains whole book as string
        f2.close()
    except:
        return
    
    
    
    text1 = text1.lower()
    textList1 = text1.split()       # textLists contain all words separately
    
    text2 = text2.lower()
    textList2 = text2.split()
    
    
    
    
    deleteWords1 = []        # contains words that will be deleted
    for i in range(0, len(textList1)): 
        
        
        # without this if , program cannot see some stop words .
        if ("." in textList1[i] ) or ("“" in textList1[i] ) or (":" in textList1[i] ) or ('"' in textList1[i] ) or (";" in textList1[i] ) or ("," in textList1[i] )  or ("(" in textList1[i] )  or (")" in textList1[i] )  or ("-" in textList1[i] )  or ("_" in textList1[i] )  or ("'" in textList1[i] )  or ("!" in textList1[i] )or ("]" in textList1[i] ) or ("[" in textList1[i] ) or ("}" in textList1[i] ) or ("{" in textList1[i] ) or ("|" in textList1[i] ) or ("/" in textList1[i] ) or ("”" in textList1[i] ) or  ("#" in textList1[i] ) or ("*" in textList1[i] ) or ("@" in textList1[i] ) or ("&" in textList1[i] )  :
            j=0
            while j < len( textList1[i] ):
                if textList1[i][j] not in letters:
                
                    kelime = textList1[i]
                    symbol = textList1[i][j]
                    kelime = kelime.replace( symbol , "")
                    textList1[i] = kelime
                    j-=1
                
                j+=1
          
        if textList1[i] in stopWords:
            deleteWords1.append(textList1[i])
            
            
            
            
    deleteWords2 = []        # contains words that will be deleted
    for i in range(0, len(textList2)): 
        
        
        # without this if , program cannot see some stop words .
        if ("." in textList2[i] ) or ("“" in textList2[i] ) or (":" in textList2[i] ) or ('"' in textList2[i] ) or (";" in textList2[i] ) or ("," in textList2[i] )  or ("(" in textList2[i] )  or (")" in textList2[i] )  or ("-" in textList2[i] )  or ("_" in textList2[i] )  or ("'" in textList2[i] )  or ("!" in textList2[i] )or ("]" in textList2[i] ) or ("[" in textList2[i] ) or ("}" in textList2[i] ) or ("{" in textList2[i] ) or ("|" in textList2[i] ) or ("/" in textList2[i] ) or ("”" in textList2[i] ) or  ("#" in textList2[i] ) or ("*" in textList2[i] ) or ("@" in textList2[i] ) or ("&" in textList2[i] )  :
            j=0
            while j < len( textList2[i] ):
                if textList2[i][j] not in letters:
                
                    kelime = textList2[i]
                    symbol = textList2[i][j]
                    kelime = kelime.replace( symbol , "")
                    textList2[i] = kelime
                    j-=1
                
                j+=1
          
        if textList2[i] in stopWords:
            deleteWords2.append(textList2[i])   
            
            
            
            
            
    for i in range(0, len(deleteWords1)):
        textList1.remove(deleteWords1[i])
    # stop words were deleted for first book .

    for i in range(0, len(deleteWords2)):
        textList2.remove(deleteWords2[i])
    # stop words were deleted for second book .   


         


            
    # delete unwanted symbols part for first book .
    i=0
    while i < len(textList1):     
        j=0
        while j < len( textList1[i] ):
            if textList1[i][j] not in letters:
                
                kelime = textList1[i]
                symbol = textList1[i][j]
                kelime = kelime.replace( symbol , "")
                textList1[i] = kelime
                j-=1
                
            j+=1
        i+=1
        
        
    # delete unwanted symbols part for second book .
    i=0
    while i < len(textList2):      
        j=0
        while j < len( textList2[i] ):
            if textList2[i][j] not in letters:
                
                kelime = textList2[i]
                symbol = textList2[i][j]
                kelime = kelime.replace( symbol , "")
                textList2[i] = kelime
                j-=1
                
            j+=1
        i+=1        
    
    
    
    
    
    
    # what is Words_Order ?
    if Word_Order == 1:
        
        # these dictionary variables keep the words and their frequency for each book separately .
        mydict1 = {}
        for i in range(0,len(textList1)):
            kackere = 0
            kelime = textList1[i]
        
            if (kelime not in mydict1) and kelime != "":
                kackere += 1
                mydict1.update( {kelime : kackere} )
                
            elif (kelime in mydict1) and kelime != "" :
                kackere = mydict1[ kelime ] + 1
                mydict1[kelime] = kackere
        
        mydict2 = {}
        for i in range(0,len(textList2)):
            kackere = 0
            kelime = textList2[i]
        
            if (kelime not in mydict2) and kelime != "":
                kackere += 1
                mydict2.update( {kelime : kackere} )
                
            elif (kelime in mydict2) and kelime != "" :
                kackere = mydict2[ kelime ] + 1
                mydict2[kelime] = kackere
      
    
    
    
    
    elif Word_Order == 2:
        
        mydict1 = {}
        for i in range(0, len(textList1)-1 ):    
            kackere = 0
            if textList1[i] != "" and textList1[i+1] !="":
                
                kelime = textList1[i] +" "+ textList1[i+1]
                if (kelime not in mydict1) and kelime != "":
                    kackere += 1
                    mydict1.update( {kelime : kackere} )
                
                elif (kelime in mydict1) and kelime != "" :
                    kackere = mydict1[ kelime ] + 1
                    mydict1[kelime] = kackere
        
        mydict2 = {}
        for i in range(0, len(textList2)-1 ):    
            kackere = 0
            if textList2[i] != "" and textList2[i+1] !="":
                
                kelime = textList2[i] +" "+ textList2[i+1]
                if (kelime not in mydict2) and kelime != "":
                    kackere += 1
                    mydict2.update( {kelime : kackere} )
                
                elif (kelime in mydict2) and kelime != "" :
                    kackere = mydict2[ kelime ] + 1
                    mydict2[kelime] = kackere
        
        
        
        
    # program finds same words in two dictionary .
    # same words and their values are added to mydictOrt dictionary .
    mydictOrt = {}  
    
    keyList1 = list( mydict1.keys() )
    keyList2 = list( mydict2.keys() )
        
    if len(keyList1) < len(keyList2):     # I create my new dictionary with smaller dictionary's size in order to avoid to get OutOfRange ERROR .
        length = len(keyList1)
        
        for k in range(0 , length):
            
            if keyList1[k] in keyList2:
                nmbOrt = mydict1[ keyList1[k] ]  +  mydict2[ keyList1[k] ]
                mydictOrt.update( { keyList1[k] : nmbOrt } )
                
                
    else:
        length = len(keyList2)
        
        for k in range(0 , length):
            
            if keyList2[k] in keyList1:
                nmbOrt = mydict2[ keyList2[k] ]  + mydict1[ keyList2[k] ]
                mydictOrt.update( { keyList2[k] : nmbOrt } )
    
    
    
     
     
     
        
        # program prints data into the file .
    fOutput = open( File_Output , "w" ,  encoding='utf-8-sig')
    
    
    fOutput.write("| total     |  Book 1     |  Book 2     |  word        | \n")
    fOutput.write("| order     |  order      |  order      |  order       | \n")
    fOutput.write("| frequency |  frequency  | frequency   |  sequence    | \n\n")
    
    
    sorted_mydictOrt = dict( sorted( mydictOrt.items() , key= operator.itemgetter(1),reverse=True)  )
    keyListOrt = list( sorted_mydictOrt.keys() )
    
    for k in range(0 , len(keyListOrt) ):
        fOutput.write( str( sorted_mydictOrt[ keyListOrt[k] ] ) )
        fOutput.write(" - - - - - - ")
        fOutput.write( str( mydict1[ keyListOrt[k] ] ) )
        fOutput.write(" - - - - - - ")
        fOutput.write( str( mydict2[ keyListOrt[k] ] ) )
        fOutput.write(" - - - - - - - ")
        fOutput.write( keyListOrt[k] )
        fOutput.write("\n")
    
    
    fOutput.close()        
        
  
Word_Order_Frequency_One_Book (Book, Word_Order ,File_Output )

#Word_Order_Frequency_Two_Books (Book_1, Book_2, Word_Order, File_Output)





