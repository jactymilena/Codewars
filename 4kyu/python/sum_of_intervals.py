# link : https://www.codewars.com/kata/52b7ed099cdc285c300001cd
# TODO : NE PASSE PAS ENCORE TOUS LES TESTS

from typing import overload


def get_overlap(n1, n2):
  return max(0, min(n1[1], n2[1]) - max(n1[0], n2[0]))

def sum_of_intervals(intervals):
  sum  = 0
  overlap = 0
  overlap_history = {}

  for i in range(len(intervals)):
    sum += intervals[i][1] - intervals[i][0] 
    # calcul overlap pour chaque element
    for j in range(i+1, len(intervals)):
      current_overlap = get_overlap(intervals[i], intervals[j])
      if current_overlap > 0:
        # si deja dans le dict ne pas l'additionner
        if (i, j) not in overlap_history and (j, i) not in overlap_history:
          overlap_history[(i, j)] = True
          overlap += current_overlap

  return sum - overlap

# Tests
interval = [(1, 4), (7, 10), (3, 6)]

print(sum_of_intervals(interval))

interval = [(1, 5), (1, 5)]
print(sum_of_intervals(interval))

interval = [(1, 4), (7, 10), (3, 5)]
print(sum_of_intervals(interval))

