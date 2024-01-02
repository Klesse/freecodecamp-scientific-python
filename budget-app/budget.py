from math import trunc


class Category:

  def __init__(self, name: str = ''):
    self.name = name[0].upper() + name[1:].lower()
    self.ledger = []

  def __str__(self):
    max_len = 0
    for item in self.ledger:
      it_len = len("{0:.2f}".format(item['amount']) + item['description'][:24])
      if it_len > max_len:
        max_len = it_len
    category_string = ''

    for item in self.ledger:
      it_len = len("{0:.2f}".format(item['amount']) + item['description'][:24])
      if max_len == it_len:
        spaces = ' ' * (max_len - it_len + 1)
      else:
        spaces = ' ' * (max_len - it_len)

      category_string += "{0}{1}{2:.2f}\n".format(item['description'][:23],
                                                  spaces, item['amount'])
    category_string += "Total: {0:.2f}".format(self.get_balance())
    star = "*" * (int(max_len - len(self.name)) // 2)
    category_string = star + self.name + star + '\n' + category_string
    return category_string

  def get_name(self):
    return self.name

  def get_balance(self) -> float:
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def get_withdraws(self) -> float:
    withdraws = 0
    for item in self.ledger:
      if item['amount'] < 0:
        withdraws += abs(item['amount'])
    return withdraws

  def check_funds(self, amount: float) -> bool:
    if (amount <= self.get_balance()):
      return True
    return False

  def deposit(self, amount: float, description: str = ''):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount: float, description: str = '') -> bool:
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def transfer(self, amount: float, budget) -> bool:
    if self.check_funds(amount):
      budget.deposit(amount, f"Transfer from {self.get_name()}")
      self.withdraw(amount, f"Transfer to {budget.get_name()}")
      return True
    return False


def sort_dict_by_value(d, reverse=True):
  return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def create_spend_chart(categories) -> str:
  total_balance, first_balance, second_balance, third_balance = 0, 0, 0, 0
  names = []

  for category in categories:
    total_balance += category.get_withdraws()
    if category.get_name() not in names:
      names.append(category.get_name())
    # Second Category
    if category.get_name() == names[0]:
      first_balance += category.get_withdraws()

    # Third Category
    elif names[1] != None and category.get_name() == names[1]:
      second_balance += category.get_withdraws()

    # Auto
    else:
      third_balance += category.get_withdraws()
  first_index = trunc((first_balance / total_balance) * 10)
  second_index = trunc((second_balance / total_balance) * 10)
  third_index = trunc((third_balance / total_balance) * 10)
  dict_to_order = {
    f"{names[0]}": first_index,
    f"{names[1]}": second_index,
    f"{names[2]}": third_index
  }
  dict_to_order = sort_dict_by_value(dict_to_order)
  index_i = 10
  first_index = index_i - list(dict_to_order.values())[2]
  second_index = index_i - list(dict_to_order.values())[0]
  third_index = index_i - list(dict_to_order.values())[1]

  # Mapping: Rows: 0 -> 10 Columns: 1, 3 and 5
  chart = [['100| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           [' 90| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           [' 80| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           [' 70| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           [' 60| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           [' 50| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           [' 40| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           [' 30| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           [' 20| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           [' 10| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           ['  0| ', ' ', '  ', ' ', '  ', ' ', '  \n'],
           ['   ', ' ----------\n']]
  # Food
  if index_i == first_index:
    chart[index_i][1] = 'o'
  else:
    for i in range(index_i, first_index - 1, -1):
      chart[i][1] = 'o'

  # Clothing
  if index_i == second_index:
    chart[index_i][3] = 'o'
  else:
    for i in range(index_i, second_index - 1, -1):
      chart[i][3] = 'o'

  # Auto
  if index_i == third_index:
    chart[index_i][5] = 'o'
  else:
    for i in range(index_i, third_index - 1, -1):
      chart[i][5] = 'o'

  chart_string = ''
  for sets in chart:
    for item in sets:
      chart_string += item
  max_name = 0
  for name in [
      list(dict_to_order.keys())[2],
      list(dict_to_order.keys())[0],
      list(dict_to_order.keys())[1]
  ]:
    if len(name) > max_name:
      max_name = len(name)
  for i in range(max_name):
    chart_string += '     '
    try:
      chart_string += list(dict_to_order.keys())[2][i] + '  '
    except IndexError:
      chart_string += '   '
    try:
      chart_string += list(dict_to_order.keys())[0][i] + '  '
    except IndexError:
      chart_string += '   '
    try:
      if i != max_name - 1:
        chart_string += list(dict_to_order.keys())[1][i] + '  \n'
      else:
        chart_string += list(dict_to_order.keys())[1][i] + '  '
    except IndexError:
      chart_string += '\n'

  return "Percentage spent by category\n" + chart_string
