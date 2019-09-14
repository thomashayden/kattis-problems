#include <stdio.h>
#include <stdlib.h>

int main() {
  long a, b;
  while (scanf("%ld %ld", &a, &b) != EOF) {
    printf("%ld\n", labs(a - b));
  }
  return 0;
}
