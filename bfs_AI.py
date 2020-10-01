initial_state = [[2,0,3],[1,8,4],[7,6,5]]

final_state = [[1,2,3],[8,0,4],[7,6,5]]

val = 0
#checking whether the inital abd final state are Same or not
def areSame(A,B):
   for i in range(3):
      for j in range(3):
         if (A[i][j] != B[i][j]):
            return False
   return True

# counting the number of mismatches

def mismatches(A,B):
   count_different = 0
   for i in range(3):
      for j in range(3):
         if (A[i][j]!=B[i][j] and A[i][j]!=0):
            count_different += 1
   return count_different

# movements of the 0 box in all directions
# in this I have simply swappped the 0 box with the correct direction and then counted mismatches .
def moveDown(initial_state,row_index,column_index):

   initial_state[row_index][column_index] , initial_state[row_index+1][column_index] = initial_state[row_index+1][column_index],initial_state[row_index][column_index]
   different_elements = mismatches(initial_state,final_state)
   initial_state[row_index+1][column_index],initial_state[row_index][column_index]=initial_state[row_index][column_index] , initial_state[row_index+1][column_index]
   
   return different_elements

def moveUp(initial_state,row_index,column_index):

   initial_state[row_index][column_index] , initial_state[row_index-1][column_index]= initial_state[row_index-1][column_index], initial_state[row_index][column_index]
   different_elements=mismatches(initial_state,final_state)
   initial_state[row_index-1][column_index], initial_state[row_index][column_index]=initial_state[row_index][column_index] , initial_state[row_index-1][column_index]
  

   return different_elements

def moveLeft(initial_state,row_index,column_index):

   initial_state[row_index][column_index], initial_state[row_index][column_index-1] = initial_state[row_index][column_index-1], initial_state[row_index][column_index]
   different_elements=mismatches(initial_state,final_state)
   initial_state[row_index][column_index-1], initial_state[row_index][column_index]=initial_state[row_index][column_index], initial_state[row_index][column_index-1]

   return different_elements

def moveRight(initial_state,row_index,column_index):

   initial_state[row_index][column_index] , initial_state[row_index][column_index+1] = initial_state[row_index][column_index+1],initial_state[row_index][column_index]
   different_elements=mismatches(initial_state,final_state)
   initial_state[row_index][column_index+1],initial_state[row_index][column_index]=initial_state[row_index][column_index] , initial_state[row_index][column_index+1]

   return different_elements




parent = 65
open_list = []
parent_heuristic= mismatches(initial_state,final_state)
node = (chr(parent),parent_heuristic)
open_list.append(node)
closed_list = []
while areSame(initial_state,final_state)!=True:
    
    
   entry_one =1000
   entry_two = 1000
   entry_three = 1000
   entry_four = 1000
   #this is the shorthand code for finding the index of 0 box , i copied it from stack overflow
   index = [(index, row.index(val)) for index, row in enumerate(initial_state) if val in row]

   (row_index , column_index) = index[0]

    
   if row_index != 0:
        entry_one= moveUp(initial_state,row_index,column_index)        
   if column_index!=0:
        entry_four= moveLeft(initial_state,row_index,column_index)
   if column_index != 2:
        entry_two= moveRight(initial_state,row_index,column_index)
   if row_index != 2:
        entry_three = moveDown(initial_state,row_index,column_index)

   

   # finding the minimum heuristic value

   min_entry = min(entry_one,entry_two,entry_three,entry_four)
   check_list = []
   check_list.append(entry_one)
   check_list.append(entry_two)
   check_list.append(entry_three)
   check_list.append(entry_four)
  
   if min_entry == entry_one:
        initial_state[row_index][column_index] , initial_state[row_index-1][column_index]= initial_state[row_index-1][column_index], initial_state[row_index][column_index]
   elif min_entry == entry_two:
        initial_state[row_index][column_index] , initial_state[row_index][column_index+1] = initial_state[row_index][column_index+1],initial_state[row_index][column_index]
   elif min_entry == entry_three:
        initial_state[row_index][column_index] , initial_state[row_index+1][column_index] = initial_state[row_index+1][column_index],initial_state[row_index][column_index]
   else:
        initial_state[row_index][column_index], initial_state[row_index][column_index-1] = initial_state[row_index][column_index-1], initial_state[row_index][column_index]
   
   for i in range(4):
      if check_list[i]!= 1000:
            parent += 1
            node = (chr(parent),check_list[i])
            open_list.append(node)
      
   for tup in open_list:
      p,h = tup
      if(h == min_entry):
         closed_list.append(tup)
   
   
   print(f"Open list elements are : {open_list}")
   print(f"Closed list elements are : {closed_list}")
   
print("Final Path is ")
print("A")
for tup in closed_list:
   print(f"{tup[0]}")


