# Regular Expressions Primer

## What are regular expressions?

* Sequence of characters that defines a search pattern
* Used for find and replace:
  * advanced language for searching for *patterns* instead of just raw text


## How do you use them?
* Define a *pattern*
  * sequence of characters defining what matches and what doesn't
  * can use wildcards, sub-patterns, many constructs
* Perform the search
  * once vs. all
* Extract the matches or replace-in-place


## Pattern language

### Primitives

* `'abc'`: finds the *literal text* `abc` within a line
* `'[abc]'`: finds any `a` or `b` or `c` character
* `'[^abc]'`: finds anything except an `a` or `b` or `c` character
* `'a*'`: finds zero or more `a` characters
* `'a+'`: finds one or more `a` characters
* `'a?'`: finds zero or one `a` characters
* `'\s'`: finds any whitespace character
* `'\S'`: finds any non-whitespace character
* `'\d'`: finds any digit
* `'\w'`: finds any alpha character
* `'.'`: finds any character
* `'\('`: finds a literal `(` character (which is a special character in *regexp* language)
* ... and so on (most good *regexp* sites will list all of these, there are hundreds

### Composition

* `'(a|b)'`: finds either an `a` or a `b`
* `'(alfred|bob)'`: finds either `alfred` or `bob`
* `'a{3}'`: finds exactly 3 `a` characters
* `'a{3,5}'`: finds 3, 4, or 5 `a` characters
* `'(aba)+'`: finds `aba` repeated any number of times (`abaabaaba` will match)
* `'(aba){3,5}'`: finds `aba` repeated either 3, 4, or 5 times


## Usage:

### Basic search:

    tweet = 'I am tired today'
    match = re.match('I am \w+ today', tweet)
    if match:
        print 'found a match'

### Capture groups

* Parentheses denote substrings that can be further manipulated
  * must be evenly balanced
  * can be nested
* `'abc(def)ghi`': finds the full text `abcdefghi` but marks the subexpressions `def` for further manipulation
  * substring is in match object as group index 1
  * extraction: just get the part in parentheses, not the rest
  * replacement: replace the `def` with some other substring
* `'bob\s+((\w+)?\s+)smith'`: finds the middle name (if one exists) for each occurrence of `bob smith` in the text

**Example:**

    tweet = 'I am tired today'
    match = re.match('I am (\w+) today', tweet)
    if match:
        print 'found:', match.group(1)


## Advanced concepts:

* Pre-compiled expressions for multiple use
* Non-capturing parentheses
* Lookahead and look-behind


## References
* [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression) on Wikipedia
* [Regular expression operations](https://docs.python.org/2/library/re.html)
* [Debuggex](https://www.debuggex.com/) regular expression build/debug tool
* [Sample CSV files](http://www.sample-videos.com/download-sample-csv.php)
