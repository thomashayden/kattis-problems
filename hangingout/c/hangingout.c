#include <stdio.h>

int main()
{
  int limit = 0, events = 0, curr = 0, people = 0, rejected = 0;
  scanf("%d %d", &limit, &events);
  for (int i = 0; i < events; i++)
  {
    char event[6];
    scanf("%s %d", event, &people);
    if (event[0] == 'e')
    {
      if (curr + people > limit)
      {
        rejected++;
      } else {
        curr += people;
      }
    } else {
      curr -= people;
    }
  }
  printf("%d\n", rejected);
  return 0;
}
