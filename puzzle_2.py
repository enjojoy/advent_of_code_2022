# x = [l.strip() for l in open("in2.txt")]
# total = 0
# #A X rock
# #B Y paper
# #C Z scissors
# win = ["A Y", "B Z", "C X"]
# lose = ["A Z", "B X", "C Y"]
# draw = ["A X", "B Y", "C Z"]
# li=[]
# for i in x:

#     score = 0
#     if "X" in i.split()[1]:
#         score += 1
#     if "Y" in i.split()[1]:
#         score += 2
#     if "Z" in i.split()[1]: 
#         score += 3
#     #print(f"first {score}")

#     i = i.strip()

#     if i in win:
#         score+=6
#     if i in lose:
#         score+=0
#     if i in draw: 
#         score+=3

#     total+=score

# # print(total)

# #2
# total1=0

# for i in x:
#     score1 = 0
#     if "X" in i:
#         print(i)
#         print("i need to loose")
#         score1+=0
#         if "A" in i:
#             score1+=1
#         if "B" in i:
#             score1+=2
#         if "C" in i:
#             score1+=3
#         print(score1)
#         total1 +=score1
#     if "Y" in i:
#         print(i)
#         print("i need to draw")
#         score1+=3
#         if "A" in i:
#             score1+=1
#         if "B" in i:
#             score1+=2
#         if "C" in i:
#             score1+=3
#         print(score1)
#         total1 +=score1
#     if "Z" in i:
#         print(i)
#         print("i need to win")
#         score1+=6
#         if "A" in i:
#             score1+=1
#         if "B" in i:
#             score1+=2
#         if "C" in i:
#             score1+=3
#         print(score1)
#         total1 +=score1

# print(total1)

# X = [l.strip() for l in open('in2.txt')]
# p1 = 0
# p2 = 0
# for x in X:
#     op,me = x.split()
#     p1 += {'X': 1, 'Y': 2, 'Z': 3}[me]
#     p1 += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
#             ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
#             ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
#             }[(op, me)]

#     p2 += {'X': 0, 'Y': 3, 'Z': 6}[me]
#     p2 += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
#             ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
#             ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
#             }[(op, me)]
# print(p1)
# print(p2)


for i in range(10, 0, -1):
    print(i)

