#https://leetcode.com/discuss/interview-question/415729/

# attempt 1
def get_most_mentions(top_count, comp_list, review_list):
    mention_counts = {comp_name: 0 for comp_name in comp_list}
    for review in review_list:
        for comp_name in comp_list:
            if comp_name.lower() in review.lower():
                mention_counts[comp_name] += 1

    # print 'mention_counts', mention_counts

    # create an inverted map
    inverted_mention_counts = {}
    for name, count in mention_counts.iteritems():
        if count in inverted_mention_counts:
            inverted_mention_counts[count].append(name)
        else:
            inverted_mention_counts[count] = [name]

    # print 'inverted_mention_counts', inverted_mention_counts

    # sort inverted map
    for key in inverted_mention_counts:
        if len(inverted_mention_counts[key]) > 1:
            inverted_mention_counts[key].sort()

    # print 'sorted inverted_mention_counts', inverted_mention_counts

    result = []
    for _ in range(top_count):
        count = max(inverted_mention_counts.keys())
        for name in inverted_mention_counts[count]:
            if len(result) == top_count:
                break
            result.append(name)
        else:
            del (inverted_mention_counts[count])
            continue
        break
    return result


# attempt2
class Competitor(object):

    def __init__(self, name, count=0):
        self.name = name
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            result = self.name < other.name  # we need lexicographically smaller named object
        else:
            result = self.count < other.count  # otherwise compare counts
        return result


def get_most_mentions2(top_count, comp_names, review_list):
    mention_counts = {comp_name: 0 for comp_name in comp_names}

    for review in review_list:
        for comp_name in comp_names:
            if comp_name.lower() in review.lower():
                # force max heap
                mention_counts[comp_name] -= 1

    comp_list = [Competitor(name, mention_counts[name]) for name in mention_counts]
    import heapq
    heapq.heapify(comp_list)
    result = []
    for _ in range(top_count):
        result.append(heapq.heappop(comp_list).name)

    return result


if __name__ == "__main__":

    comps = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
    reviews = ["newshop is providing good service in the city;everyone should try newshop",
               "best services by newshop",
               "fashionbeats has great services in the city",
               "Im proud to have fashionbeats",
               "mymarket has awesome service",
               "thank Newshop for the quick delivery"]
    print get_most_mentions2(2, comps, reviews)

    comps = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
    reviews = ["newshop is providing good service in the city;everyone should try newshop",
               "best services by newshop",
               "fashionbeats has great services in the city",
               "Im proud to have fashionbeats",
               "afshion has awesome service",
               "thank afshion for the quick delivery"]

    print get_most_mentions2(2, comps, reviews)
