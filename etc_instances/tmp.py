# Other tmp calc
import pandas as pd
def f_MovingAverage(df_s, n):
    """
    series - dataframe with timeseries
    n - rolling window size
    """

    rolling_mean = df_s.rolling(window=n).mean()
    return rolling_mean

def f_weighted_average(series, weights):
    result = 0.0
    weights.reverse()
    for n in range(len(weights)):
        result += series[-n-1] * weights[n]
    return result

def f_exp_smoothing(series, alpha):
    result = [series[0]] # first value is same as series
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n-1])
    return result

def f_double_exp_smoothing(series, alpha, beta):
    result = [series[0]]
    for n in range(1, len(series)+1):
        if n == 1:
            level, trend = series[0], series[1] - series[0]
        if n >= len(series): # прогнозируем
            value = result[-1]
        else:
            value = series[n]
        last_level, level = level, alpha*value + (1-alpha)*(level+trend)
        trend = beta*(level-last_level) + (1-beta)*trend
        result.append(level+trend)
    return result

series = [1, 1.1, 1.5, 1.7, 1.9, 2.11, 2.13, 2.15, 2.19, 2.205]
df_s = pd.DataFrame({'s': series})
print(df_s)

rolling_mean = f_MovingAverage(df_s, 3)
weighted_average = f_weighted_average(series, [0.6, 0.2, 0.1, 0.07, 0.03])
exp_smoothing = f_exp_smoothing(series, 0.1)

print('rolling_mean - {}'.format(rolling_mean))
print('weighted_average - {}'.format(weighted_average))
print('exp_smoothing - {}'.format(exp_smoothing))

# Reverce
print(series)
series.reverse()
print(series)


itertools.product
