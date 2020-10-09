class number_converter:
  def converter_function(self, value):
    standerdnum = [
      1000, 900, 500, 400,
      100, 90, 50, 40,
      10, 9, 5, 4,
      1
      ]
    numerals = [
      "M", "CM", "D", "CD",
      "C", "XC", "L", "XL",
      "X", "IX", "V", "IV",
      "I"
      ]
    roman_numbers = ''
    i = 0
    while  value > 0:
        for _ in range(value // standerdnum[i]):
            roman_numbers += numerals[i]
            value -= standerdnum[i]
        i += 1
    return roman_numbers
