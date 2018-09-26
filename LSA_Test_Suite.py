from LSA import LSA
import textmining


##Mock list of documents
titles =[
    "How to Make Money in Stocks: A Winning System in Good Times or Bad",
    "One Up On Wall Street: How to Use What You Already Know to Make Money in the Market",
    "Flash Boys: A Wall Street Revolt",
    "Reminiscences of a Stock Operator",
    "How to Avoid Loss and Earn Consistently in the Stock Market: An Easy-To-Understand and Practical Guide for Every Investor",
    "How I Made $2,000,000 In The Stock Market ",
    "The Warren Buffett Way: Investment Strategies of the World's Greatest Investor",
    "The Dhandho Investor: The Low-Risk Value Method to High Returns",
    "How to Make Money in Stocks: Complete Investing System"
]
#these values are ignored or skipped over in the parsing because they hold no value
stopwords = ['and','to','for','in','little','of','the','to', 'a']
ignorechars = ''',:'!$-'''

#intialize the object
mylsa = LSA(stopwords, ignorechars)
print "Object initalized running test"

def test_parse_and_build(mylsa):
    print "Begin parsing all documents"
    tdms = []
    for t in titles:
        mylsa.parse(t)
    print "Parsing Successful, Building text document matrix"
    mylsa.build()
    print "Build Successful, Comparing against Textmining TDM"

    tdm = textmining.TermDocumentMatrix()
    for t in titles:
        tdm.add_doc(t)


test_parse_and_build(mylsa)

