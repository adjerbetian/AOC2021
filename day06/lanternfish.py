from collections import defaultdict

Population = dict[int, int]


def build_population(ages: list[int]) -> Population:
  population = defaultdict(lambda: 0)
  for age in ages:
    population[age] += 1
  return dict(population)


def pass_n_days(population: Population, n: int) -> Population:
  for i in range(n):
    population = pass_day(population)
  return population


def pass_day(population: Population) -> Population:
  new_population = defaultdict(lambda: 0)
  for age, count in population.items():
    if age == 0:
      new_population[6] += count
      new_population[8] += count
    else:
      new_population[age - 1] += count
  return new_population


def get_population_count(population: Population) -> int:
  return sum(population.values())
