msg = "닭 %d마리, 돼지%d마리, 소%d마리 다리의 합은 : %d"
legs2 = 2
legs4 = 4
chickenLegs = 0
pigLegs = 0
cowLegs = 0

chickenAfew = 0
pigAfew = 4
cowAfew = 3

if (chickenAfew > 0) : chickenLegs = chickenAfew *legs2
if (pigAfew > 0) : pigLegs = pigAfew *legs4
if (cowAfew > 0) : cowLegs = cowAfew *legs4

total = chickenLegs + pigLegs + cowLegs
print(msg % (chickenAfew, pigAfew, cowAfew, total))