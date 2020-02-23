/*
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
*/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 
class ListComparator { 
public: 

    int operator() (ListNode*& l1, ListNode*& l2) { 
        return l1->val > l2->val; 
    } 
};


class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        ListNode result(0);
        ListNode *ptr = &result;
        
        priority_queue<ListNode*, vector<ListNode*>, ListComparator > queue;
        
        for (ListNode *list: lists)
            if (list)
                queue.push(list);
        
        while (!queue.empty()) {
            ListNode *list = queue.top();
            queue.pop();
            ptr->next = new ListNode(list->val);
            ptr = ptr->next;
            if (list->next)
                queue.push(list->next);
        }
        
        return result.next;
    }
};
