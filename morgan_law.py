# You may be familiar with De Morgan's laws. They say that:

# The negation of a conjunction is the disjunction of the negations.
# The negation of a disjunction is the conjunction of the negations.

# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

# & (ampersand) - bitwise conjunction;
# | (bar) - bitwise disjunction;
# ~ (tilde) - bitwise negation;
# ^ (caret) - bitwise exclusive or (xor).

# Bitwise operations (&, |, and ^)
# Argument A	Argument B	A & B	 A | B  	A ^ B
#      0           0	     0	       0	      0
#      0	       1	     0	       1	      1
#      1	       0	     0	       1	      1
#      1	       1	     1         1	      0


# Bitwise operations (~)
# Argument	  ~ Argument
#    0	           1
#    1             0

# Let's make it easier:

# & requires exactly two 1s to provide 1 as the result;
# | requires at least one 1 to provide 1 as the result;
# ^ requires exactly one 1 to provide 1 as the result.
