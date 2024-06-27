#include <iostream>

using namespace std;

int main() {
    int N;
    
    while (true) {
        cin >> N;
        if (N == 0) break;

        for (int i = 0; i < N; ++i) {
            int A, B, C, D, E;
            cin >> A >> B >> C >> D >> E;

            // Conta quantos valores são <= 127
            int count = 0;
            if (A <= 127) count++;
            if (B <= 127) count++;
            if (C <= 127) count++;
            if (D <= 127) count++;
            if (E <= 127) count++;

            if (count == 1) {
                if (A <= 127) cout << "A" << endl;
                else if (B <= 127) cout << "B" << endl;
                else if (C <= 127) cout << "C" << endl;
                else if (D <= 127) cout << "D" << endl;
                else if (E <= 127) cout << "E" << endl;
            } else {
                cout << "*" << endl;
            }
        }
    }

    return 0;
}
