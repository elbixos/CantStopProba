def compute_sums(tab):
  sums=[]
  for i in range(len(tab)):
    for j in range(i+1,len(tab)):
      sums.append(tab[i]+tab[j])
  return sums

possible_sums = {}

for i in range(2,13):
  possible_sums[i]=0

nb_cases=0

for i in range(1,7):
  for j in range(1,7):
     for k in range(1,7):
        for l in range(1,7):
          combi = str(i)+str(j)+str(k)+str(l)
          sums = compute_sums([i,j,k,l])
          nb_cases +=1

          for s in sums:
            possible_sums[s]+=1.0

nb_possibilities = 0
for s in possible_sums:
    nb_possibilities+=possible_sums[s]
print(nb_possibilities)

proba={}
for s in possible_sums:
  proba[s]= possible_sums[s]/nb_possibilities

while True:
    print("enter possible choices")
    my_string= input()
    information = my_string.split(':')

    nb_remaining = int(information[0])
    choices = information[1].split(',')
    completed = information[2].split(",")

    print(nb_remaining, choices,completed)


    p_get=0
    for c in choices:
        p_get+=proba[int(c)]
    print("for ",str(choices), " proba are ",str(p_get) ," to get it")
