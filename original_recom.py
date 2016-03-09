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
def topMatches(prefs, person, n = 5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other)
                for other in prefs if other !=  person]
#不是由其他元素吗直接就可以sort吗
    scores.sort()
    scores.reverse()
    return scores[0:n]



def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}

    simSums={}

    for other in prefs:

    # don't compare me to myself

        if other==person: continue

        sim=similarity(prefs,person,other)



        # ignore scores of zero or lower

        if sim<=0: continue

        for item in prefs[other]:

        
            if item not in prefs[person] or prefs[person][item]==0:

        # Similarity * Score

                totals.setdefault(item,0)

                totals[item]+=prefs[other][item]*sim

        # Sum of similarities

                simSums.setdefault(item,0)

                simSums[item]+=sim



  # Create the normalized list
    rankings=[(total/simSums[item],item) for item,total in totals.items()]



  # Return the sorted list

    rankings.sort()

    rankings.reverse()

    return rankings
def transformPrefs(prefs):
    result = {}
    for item in prefs:
        for it in prefs[item]:
            result.setdefault(it,{});
            result[it][item]=prefs[item][it]
    return result
def loadMovieLens(path='ml/'):
    moives = {}
    for line in open(path+'u.item'):#line
        (id,title) = line.split('|')[0:2]
        moives[id] = title

    prefs = {}
    for line in open(path+'u.data'):
        (user,moiveid,rating,ts) = line.split('\t')
        prefs.setdefault(user,{});
        prefs[user][moives[moiveid]] = float(rating)
        #movieid is important
    return prefs

