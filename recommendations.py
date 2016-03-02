#---coding: utf-8---
import recom1
from math import sqrt
pros = recom1.recom()

title = ['合计','家庭户','集体户','人口','人口（男）','人口（女）','性别比','家庭户','家庭户(男)','家庭户(女)','家庭户(性别比)','集体户','集体户(男)','集体户(女)','性别比(集体户)','户规模']
def sim_distance(prefs,person1, person2):
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item] , 2)
                         for item in range(0,16)])
    return 1/(1 + sqrt(sum_of_squares))

def sim_pearson(prefs, p1, p2):
    sum1 = sum([prefs[p1][it] for it in range(0, 16)]) 
    sum2 = sum([prefs[p2][it] for it in range(0, 16)])

    sum1Sq = sum([pow(prefs[p1][it], 2) for it in range(0, 16)])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in range(0, 16)])

    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in range(0, 16)])

    num = pSum - (sum1 * sum2/16)
    den = sqrt((sum1Sq - pow(sum1, 2)/16) * (sum2Sq - pow(sum2, 2)/16))

    r = num/den
    return r
def topMatches(prefs, person, n=5, similarity = sim_pearson):
    scores = [(similarity(prefs,person,other), other)
                for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]
