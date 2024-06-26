from LOTlib3.Grammar import Grammar
from LOTlib3.DataAndObjects import FunctionData
from LOTlib3.Hypotheses.LOTHypothesis import LOTHypothesis
from LOTlib3.Hypotheses.Likelihoods.BinaryLikelihood import BinaryLikelihood
from LOTlib3.Eval import primitive
from LOTlib3.Miscellaneous import qq, Infinity
from LOTlib3.TopN import TopN
from LOTlib3.Samplers.MetropolisHastings import MetropolisHastingsSampler
from math import log, exp
from itertools import product

# Define the grammar
grammar = Grammar(start='S')

# Rules for binary digits
grammar.add_rule('S', '"1"', None, 6.0)
grammar.add_rule('S', '"0"', None, 6.0)

# Rules for operations
grammar.add_rule('S', 'repeat_', ['S', 'X'], 1.0)
grammar.add_rule('S', 'concat_', ['S', 'S'], 1.0)
grammar.add_rule('S', 'bflip_', ['S'], 1.0)
grammar.add_rule('S', 'rev_', ['S'], 1.0)

for n in range(10):
    grammar.add_rule('X', str(n), None, 10.0/((n+1)**2))


@primitive
def repeat_(x, y):
    return x*y

@primitive
def concat_(x, y):
    return x+y

@primitive
def rev_(x):
    return x[::-1]

@primitive
def bflip_(x):
    def help_(y):
        return '0' if y=='1' else '1'
    return ''.join([help_(z) for z in x])

# define a hypothesis
class MyHypothesis(LOTHypothesis):
    
    def __init__(self, **kwargs):
        # initialize by running the superclass' init
        # with the appropriate arguments.
        LOTHypothesis.__init__(
            self, 
            grammar=grammar, 
            display="lambda: %s", 
            **kwargs
        )

    def compute_single_likelihood(self, datum):
        """Define the loglikelihood function P(datum | self)"""
        # If the hypothesis called with the datum's input
        # is equal to the output...
        interpreted = self(*datum.input)
        if len(interpreted) > 8:
            number_of_differences = sum([
                x!=y
                for x, y
                in zip(interpreted, datum.output)
            ])
            return log(
                (1-datum.alpha) ** number_of_differences *
                datum.alpha ** (8-number_of_differences)
            )
        else:
            return -Infinity

# Create all binary sequences for length 8
binary_sequences = [
    ''.join(seq)
    for seq
    in product('01', repeat=8)
]

from LOTlib3.DataAndObjects import FunctionData


from LOTlib3.Samplers.MetropolisHastings import MetropolisHastingsSampler
from collections import Counter

h0 = MyHypothesis()

def save_line(fname, line):
    with open(fname, 'a') as openfile:
        openfile.write(line)


filename = './better_probs.csv'

first_line = 'sequence, prediction\n'
with open(filename, 'w') as openfile:
    openfile.write(first_line)

import time
start_time = time.time()

# for i, d in enumerate(binary_sequences):
for i, d in enumerate:

    data = [ 
        # a single datum
        FunctionData(
            # input is empty since we are 
            # encoding a single number
            input=[], 
            # the observation we want to encode
            output=d, 
            # the probability of 
            # observing the true number
            alpha=0.9999
        )
    ]
    count = Counter()
    n_steps = 400000
    for h in MetropolisHastingsSampler(h0, data, steps=n_steps):
        count[h] += 1

    for h in sorted(count.keys(), key=lambda x: count[x])[-10:]:
        print('Count:          ', count[h])
        print('Posterior:      ', exp(h.posterior_score))
        print('Hypothesis:     ', h)
        print('Prior:          ', h.prior)
        print('Interpretation: ', h())
        print()

    current_time = time.time()
    print('Avg time: ', (current_time - start_time) / (i+1))

    count_zeroes = 0
    for h, n in count.items():
        if len(h()) > 8 and h()[8] == '0':
            count_zeroes += n
    prop = count_zeroes / n_steps

    save_line(filename, f'{d}, {prop}\n')

print((time.time() - start_time)/10)

