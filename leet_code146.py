"""
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Companies 
Google Facebook Microsoft Amazon Bloomberg Uber Twitter Snapchat Zenefits Yahoo Palantir

"""


# PLUP Solution
# Use double Linked list, save the node in mapr

class Node(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val

        self.previous = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.mapr = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.previous = self.head

    def _add_node_end(self, node):
        temp_node = self.tail.previous
        temp_node.next = node
        node.previous = temp_node
        node.next = self.tail
        self.tail.previous = node

    def _delete_node(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not self.mapr.has_key(key):
            return -1

        node = self.mapr[key]
        self._delete_node(node)
        self._add_node_end(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # BUG: Need to delete the node from Double LL if the key already exists
        # bcoz we update it with new value (by creating a new node)
        # if the key already exists delete the node
        if self.mapr.has_key(key):
            node = self.mapr[key]
            self.mapr.pop(key)
            self._delete_node(node)

        # delete first node
        if len(self.mapr) + 1 > self.capacity:
            node = self.head.next
            tkey = node.key
            self.mapr.pop(tkey)
            self._delete_node(node)

        new_node = Node(key, value)
        self.mapr[key] = new_node
        self._add_node_end(new_node)



        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)