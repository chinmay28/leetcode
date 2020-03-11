/*
Given a binary tree, return the vertical order traversal of its nodes' values. 
(ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

*/

#include<iostream>
#include<vector>
#include<map>
#include<queue>
using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 

class Solution {
public:
    
    vector<vector<int>> verticalOrder(TreeNode* root) {
        map<int, vector<int>> tree_map;
        getTreeData(root, tree_map, 0);
        
        vector<vector<int>> result;
        
        for (auto it = tree_map.begin(); it != tree_map.end(); it++) {
            result.push_back(it->second);
        }
        
        return result;
    }
    
    void getTreeData(TreeNode* root, map<int, vector<int>>& tree_map, int count) {
        
        if (!root) return;
        
        queue<pair<int, TreeNode*>> bfs_queue;
        pair<int, TreeNode*> root_pair(count, root);
        bfs_queue.push(root_pair);
        
        while(!bfs_queue.empty()) {
            pair<int, TreeNode*> node = bfs_queue.front();
            bfs_queue.pop();
            
            if (!node.second)
                continue;  // node is a null value. skip
                        
            tree_map[node.first].push_back(node.second->val);
            pair<int, TreeNode*> left(node.first - 1, node.second->left);
            pair<int, TreeNode*> right(node.first + 1, node.second->right);
            bfs_queue.push(left);
            bfs_queue.push(right);
        }
    }
};
