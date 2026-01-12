#include <stdio.h>
#include <math.h>

// Function to check if a number is prime
int is_prime(int num) {
    if (num <= 1) return 0;
    if (num <= 3) return 1;
    if (num % 2 == 0 || num % 3 == 0) return 0;
    
    for (int i = 5; i <= sqrt(num); i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return 0;
    }
    return 1;
}

int main() {
    int n, found = 0;
    printf("Enter number: ");
    scanf("%d", &n);
    
    int start = n * n;
    int end = (n + 1) * (n + 1);
    printf("PRIME NUMBERS IN RANGE OF %d and %d:\n", start, end);
    
    for (int i = start; i < end; i++) {
        if (is_prime(i)) {
            printf("%d\n", i);
            found = 1;
        }
    }
    
    if (!found) {
        printf("NONE\n");
    }
    
    return 0;
}
