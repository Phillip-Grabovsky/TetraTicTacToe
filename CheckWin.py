def checkWin(move, board, player): # move: [x, y, z] AKA the address

   def check(xFunc, yFunc, zFunc):
      sumd = 0
      for i in range(4):
         sumd += board[xFunc(i)][yFunc(i)][zFunc(i)]
      return sumd == player * 4

   x = move[0]
   y = move[1]
   z = move[2]

   # z-check
   if board[x][y] == [player, player, player, player]:
       print("Player " + str(player) + " wins!")
       return True

   # x-check
   if check(lambda i: i, lambda i: y, lambda i: z):
      return True

   # y-check
   if check(lambda i: x, lambda i: i, lambda i: z):
      return True

   # diagonal check 1
   if check(lambda i: i, lambda i: i, lambda i: z):
      return True

   # diagonal check 2
   if check(lambda i: i, lambda i: 3 - i, lambda i: z):
      return True

   # diagonal check 3
   if check(lambda i: x, lambda i: i, lambda i: i):
      return True

   # diagonal check 4
   if check(lambda i: x, lambda i: 3 - i, lambda i: i):
      return True


   # diagonal check 5
   if check(lambda i: i, lambda i: y, lambda i: i):
      return True


   # diagonal check 6
   if check(lambda i: 3 - i, lambda i: y, lambda i: i):
      return True

   #Grand Diagonal Checks (4)


   #GD check 1
   if check(lambda i: i, lambda i: i, lambda i: i):
      return True

   #GD check 2
   if check(lambda i: 3 - i, lambda i: i, lambda i: i):
      return True

   #GD check 3
   if check(lambda i: i, lambda i: 3 - i, lambda i: i):
      return True

   #GD check 4
   if check(lambda i: i, lambda i: i, lambda i: 3 - i):
      return True

   return False
