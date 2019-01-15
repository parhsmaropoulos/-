text = input("enter file path:")


def ridofcomments(text):
 file = open(text, encoding='utf-8')
 for i in file.read().splitlines():
     list = [i]
     string ="".join(list)
     newline = ''
     for j in range(len(string)):
          if string[j] == '#':
            break
          else:
             newline += string[j]
     print(newline)
 file.close()

ridofcomments(text)

