def is_unique(input_str):
  input_str = input_str.lower()
  d = dict()
  for i in input_str:
    if i in d:
      d[i] +=1
    else:
      d[i] = 1

  for x in d.values():
    if x >1:
      return False
    else:
      return True

print(is_unique('abCDefGh'))
print(is_unique('nonunique'))