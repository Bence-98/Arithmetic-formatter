def arithmetic_arranger(problems, solve=False):

  prblms = list()
  for x in problems:
    prblms.append(x.split())
    tmp = x.split()
    if tmp[1] == "*" or tmp[1] == "/":
      return "Error: Operator must be '+' or '-'."
    if not tmp[0].isdigit() or not tmp[2].isdigit():
      return "Error: Numbers must only contain digits."
    if len(tmp[0]) > 4 or len(tmp[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
  if len(prblms) > 5:
    return "Error: Too many problems."
  first, second, dashes, answers =  str(), str(), str(), str()
  for prt in prblms:
    needed_length = max(len(prt[0]), len(prt[2])) + 2
    spaces = (needed_length - len(prt[0])) * " "
    first += spaces + prt[0]
    spaces = ((needed_length - len(prt[2])) -1) * " "
    second += prt[1] + spaces + prt[2]
    dashes += needed_length * "-"
    if prt[1] == "+":
      answer = int(prt[0]) + int(prt[2])
      answer = str(answer)
    else:
      answer = int(prt[0]) - int(prt[2])
      answer = str(answer)
    spaces = (needed_length - len(answer)) * " "
    answers += spaces + answer
    first += "    "
    second += "    "
    dashes += "    "
    answers += "    "

  first = first.rstrip()
  second = second.rstrip()
  dashes = dashes.rstrip()
  answers = answers.rstrip()
  if solve == True:
    arranged_problems =first + "\n" + second + "\n" + dashes + "\n" + answers
  else:
    arranged_problems =first + "\n" + second + "\n" + dashes
  return arranged_problems