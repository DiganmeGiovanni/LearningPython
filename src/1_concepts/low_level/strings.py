""" Use of strings in python
This module pretends shows the use of strings and its
operations in python
"""

QUOTED = "Describing the use of 'strings' in python lang\n"
QUOTED_2 = 'Using "quotes" is intuitive'

MULTILINE = """\nLarge strings can be spanned in multiple lines
for better code readability"""

print QUOTED, QUOTED_2
print MULTILINE

##
## String formatting
first_name = 'Giovanni'
last_name = 'Aguirre'
full_name = '%s %s' % (first_name, last_name)
print '\n%s' % (full_name)


#
# Assembling large strings
# Since strings in Python are immutable, appending to a string
# requires a re-allocation. So, it is faster to append to a list,
# then use join.
large_str = []
large_str.append('\nLARGE STRING WITH LIST')
large_str.append('Line #1')
large_str.append('Line #2')
large_str.append('Line #3')
_str = '\n'.join(large_str)
print _str

#
# String formatting (Preferred way)
full_name = 'First name:{}, Last name:{}'.format('Giovanni', 'Aguirre')
print '\nFormatting string:'
print full_name
