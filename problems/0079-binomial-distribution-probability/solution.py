import math

def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Calculate the probability of exactly k successes in n Bernoulli trials.
    
    Args:
        n: Total number of trials
        k: Number of successes
        p: Probability of success on each trial
    
    Returns:
        Probability of k successes
    """
    # Your code here
    comb_value = math.comb(n,k)
    success = pow(p,k)
    failure = pow((1-p),(n-k))
    return comb_value*success*failure
    pass