#include<iostream>
#include<map>
#include<vector>
using namespace std;


void return_some_map(vector<string> keys, vector<int> values, map<string, int>* result) {
    // map<string, int> result;
    for (int i=0; i<keys.size(); i++) {
        result->emplace(keys[i], values[i]);
    }
    cout <<result << endl;
    // return result;
}


int main() {
    map<string, int> test_map = {
        {"sunnyvale", 10},
        {"santa clara", 20}
    };

    test_map["san jose"] = 30;

    map<string, int> second_map = test_map;
    second_map["sunnyvale"] = 60;

    cout << &second_map << endl;

    // for (auto it = test_map.begin(); it != test_map.end(); it++) {
    //     cout << it->first << "-->" << it->second << endl;
    // }

    // cout << "-----------------\n";

    vector<string> keys = {"sunnyvale", "santa clara", "san jose"};

    vector<int> values = {3, 4, 5};
    int stack_var1 = 6;
    string stack_var2 = "test";
    string* name = &keys[1];

    return_some_map(keys, values, &second_map);
    cout <<&second_map << endl;

    for (auto it = second_map.begin(); it != second_map.end(); it++) {
        cout << it->first << "-->" << it->second << endl;
    }
    
    return 0;
}