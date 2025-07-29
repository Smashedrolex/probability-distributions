import scipy.stats as stats


prob1 = 1-stats.poisson.cdf(20, 15)


print(prob1)

prob2 = stats.poisson.pmf(17, 15) + stats.poisson.pmf(18, 15) + stats.poisson.pmf(19, 15) + stats.poisson.pmf(20, 15) + stats.poisson.pmf(21, 15)

print(prob2)