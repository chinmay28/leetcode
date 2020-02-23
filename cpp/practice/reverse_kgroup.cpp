#include<iostream>
#include<map>
#include<vector>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(): val(0), next(NULL) {}
    ListNode(int x) : val(x), next(NULL) {}
};


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

int main() {
    ListNode nodes[6];
    for (int i=1; i<=6; i++) {
        nodes[i-1].val = i;
        if (i < 6) 
            nodes[i-1].next = &nodes[i];
    }

    ListNode *newHead = reverseKGroup(&nodes[0], 2);

    return 0;
}