def arithmetic_arranger(problems, show_results=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = {"top": [], "bottom": [], "lines": [], "results": []}
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem should have exactly two numbers and one operator"
        
        num1, operator, num2 = parts
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits"
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits"
        
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'"
        
        max_len = max(len(num1), len(num2))
        width = max_len + 2
        
        arranged_problems["top"].append(num1.rjust(width))
        arranged_problems["bottom"].append(operator + num2.rjust(width - 1))  # Left-align the operator
        arranged_problems["lines"].append('-' * width)
        
        if show_results:
            result = str(eval(problem))
            arranged_problems["results"].append(result.rjust(width))  # Right-align the result

    top_line = '     '.join(arranged_problems["top"])
    bottom_line = '     '.join(arranged_problems["bottom"])
    lines = '     '.join(arranged_problems["lines"])
    results_line = '     '.join(arranged_problems["results"]) if show_results else ""
    
    return '\n'.join([top_line, bottom_line, lines, results_line]).strip()

# Test cases
print('Sin resultados:\n')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print('\n__________________________________\n')
print('Con resultados:\n')
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
