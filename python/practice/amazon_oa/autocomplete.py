#https://leetcode.com/discuss/interview-question/414085/

class TrieNode(object):

    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_word = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        current = self.root
        value = ''
        for char in word:
            value += char
            if char not in current.children:
                current.children[char] = TrieNode(value)

            current = current.children[char]

        # once the word is complete, we mark it
        current.is_word = True

    def get_words(self, node):
        node_list = [node]
        result = []

        while node_list:
            current = node_list.pop(0)
            if current.is_word:
                result.append(current.value)

            for child_node in current.children.values():
                node_list.append(child_node)

        return result

    def get_top_words_with_prefix(self, prefix, limit=3):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        words = self.get_words(current)
        import heapq
        heapq.heapify(words)
        result = []
        for _ in range(limit):
            if not words:
                break
            result.append(heapq.heappop(words))

        return result

    def auto_complete(self, product_names, query):
        if len(query) < 2 or not product_names:
            return None

        for name in product_names:
            self.insert(name)

        autocomplete_queries = []
        for i in range(2, len(query) + 1):
            autocomplete_queries.append(query[0:i])

        result = []
        for ac_query in autocomplete_queries:
            top_results = self.get_top_words_with_prefix(ac_query)
            result.append(top_results)

        return result


import pprint
trie = Trie()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
query = "mouse"
#expected = [["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
pprint.pprint(trie.auto_complete(products, query))

trie = Trie()
products = ["ps4", "ps4 slim", "ps4 pro", "xbox", "tissue",
            "standing table", "house", "true love", "tracking device"]
query = "ps4"
#expected = [["ps4", "ps4 pro", "ps4 slim"], ["ps4", "ps4 pro", "ps4 slim"]]
pprint.pprint(trie.auto_complete(products, query))

query = "tru"
#expected = [["tracking device", "true love"], ["true love"]]
pprint.pprint(trie.auto_complete(products, query))
