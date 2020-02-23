/*
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
*/

#include<iostream>


// Definition for singly-linked list.
 struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
 

class Solution {
public:
    ListNode* kNodeReverse(ListNode* head, int k, ListNode*& last) {
        ListNode* curr = head;

        // dry run
        int bkp_k = k;
        while (k-- && curr->next)
            curr = curr->next;
        if (k > 0) {
            last = curr;
            return head;
        }

        curr = head;
        k = bkp_k;

        ListNode *prevLast = last; // last from previous group
        last = head;
        if (!curr->next)
            return head;
        ListNode *prev = NULL, *next = curr->next;

        while (k) {
            curr->next = prev;
            prev = curr;
            curr = next;
            if (!next)
                break;
            next = next->next;
            k--;
        }

        // reattach head's link
        last->next = curr;
        if (prevLast != head)
            prevLast->next = prev;
        return prev;
    }


    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* curr = head;
        ListNode* last = head;
        ListNode* newHead = NULL;
        while (curr) {
            ListNode* temp = kNodeReverse(curr, k, last);
            if (!newHead)
                newHead = temp;
            curr = last->next;
        }
        return newHead;
    }
};
