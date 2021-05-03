# graph-theory-project-G00365942



## description 
    A search tool that uses reads in a txt file using regular expression with re or imports
     The tool curently has(hhh(or 3 of any)) are used to show case how thry are typed in to use) 
        1.hhh. (finds any instance of hhh)
        2.^hhh (finds any intance of hhh at the start of the string)
        3.hhh$ (finds any intance of hhh at the end of the string)
        4.^hhh$(find any intance where hhh is the string)
        5.hhh|222 (finds any intance where hhh or 222 are in the string)
        6.\d (checks the string to see if they have any numeric digit between 0-9)
        7.\D (checks the string to see if they have no numeric digit between 0-9)
        8.\w (checks the string to see if they have any letter, numeric digit or underscore)
        9.\W (checks the string to see if they have no letter, numeric digit or underscore)
        10.\s (checks the string to see if they have any space, tabs or new lines)
        11.\S (checks the string to see if they have no space, tabs or new lines)

## Instructions
    Type in python projectCode.py on the command line
    type in the file directory
    type what regular expresion you wish to do
    and let the code do the rest

## The explanation of the algorithm


## What is a regular expression?
regex is a string of text that allows you to create patterns that help match, locate, and manage text
A regular expression (regex or regexp for short) is a special text string for describing a search pattern. You can think of regular expressions as wildcards on steroids.(https://www.regular-expressions.info/)
Stephen Kleene invented regular expressions in the mid-1950 tho they first appeared in a program setting in Ken Thompson’s version of the QED text editor in the mid-1960s and was later patent it in 1967 by ken (https://www.oreilly.com/library/view/beautiful-code/9780596510046/ch01.html#:~:text=Stephen%20Kleene%20invented%20regular%20expressions,automata%20in%20what%20they%20represent.)
https://medium.com/@zohaibshahzadTO/regular-expressions-character-classes-findall-method-c4b4d71d353a
## How do regular expressions differ across implementations?
below is an example of the differance betwwen python and java regular expessions given the smae pattern
(https://stackoverflow.com/questions/30527195/different-behavior-of-same-regular-expression-in-python-and-java)
```python
import re
p = re.compile("[0-9]*(?:\\.[0-9]+)?[^0-9]*D\\([MW]\\)\\s*US")
test_str = "9.5 D(M) US"
print re.search(p, test_str).group()
```
result will be:
9.5 D(M) US
 escape characters in regular expressions, \\d in Java, and \d in python

```java
import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.regex.*;
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Pattern FALLBACK_MEN_SIZE_PATTERN = Pattern.compile("([0-9]*)([\\.[0-9]+]?)([^0-9]*)D\\([M|W]\\)\\s*US");
        String strTest = "9.5 D(M) US";
        Matcher matcher = FALLBACK_MEN_SIZE_PATTERN.matcher(strTest);
        if (matcher.find()) {
            System.out.println(matcher.group(1));
            System.out.println(matcher.group(2));
            System.out.println(matcher.group(3));
        }
    }
 
}
```
result will be 
5

explanastion
[\.[0-9]+]?
java|
java see this as a one chacater macth, "." or a numberic digit.
java see this as one total expersion
Python see this as 2 seperate expersion
The first expersion ending in the first "]" the "+" after that matches that muliplte intances of the characters"." or a numberic digit. The second pattern is "]?" matches the "]" characters, 
so the following text "123.+[]" in java will give 8 matches("1","2","3",".","+","","","","")
python give the following matches ("123.","[]")
## Can all formal languages be encoded as regular expressions?
 A formal language consists of words whose letters are taken from an alphabet and are well-formed according to a specific set of rules. Not formaly you regular experssion will give syntax errors due to formal languages are strict on it's rules. It is possible given that your regular expression is quite percise it would be possible. regylar expression is also drived form formal languages 

Talk about grammar.

https://web.mit.edu/6.005/www/fa15/classes/17-regex-grammars/

