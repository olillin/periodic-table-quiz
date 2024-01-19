def main():
  with open('periodic_table.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
  svar = len(lines)
  for i, line in enumerate(lines):
    line = line.strip()
    guess = ''
    while guess.lower() != line.lower():
      guess = input(f'{i+1}: ')
      if guess == '':
        print(f'Rätt svar: {line}')
        svar -= 1
  print(f'Rätta svar: {svar}')

if __name__ == '__main__':
  main()