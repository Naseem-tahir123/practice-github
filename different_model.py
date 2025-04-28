# This is the print statement
print(2**5)
print(2**2)


# test_bad_style.py - A file with deliberate PEP 8 style errors

import os # Unused import (might not be caught by pycodestyle, but good practice)
import sys # Import not at top (E402)


# E302 expected 2 blank lines, found 1
def function_with_bad_style ( param1, param2 ): # E201 whitespace after '(', E202 whitespace before ')', E231 missing whitespace after ','
    # E111 indentation is not a multiple of 4 (assuming 4-space indent)
   result = param1+param2 # E225 missing whitespace around operator '+'

   print(result, "is the value") # E231 missing whitespace after ','

   if result > 10 : # E225 missing whitespace around operator '>', E271 multiple spaces after keyword 'if'
       print ("Result is large!") # E211 whitespace before '('
       # E117 over-indented
           pass # Over-indented


   # E501 line too long
   very_very_very_long_variable_name_that_is_clearly_designed_to_exceed_the_standard_pep8_line_length_limit = "this string makes the line too long"


   # E701 multiple statements on one line (colon)
   if result < 5: print('Small number'); x=1


   return result


# E303 too many blank lines (more than 2)



# E265 block comment should start with '# '
#block comment without space

another_var=10 # E225 missing whitespace around operator '='. E261 at least two spaces before inline comment

# Call the function
output = function_with_bad_style( 5, 3)
print (f"Final output:{output}") # E211 whitespace before '('



