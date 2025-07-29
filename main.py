import scipy.stats as stats

prob1 = stats.poisson.pmf(6, 10)
print("probability of getting 6 days of rain", prob1)

prob2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10)
print("probability of raining for 12-14 days :", prob2)