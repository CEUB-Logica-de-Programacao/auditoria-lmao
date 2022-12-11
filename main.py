def etapa1(id):
  nums = sorted(str(id))
  if len(nums) > 4:
      return False
  new1 = int(nums[0]+nums[2])
  new2 = int(nums[1]+nums[3])
  sum = new1+new2
  return sum


def etapa2(votos):
  return list(set(range(1, len(votos)+1))-set(votos))


def etapa3(senha):
  keys = {}
  for i in senha:
    if i in keys:
        keys[i]+=1
    else:
        keys[i]=1
  ref = list(keys.values())[0]
  for i in keys.values():
    if i != ref:
      return False
  return True

while True:
    if etapa1('1234') > 100:
        print('ID inválido')
        exit(1)
    if len(etapa2([1, 1])) > 0:
        print('Voto inválido')
        exit(1)
    if not etapa3('abba'):
        print('Senha inválida')
        exit(1)
