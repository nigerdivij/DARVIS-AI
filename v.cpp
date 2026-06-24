#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int choice;
    cin >> choice;

    if (choice == 1) {
        int a, b;
        cin >> a >> b;
        cout << a + b;
    }

    else if (choice == 2) {
        int a, b;
        cin >> a >> b;
        cout << a - b;
    }

    else if (choice == 3) {
        int a, b;
        cin >> a >> b;
        cout << a * b;
    }

    else if (choice == 4) {
        int a, b;
        cin >> a >> b;
        if (b == 0) cout << "Error";
        else cout << (double)a / b;
    }

    else if (choice == 5) {
        int n;
        cin >> n;
        long long fact = 1;
        for (int i = 1; i <= n; i++)
            fact *= i;
        cout << fact;
    }

    else if (choice == 6) {
        double b, e;
        cin >> b >> e;
        cout << pow(b, e);
    }

    else if (choice == 7) {
        double b;
        cin >> b;
        cout << pow(b, 2);
    }

    else if (choice == 8) {
        double b;
        cin >> b;
        cout << pow(b, 3);
    }

    else if (choice == 9) {
        double n;
        cin >> n;
        cout << sqrt(n);
    }

    return 0;
}