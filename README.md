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
Stephen Kleene invented regular expressions in the mid-1950 "as a notation for finite automata" although the first use in a programming was by Ken Thompson’s QED text editor in the mid-1960s. He later went on to register a patent for it. In the 1980s In the 1980s Henry Spencer (1986) wrote more complex versio nfor perl and TCL. Regex functionality is built into most programming langauges by default.  

### Common Uses
The grep tool in linux uses regular expressionsas grep stands for <b>G</b>lobally search for the <b>R</b>egular <b>E</b>xpression and <b>P</b>rint  
### Summary
A regular expression (regex or regexp for short) is a special text string for describing a search pattern. "You can think of regular expressions as wildcards on steroids." (https://www.regular-expressions.info/). So regular expression is a text pattern when given to a an engine will find matches in a target text, e.g.  a "/d" (find a digit) pattern will find 3 matches in the targhet text of "1 2 3". The engine uses graph theory to parse and store the target text, prior to examine all elements for a match with the pattern.  

### Details 
#### Pattern
##### Components
Each pattern is made from a set of components these include but not limnited to 

1. matching characters 
    - "." matches any character 
    - "\\" denoates that the immediate character following performs a special match e.g. \d matches a digit 
    - literal character such as any alpha number character e.g. "a" match the letter a in the string
2. postional matches are "^" (start of target text) and "$" (end of target text)  
3. Qualifying Characters are * (zero or multiple matches), + (one or multiple matches) and ? (one or 0 matches) 
4. ranges is where the "[]" is use to specify a range e.g. [0-4] would mean any of teh characters 0, 1, 2, 3,4
5. match quanity "{m,n}" would match the preceeding pattern at min m times and at max n times. "[A-Z]{2,4}" would have a posive match if there was 2, 3 or 4  aplabetical character in a row.  

##### Complex examples
The above components can be combined in order to give complex patterns that search through the text. e.g. 
"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b" would find email address.

#### Processor
There are two kinds of regular expression engines: text-directed engines, and regex-directed engines. Jeffrey
Friedl calls them DFA and NFA engines, respectively. 
##### DFA engine
Deterministic Finite Automaton (DFA): there is always the same output for the same starting value and input. 
##### NFA engine 
Non-Deterministic Finite Automaton (NFA) : there can be multiple  outputs for the same starting value and input. 

Although they are commonly classified as "text"  or "regex" directed. 
<b>Text</b> directed process each character in the text and looks for a match in teh regexp. If none found it moves to the next character in the text.
<b>regexp</b> directed takes the a elemnt of the regexp pattern and tries to find a match in the text. If none found move to teh next element in the regexp.  

## How do regular expressions differ across implementations?
### Programming language implementations
below is an example of the differance betwwen python and java regular expessions given the smae pattern
(https://stackoverflow.com/questions/30527195/different-behavior-of-same-regular-expression-in-python-and-java)
### python regex example
```python
import re
p = re.compile("[0-9]*(?:\\.[0-9]+)?[^0-9]*D\\([MW]\\)\\s*US")
test_str = "9.5 D(M) US"
print re.search(p, test_str).group()
```
result will be:
9.5 D(M) US
 escape characters in regular expressions, \\d in Java, and \d in python

### Java regex example
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

### Text Directed Verus Regexp implementation

#### Text Directed

##### Sumarry

##### Advantages

##### Disadvantages
Doesn't have backtraking 
##### Example implementation
(Set|SetValue) on input "SetValue" will match "SetValue"
#### Regexp Directed
##### Sumarry
Starting at the first character in the target text a sub set of the pattern (form left to right) is used to verfiy that this contains a match. It adds another that sub set a repearts for verifaction of a match in the target text. If that fails it goes to the next character in the target text and repeats the process until it finds the first success in the total pattern
##### Advantages
Does have backtraking 
##### Disadvantages

##### Example implementation
(Set|SetValue) on input "SetValue" will match "Set"


## Can all formal languages be encoded as regular expressions?
 A formal language consists of words whose letters are taken from an alphabet and are well-formed according to a specific set of rules. Not formaly you regular experssion will give syntax errors due to formal languages are strict on it's rules. It is possible given that your regular expression is quite percise it would be possible. regylar expression is also drived form formal languages 

Talk about grammar.

https://web.mit.edu/6.005/www/fa15/classes/17-regex-grammars/



(https://www.oreilly.com/library/view/beautiful-code/9780596510046/ch01.html#:~:text=Stephen%20Kleene%20invented%20regular%20expressions,automata%20in%20what%20they%20represent.)
https://medium.com/@zohaibshahzadTO/regular-expressions-character-classes-findall-method-c4b4d71d353a


https://devopedia.org/regex-engines
