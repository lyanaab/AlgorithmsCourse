// Fraction.cpp : This file contains the 'main' function. Program execution begins and ends there.


#include <iostream>
int factorial(int n) {
	if (n < 0) {
		std::cout << "Factorial is not defined for negative numbers";
		return -1;
	}
		int result = 1;
		for (int i = 1; i <= n; i++) {
			result *= i;
		}
		return result;

	}



int main()
{
	int number;
	std::cout << "Enter a non-negative integer: ";
	std::cin >> number;
	int result = factorial(number);
	if (result != -1) {
		std:: cout << "The factorial of " << number << " is " << result << "\n";
	}
	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu


