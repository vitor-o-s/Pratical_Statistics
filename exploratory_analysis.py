def mean (*args):
    """Return a float"""
    return sum(args) / float(len(args))

def trimmed_mean (*args):
    trimmed_list = sorted(args)[1:-1]
    return  sum(trimmed_list) / len(trimmed_list)# - 2*p

def weighted_mean (*args, *weights=None):
    """Calculate the weighted mean of a list."""
    if weights is None:
        return mean(args)
    multipled_arg = 0
    for i, arg in weights, args:
        multipled_arg += arg * weight[i]
    return multipled_arg / float(sum(weights))

'''
def weighted_mean(data, weights=None):

    total_weight = float(sum(weights))
    weights = [weight / total_weight for weight in weights]
    w_mean = 0
    for i, weight in enumerate(weights):
        w_mean += weight * data[i]
    return w_mean


def median(*args):
    """Calculate the median of a list."""
    args.sort()
    num_values = len(args)
    half = num_values // 2
    if num_values % 2:
        return args[half]
    return 0.5 * (args[half-1] + args[half])

def weighted_median(data, weights=None):
    """Calculate the weighted median of a list."""
    if weights is None:
        return median(data)
    midpoint = 0.5 * sum(weights)
    if any([j > midpoint for j in weights]):
        return data[weights.index(max(weights))]
    if any([j > 0 for j in weights]):
        sorted_data, sorted_weights = zip(*sorted(zip(data, weights)))
        cumulative_weight = 0
        below_midpoint_index = 0
        while cumulative_weight <= midpoint:
            below_midpoint_index += 1
            cumulative_weight += sorted_weights[below_midpoint_index-1]
        cumulative_weight -= sorted_weights[below_midpoint_index-1]
        if abs(cumulative_weight - midpoint) < sys.float_info.epsilon:
            bounds = sorted_data[below_midpoint_index-2:below_midpoint_index]
            return sum(bounds) / float(len(bounds))
        return sorted_data[below_midpoint_index-1]
'''

def mean_absolution_deviation ():

    return

def variance ():

    return

def standard_deviation ():

    return

def median_absolutte_deviation ():

    return

def percentile ():

    return
