# Binomial Distribution

It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

It has three parameters:

n - number of trials.

p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).

size - The shape of the returned array.

# Poisson Distribution A.K.A Discrete Distribution

It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

It has two parameters:

lam - rate or known number of occurrences e.g. 2 for above problem.

size - The shape of the returned array

Binomial distribution only has two possible outcomes, whereas poisson distribution can have unlimited possible outcomes.

But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam.

# Uniform Distribution
Used to describe probability where every event has equal chances of occuring.

E.g. Generation of random numbers.

It has three parameters:

low - lower bound - default 0.0

high - upper bound - default 1.0

size - The shape of the returned array

# Logistic Distribution
Logistic Distribution is used to describe growth.

Used extensively in machine learning in logistic regression, neural networks etc.

It has three parameters:

loc - mean, where the peak is. Default 0.

scale - standard deviation, the flatness of distribution. Default 1.

size - The shape of the returned array.

# Multinomial Distribution

Multinomial distribution is a generalization of binomial distribution.

It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

It has three parameters:

n - number of times to run the experiment.

pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).

size - The shape of the returned array.

# Exponential Distribution

Exponential distribution is used for describing time till next event e.g. failure/success etc.

It has two parameters:

scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

size - The shape of the returned array

# Chi Square Distribution
Chi Square distribution is used as a basis to verify the hypothesis.

It has two parameters:

df - (degree of freedom).

size - The shape of the returned array.

x^2= Sum(O-E)^2/E

# Rayleigh Distribution
Rayleigh distribution is widely used in signal processing.
It has two parameters:

scale - (standard deviation) decides how flat the distribution will be default 1.0).

size - The shape of the returned array.

# Pareto Distribution
Pareto distribution can be seen as generalization of exponential distribution.

A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

It has two parameter:

a - shape parameter.

size - The shape of the returned array.

# Zipf's Law
Zipf's law states that given a large sample of words used:In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.

It has two parameters:

a - distribution parameter.

size - The shape of the returned array.


##### Pandas

Used for analyzing data.
It has functions for analyzing, cleaning, exploring, and manipulating data.
-analyze big data and make conclusions based on statistical theories.
-can clean messy data sets, and make them readable and relevant.
-Relevant data is very important in data science.

# Series
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.

## Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.
You can also use a key/value object, like a dictionary, when creating a Series.
Note: The keys of the dictionary become the labels.

# DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
Use ""print(df.loc[0])"" to return one or more specified rows.

# Read CSV
Pandas can read CSV files and turn them into a DataFrame.
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
Use to_string() to print the entire DataFrame.
You can check your system's maximum rows with the pd.options.display.max_rows statement.

"pd.options.display.max_rows = 9999" change the number of max rows using this.

# Read JSON
Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.

# Analyzing Data
For a quick overview of the data- use head(),specify the number of rows inside head() and it'll return that amount of rows.
There is also a tail() method for viewing the last rows of the DataFrame.
if no value is given,both will return 5 rows from the  top and the bottom.

The DataFrames object has a method called info(), that gives you more information about the data set.

# Data Cleaning
Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates
Inconsistent data
To fix it

dropna() is used to remove any missing values or empty cells.
this will be made to a copy of the DF,not the original one. If you want to change the original one, Use "inplace = True".

The fillna() method allows us to replace empty cells with a value:

A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# Wrong Data 
"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

To fix this, we can replace the values or we can remove them.

# Plot

Pandas uses the plot() method to create diagrams.

We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.