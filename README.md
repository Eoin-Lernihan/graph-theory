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
```python
import re

txt = "now stand aside worthy adversary"
x = re.search("adversary$", txt)
```
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
  public static void main(String[] args) {
    Pattern pattern = Pattern.compile("flesh", Pattern.CASE_INSENSITIVE);
    Matcher matcher = pattern.matcher("tis but a flesh wound");
    boolean matchFound = matcher.find();
    if(matchFound) {
      System.out.println("Match found");
    } else {
      System.out.println("Match not found");
    }
  }
}
```
```javascript
<!DOCTYPE html>
<html>
<body>
<p id="demo"></p>
<script>
var str = "Visit W3Schools!"; 
var n = str.search("W3Schools");
document.getElementById("demo").innerHTML = n;
</script>
</body>
</html>
```


## Can all formal languages be encoded as regular expressions?
