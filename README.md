## Regex in Python
#### Introduction
Regular expressions (regex) are powerful tools for matching and manipulating text. 

They are used for searching, validating, and parsing strings based on specific patterns. Python provides the re module to work with regular expressions. 

#### Installation
The re module is part of Python's standard library, so you don't need to install anything extra. Just make sure you have Python installed on your system.

#### Basics of Regex
A regex pattern is a sequence of characters that defines a search pattern. Here are some basic components:

##### Literal characters: Match themselves (e.g., a matches "a").
##### Meta-characters: Characters with special meanings (e.g., ., ^, $, *, +, ?, {}, [], (), \).
Common Meta-characters

```
.: Matches any character except newline.
^: Matches the start of the string.
$: Matches the end of the string.
*: Matches 0 or more repetitions of the preceding element.
+: Matches 1 or more repetitions of the preceding element.
?: Matches 0 or 1 repetition of the preceding element.
{n,m}: Matches between n and m repetitions of the preceding element.
[]: Matches any one of the characters inside the brackets.
|: Acts as an OR operator.
(): Groups elements together.
```