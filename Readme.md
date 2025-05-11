a set of python patterns used to train custom developed LLM for automated code generation

key operations/functional primitives on data (become part of algorithms):

"data" is scalars, collections, classes/objects (individual classes may have to support some of the below ops, by overwriting standard methods)

0. Indexing
1. search/find
2. slicing / subsetting
3. filter
4. sort
5. compare (==, <, >)
6. join/concatenate
7. aggregations (global and by key), including based on sliding window when by key - global or sliding win when by key
8. apply transformations (including pivots, transpose etc) and/or calculations/math models
9. validation / quality checks
9. visualizations

Data then feeds math models / calcs:

1. English math terms for all situations
2. Coding any math expression/equation in python
3. Feeding the above with data / data processing / preparation for the above

 mat models - building block hierarchy:
 1. Math constants: Pi, E, etc
 2. Number systems: real numbers, rational numbers, fractions, ratios etc
 3. Scalar Numeric data types and their precision and lenght / size - in programming languages
 4. Vector/Matrix data types
 5. Math Operators (+, -, *, **, sqrt) - on scalar and vector/matrix
 6. Math Functions (exp, ln etc) - on scalar and vector/matrix
 7. Math Models (of the above)
(adjacent area is operations with dates)