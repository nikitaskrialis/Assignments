import urllib
import json
from pprint import pprint

# epistrefei ton arithmo apo likes, followers, following, tweets analoga tis parametrous
# pou tha dwsoume. Oi arithmoi pou theloume briskontai panta sto telos tou prwtou string
# ths listas pou dimiourgeitai me kathe split(). Tous diabazoume ws string tous metatrepoume
# se arithmous kai tous epistrefoume sto kyriws programma
def getNumber(s, split):
    temp = s.split(split)
    tweets = ''
    count = len(temp[0])-1
    while temp[0][count] != '"':
        if temp[0][count] != ',':
            tweets += temp[0][count]
        count-=1
    tweets = tweets[::-1]
    return int(tweets)


def main():
    profile1 = raw_input('Give first tweet profile:')
    profile1 = profile1.replace('@','')
    profile2 = raw_input('Give second tweet profile:')
    profile2 = profile2.replace('@','')
    link = "https://twitter.com/" + profile1
    f1 = urllib.urlopen(link)
    # bazoume to periexomeno tou arxeiou se string apo opou tha kanoume parsing
    myfile1 = f1.read()
    link = "https://twitter.com/" + profile2
    f2 = urllib.urlopen(link)
    # bazoume to periexomeno tou arxeiou se string apo opou tha kanoume parsing
    myfile2 = f2.read()
    # oi parametroi gia ta split pou tha kanoume
    tweets = ' Tweets" '
    following = ' Following" '
    followers = ' Followers" '
    likes = ' Likes" '
    count1 = count2 = 0
    num1 = getNumber(myfile1, tweets)
    num2 = getNumber(myfile2, tweets)
    if num1 > num2:
        count1 += 1
    else:
        count2 +=1
    num1 = getNumber(myfile1, following)
    num2 = getNumber(myfile2, following)
    if num1 > num2:
        count1 += 1
    else:
        count2 +=1    
    num1 = getNumber(myfile1, followers)
    num2 = getNumber(myfile2, followers)
    if num1 > num2:
        count1 += 1
    else:
        count2 +=1
    num1 = getNumber(myfile1, likes)
    num2 = getNumber(myfile2, likes)
    if num1 > num2:
        count1 += 1
    else:
        count2 +=1

    print 'Score ' + str(count1) + '-' + str(count2)
    
main()
