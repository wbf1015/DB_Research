#include<iostream>
#include<cmath>
using namespace std;
double makeCal(int m, int r) {
	if (r % 2 == 1) {
		double son = m * pow((m - 1), (r + 1) / 2) - m;
		double mother = 2 * pow((m - 1), (r + 1) / 2) - m;
		return son / mother;
	}
	else {
		double son = m * pow((m - 1), (r) / 2) - 2;
		double mother = 2 * pow((m - 1), (r) / 2) - 2;
		return son / mother;
	}
}
int main() {
	for (int m = 3; m <= 10; m++) {
		for (int r = 2; r <= 10; r++) {
			cout << "m= " << m << "r= " << r << " 时相似比为 " << makeCal(m, r) << endl;
		}
	}
}