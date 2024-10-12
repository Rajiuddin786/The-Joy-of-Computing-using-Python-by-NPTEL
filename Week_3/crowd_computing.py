# from statistics import mean
from scipy import stats
Estimates = [1830, 295, 1834, 1781, 794, 513, 680, 1148, 1200, 1998, 1008, 819, 1329, 497, 143, 1408, 1588, 644, 1948, 1586, 1904, 828, 475, 210, 960, 668, 516, 590, 306, 1006, 542, 1389, 1466, 565, 1292, 1479, 268, 567, 1774, 1466, 260, 1172, 989, 1392, 1828, 187, 1304, 1549, 1871, 321, 1687, 844, 857, 891, 745, 1779, 621, 115, 1252, 1647, 1529, 1698, 1420, 1443, 1675, 1919, 592, 1975, 1565, 1978, 879, 1953, 1706, 1762, 1491]
Estimates.sort()
m=stats.trim_mean(Estimates,0.1)
print(m)
# tv = int(0.1*len(Estimates))
# Estimates = Estimates[tv:]
# Estimates = Estimates[:len(Estimates)-tv]
# print(mean(Estimates))