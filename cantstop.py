def compute_sums(tab):
  sums=[]
  for i in range(len(tab)):
    for j in range(i+1,len(tab)):
      sums.append(tab[i]+tab[j])
  return sums

def compute_result (nb_remaining, choices, completed, draw):

    sums = compute_sums(draw)
    #print(sums)

    this_kills_you=True
    this_is_ok=False
    for s in sums:
      if s in choices :
          this_is_ok=True
      if not s in completed:
          this_kills_you = False

    if nb_remaining <=0:
      if not this_is_ok :
          final = False
      else :
          final = True
    else :
      if this_kills_you:
          final=False
      else :
          final=True

    return final
    #print ("final", final)

def get_probas(nb_remaining, choices, completed):
    #print(nb_remaining, choices,completed)


    nb_possibilities=6*6*6*6

    ok=0
    nok=0
    for i in range(1,7):
      for j in range(1,7):
         for k in range(1,7):
            for l in range(1,7):
              result = compute_result(nb_remaining, choices, completed, [i,j,k,l])
              if result :
                  ok+=1
              else :
                  nok+=1

    advance = ok/nb_possibilities
    get_lost = nok/nb_possibilities

    print(ok, nok, ok+nok)
    print(advance,get_lost,advance+get_lost)

    return advance, get_lost

'''
print (compute_result (0, [6,7,8], [], [6,5,6,4]))
print (compute_result (1, [6,7,8], [], [6,5,6,4]))
print (compute_result (1, [6,7,8], [9,10,11], [6,5,6,4]))
print (compute_result (1, [6,7,8], [9,10,11,12], [6,5,6,4]))
'''


while True:    
    print("enter possible choices")
    print("a single line with numbers_of_remaining_tokens:your_lines:completed_lines")
    print("such as :")
    print("1:6,7:")
    print("0:2,6,7:9,12")
    my_string= input()
    information = my_string.split(':')

    nb_remaining = int(information[0])
    choices = [int(e) for e in information[1].split(',')]
    completed = []
    if information[2]:
        completed = [int(e) for e in information[2].split(",")]

    advance,lose = get_probas(nb_remaining,choices,completed)

    print("for ",str(choices))

    print(" "*5,"proba are ","{:.2f}".format(advance) ," to get it and" , "{:.2f}".format(lose), "to lose")

    nth_advance=advance
    if nb_remaining<=0:
        for i in range(2,15):
            nth_advance*=advance
            print(" "*5,"after",i, "attempts","{:.2f}".format(nth_advance) ," to get it and" , "{:.2f}".format(1-nth_advance), "to lose")
