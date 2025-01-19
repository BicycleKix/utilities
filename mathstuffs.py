import math

def fit_squares_in_space(num_squares: int, dims: list):
    dim_ratio = dims[0] / dims[1]
    ideal_ratio = [100, 1]
    for nx in range(1, num_squares):
        ny = math.ceil(num_squares/nx)
        ratio = nx/ny
        if abs(ratio - dim_ratio) < abs(ideal_ratio[0] / ideal_ratio[1] - dim_ratio):
            ideal_ratio = [nx, ny]
    return ideal_ratio

def get_magnitude(in_array, hyp=True):
    if hyp:
        radical = sum(vec**2 for vec in in_array)
    else:
        radical = in_array[0]**2 - sum(vec**2 for vec in in_array[1:])
    return math.sqrt(radical)

def normalize(in_array):
    magnitude = get_magnitude(in_array)
    return [vec / magnitude for vec in in_array] if magnitude else [0, 0]