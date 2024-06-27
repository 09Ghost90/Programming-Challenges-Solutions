#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool temDigitosRepetidos(int numero) {
    string NumStr = to_string(numero);
    unordered_set<char> digitos;

    for (char c : NumStr) {
        if (digitos.find(c) != digitos.end()) {
            return true;
        }
        digitos.insert(c);
    }
    return false;
}

int main() {
    int N, M;
    while (cin >> N >> M) {
        int count = 0;
        for (int i = N; i <= M; i++) {
            if (!temDigitosRepetidos(i)) {
                count++;
        }
    }
    cout << count << "\n";
}
    return 0;
}
