def larger(numbers: list) -> int:
  result = -1
  for number in numbers:
    if int(number) > int(result):
      result = number
  return result


def arithmetic_arranger(problems: list, display: bool = False) -> str:
  first_number = []
  second_number = []
  result_number = []
  operator = []
  larger_number = []
  if (len(problems) > 5):
    return "Error: Too many problems."
  for i, problem in enumerate(problems):
    first_number.append(problem.split(' ')[0])
    operator.append(problem.split(' ')[1])
    second_number.append(problem.split(' ')[2])
    if operator[i] != '+' and operator[i] != '-':
      return "Error: Operator must be '+' or '-'."
    if not str(first_number[i]).isdigit() or not str(
        second_number[i]).isdigit():
      return "Error: Numbers must only contain digits."
    if len(str(first_number[i])) > 4 or len(str(second_number[i])) > 4:
      return "Error: Numbers cannot be more than four digits."
    if operator[i] == '+':
      result_number.append(int(first_number[i]) + int(second_number[i]))
    else:
      result_number.append(int(first_number[i]) - int(second_number[i]))
    larger_number.append(larger([first_number[i], second_number[i]]))
  #first_line
  result = ''
  spaces = ''
  first_line = ''
  for i in range(len(problems)):
    spaces = ' ' * (len(str(larger_number[i])) - len(first_number[i]) + 2)
    first_line += spaces + str(first_number[i])
    if i != len(problems) - 1:
      first_line += '    '

  #second_line
  second_line = ''
  for i in range(len(problems)):
    spaces = ' ' * (len(str(larger_number[i])) - len(second_number[i]) + 1)
    second_line += str(operator[i]) + spaces + str(second_number[i])
    if i != len(problems) - 1:
      second_line += '    '

  # dash line
  symbol = ''
  for i in range(len(problems)):
    symbol += '-' * (len(str(larger_number[i])) + 2)
    if i != len(problems) - 1:
      symbol += '    '

  result_line = ''
  # result_line

  if display == True:
    for i in range(len(problems)):
      spaces = ' ' * (len(str(larger_number[i])) - len(str(result_number[i])) +
                      2)
      result_line += spaces + str(result_number[i])
      if i != len(problems) - 1:
        result_line += '    '
    arranged_problems = first_line + '\n' + second_line + '\n' + symbol + '\n' + result_line
  else:
    arranged_problems = first_line + '\n' + second_line + '\n' + symbol
  return arranged_problems
