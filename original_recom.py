#---coding: utf-8---
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,

 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 

 'The Night Listener': 3.0},

'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 

 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 

 'You, Me and Dupree': 3.5}, 

'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,

 'Superman Returns': 3.5, 'The Night Listener': 4.0},

'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,

 'The Night Listener': 4.5, 'Superman Returns': 4.0, 

 'You, Me and Dupree': 2.5},

'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 

 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,

 'You, Me and Dupree': 2.0}, 

'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,

 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},

'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

def sim_distance(prefs, person1, person2):
# 函数名称需要搞清楚啊
    sum2Square = sum([pow( prefs[person1][item] - prefs[person2][item] , 2)
                for item in prefs[person1] if item in prefs[person2]] )
    return 1/(1 + sqrt(sum2Square))

def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
# 为什么不去直接用列表呢，不懂
# 把数组元素给忘了。。。`
    n = len(si)

    if n==0:
        return 1
# 不是强制换行的么
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sum1Sq = sum([pow(prefs[p1][it] , 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it] , 2) for it in si])

    sum_of_multiply = sum([prefs[p1][it] * prefs[p2][it]
                    for it in si ])

    upper = sum_of_multiply - sum1 * sum2/n
    lower = (sum1Sq - sum1 * sum1/n) * (sum2Sq - sum2 * sum2/n)
    if lower==0:
        return 0

    return upper/sqrt(lower)
