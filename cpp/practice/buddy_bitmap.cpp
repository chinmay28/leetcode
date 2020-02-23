#include<iostream>
#include<map>
#include<vector>
using namespace std;

int NLEVELS = 0;

void set_bit(vector<bool>& bitmap, int start, int end) {
    int leaf_start = 1 << (NLEVELS - 1);
    int leaf_end = (1 << NLEVELS) - 1;
    if (start < leaf_start || end > leaf_end || start > end) {
        cerr << "invalid start/end position!" << endl;
        return;
    }

    // update parents
    while (start > 0 && end > 0) {
        for (int i=start; i <= end; i++) {
            // leaf or invariant is true
            if (2 * i + 1 > leaf_end || (bitmap[2*i] && bitmap[2*i+1]))
                bitmap[i] = true;
        }

        end /= 2;
        start /= 2;
    }
}


void clear_bit(vector<bool>& bitmap, int start, int end) {
    int leaf_start = 1 << (NLEVELS - 1);
    int leaf_end = (1 << NLEVELS) - 1;
    if (start < leaf_start || end > leaf_end || start > end) {
        cerr << "invalid start/end position!" << endl;
        return;
    }

    // update parents
    while (start > 0 && end > 0) {
        for (int i=start; i <= end; i++) {
            // leaf or invariant is true
            if (2 * i + 1 > leaf_end || !(bitmap[2*i] && bitmap[2*i+1]))
                bitmap[i] = false;
        }

        end /= 2;
        start /= 2;
    }
}


int main() {

    cout << "Number of levels: ";
    cin >> NLEVELS;
    cout << "You entered " << NLEVELS << endl;

    vector<bool> bitmap((1 << NLEVELS), 0);

    set_bit(bitmap, 12, 13);
    set_bit(bitmap, 14, 15);
    set_bit(bitmap, 4, 15);
    set_bit(bitmap, 14, 5);
    clear_bit(bitmap, 14, 14);
    set_bit(bitmap, 8, 11);
    clear_bit(bitmap, 8, 9);

    return 0;
}