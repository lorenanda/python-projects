def arithmetic_arranger(problems, statprint=False):
    # check problem list
    first = ''
    second = ''
    sumx = ''
    lines = ''
    # maximal problems is 5
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # split problem to separate components
    for i in problems:
        a = i.split()
        firsts = a[0]
        seconds = a[2]
        operands = a[1]
        # check the length of the number, max 4 digits
        if (len(firsts) > 4 or len(seconds) > 4):
            return "Error: Numbers cannot be more than four digits."

        # check the input as valid digits
        if not firsts.isnumeric() or not seconds.isnumeric():
            return "Error: Numbers must only contain digits."

        if (operands == '+' or operands == '-'):
            if operands == "+":
                sums = str(int(firsts) + int(seconds))
            else:
                sums = str(int(firsts) - int(seconds))
            # set length of sum and top, bottom and line values
            length = max(len(firsts), len(seconds)) + 2
            top = str(firsts).rjust(length)
            bottom = operands + str(seconds).rjust(length - 1)
            line = ''
            res = str(sums).rjust(length)
            for s in range(length):
                line += '-'
            # add to the overall string
            
            if i != problems[-1]:
              first += top + '    '
              second += bottom + '    '
              lines += line + '    '
              sumx += res + '    '
            else:
              first += top
              second += bottom
              lines += line
              sumx += res
        else:
            return "Error: Operator must be '+' or '-'."
    # strip out spaces to the right of the string
    first.rstrip()
    second.rstrip()
    lines.rstrip()
    if statprint:
        sumx.rstrip()
        arranged_problems = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        arranged_problems = first + '\n' + second + '\n' + lines
    return arranged_problems
    

from arithmetic_arranger import arithmetic_arranger
from unittest import main
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# Run unit tests automatically
main(module='test_module', exit=False)