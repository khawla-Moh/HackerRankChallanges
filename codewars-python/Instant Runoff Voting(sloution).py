from collections import Counter

def runoff(voters):
    while voters[0]:
        poll = Counter(ballot[0] for ballot in voters)
        winner, maxscore = max(poll.items(), key = lambda x: x[1])
        minscore = min(poll.values())
        if maxscore * 2 > len(voters):
            return winner
        voters = [[c for c in voter if poll[c] > minscore] for voter in voters]




def stage_counter(ballots):
    counts = {}
    for ballot in ballots:
        vote = ballot[0]
        if vote in counts:
            counts[vote] += 1
        else:
            counts[vote] = 1
    candidates = set()
    for ballot in ballots:
        candidates.update(ballot)
    for not_represented in set(candidates)-set(counts):
        counts[not_represented] = 0
    return counts


def get_winners(ballots):
    counts = stage_counter(ballots)

    max_count = max(counts.values())
    num_counts = sum(counts.values())

    potential_winners = [candidate for (candidate, count) in counts.items()
                         if count == max_count]

    if max_count >= num_counts/2 and len(potential_winners) == 1:
        return potential_winners[0]
    else:
        return []


def get_losers(ballots):
    counts = stage_counter(ballots)

    min_count = min(counts.values())

    potential_losers = [candidate for (candidate, count) in counts.items()
                        if count == min_count]

    if len(potential_losers) == len(counts):
        return potential_losers
    else:
        return potential_losers


def remove_candidate(ballots, candidate):
    for ballot in ballots:
        ballot.remove(candidate)


def runoff(ballots):
    print(stage_counter(ballots))
    while True:
        winners = get_winners(ballots)
        if winners:
            break
        losers = get_losers(ballots)
        if len(losers) == len(ballots[0]):
            return None
        print('=> Losers:', losers)
        for loser in losers:
            remove_candidate(ballots, loser)
    print("Winners: ", winners)
    return winners

#=====================================
from collections import Counter

def runoff(voters):
    numVoters = len(voters)
    while voters[0]:
        c = Counter( voters[i][0] for i in range(numVoters) )
        
        maxVote = max(c.values())
        if maxVote > numVoters/2:
            return [elt for elt in c if c[elt] == maxVote][0]
        
        for k in set(c.keys()) ^ set(voters[0]): c[k] = 0   # add those who addn't receive any "first choice vote"
        minVote = min(c.values())
        voters = [[ p for p in v if not p in [elt for elt in c if c[elt] == minVote] ] for v in voters]
        
    return None
def runoff(voters):
    if voters == []:
        return None
    elif len(voters[0]) == 1:
        return voters[0][0]
    voters_dict = {elem: [x[0] for x in voters].count(elem) for elem in voters[0]}
    expelled = sorted([voters_dict.get(x) for x in voters_dict])[0]
    return runoff([i for i in [[x for x in choices if
                                voters_dict.get(x) != expelled] for choices in voters] if i != []])
#====================================
from collections import Counter
def runoff(voters):
    while voters and len(voters[0]) > 1:
        tally = Counter([b[0] for b in voters])
        kick = min(tally[v] for v in voters[0])
        for b in voters: b[:] = [v for v in b if tally[v] > kick]
    return voters[0][0] if voters[0] else None
    

def runoff(voters):
    while voters and voters[0]:
        candidates = voters[0].copy()
        counts = {c:0 for c in candidates}
        for v in voters:
            counts[v[0]] += 1
        least = min(counts.values())
        for c in candidates:
            if counts[c] > len(voters) / 2.0:
                return c
            if counts[c] == least:
                for v in voters:
                    v.remove(c)
    return None


def runoff(votes):
    voters, candidates = len(votes), votes[0]
    while votes:
        round = [vote[0] for vote in votes]
        polls = sorted((round.count(candidate), candidate) for candidate in candidates)
        min_poll, (max_poll, winner) = polls[0][0], polls[-1]
        if max_poll / voters > 0.5:
            return winner
        if len(polls) > 1 and max_poll == min_poll:
            return None
        loosers = [candidate for poll, candidate in polls if poll == min_poll]
        for voter in votes:
            for candidate in loosers:
                voter.remove(candidate)



#======================

def runoff(li):
    while all(li) and not all(len(k) == 1 for k in li):
        d = {l: 0 for k in li for l in k}
        for i in range(len(li)):
            d[li[i][0]] += 1
        m = min(d.values())
        li = [[j for j in i if d[j] != m] for i in li]
    return li[0][0] if li[0] else None




#================================
from collections import Counter


def runoff(voters):
    while True:
        result = Counter(voter[0] for voter in voters)
        for missing in set(voters[0])-set(result):
            result[missing] = 0
        losers = [candidate for (candidate, count) in result.items() if count == min(result.values())]
        for loser in losers:
            for voter in voters:
                voter.remove(loser)
        if len(result) == 1:
            return list(result.keys())[0]
        if len(voters[0]) == 0:
            return None