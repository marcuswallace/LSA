from LSA import LSA
import nltk

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

#the method test to make sure my object can parse and properly build a term document matrix
def test_parse_and_build(mylsa):
    for t in titles:
        mylsa.parse(t)
    mylsa.build()

    ##TODO test against term document from imported library

test_parse_and_build(mylsa)

