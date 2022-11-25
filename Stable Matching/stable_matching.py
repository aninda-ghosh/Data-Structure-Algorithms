from queue_custom import MyQueue

male_pref_list = {
    0: [1, 2, 3, 0],
    1: [1, 2, 3, 0],
    2: [2, 3, 1, 0],
    3: [3, 1, 2, 0]
}

#Preference list for females to get who is ranked higher and easy for referencing.
female_pref_list = {
    0: [1, 2, 3, 0],
    1: [2, 3, 1, 0],
    2: [3, 1, 2, 0],
    3: [0, 1, 2, 3]
}

#Let's prepare the inverse preference list
female_inv_pref_list ={}

for female in female_pref_list:
    inv_pref_list = [None]*len(female_pref_list[female])
    for i,pref in enumerate(female_pref_list[female]):
        inv_pref_list[pref] = i
    female_inv_pref_list[female] = inv_pref_list

#Engagements stored in an array
#initially everyone is free
wife = [-1, -1, -1, -1]  #Storing who is whose wife #Storing husbands details
husband = [-1, -1, -1, -1] #Storing who is whose husband #Storing wives details

#We will store the proposal count here for reference
#Initially no proposals have been made.
proposal_count = [0, 0, 0, 0]

freeMale = MyQueue()

for male in male_pref_list:
    freeMale.enqueue(male)


#Let's do a O(n^2) implementation
iteration = 0
while(not freeMale.empty() and iteration < 16):
    #Get who is next in line for a proposal
    currmale = freeMale.dequeue()



    #Then we find the most valid partner for that male
    pref_list = male_pref_list[currmale]
    for (i,valid_partner) in enumerate(pref_list):
        if(valid_partner != -1):
            break
    most_valid_partner_arr_loc = i   
    most_valid_partner = valid_partner

    print("\n<------------------------------------>")
    #We print out the most valuid partner from his list of preference.
    print("Male:", currmale, ", Valid Female:", most_valid_partner)

    #check if the mostvalid partner for the current male is free or not?
    #Check1 if she is already engaged or not?
    if(wife[most_valid_partner] == -1): #She's not engaged
        print("She's Not Engaged")
        wife[most_valid_partner] = currmale #Do a temporary engagement here.
        husband[currmale] = most_valid_partner  #Also fill the husband tabel for reference.
        # proposal_count[currmale] += 1
    else: #She's engaged
        print("She's Engaged")
        #check if she wants to trade here previous engagement or not?
        prevmale = wife[most_valid_partner]
        prevmale_rank = female_inv_pref_list[most_valid_partner][prevmale]
        currmale_rank = female_inv_pref_list[most_valid_partner][currmale]
        print(currmale_rank, prevmale_rank)
        if(currmale_rank < prevmale_rank):   #She will switch
            print("She's Will Switch")
            #Destroy the old engagement
            husband[prevmale] = -1
            #make this unavailable in that male's list
            male_pref_list[prevmale][most_valid_partner_arr_loc-1] = -1
            #Enqueue him again since he is a free male again
            freeMale.enqueue(prevmale)
            
            #Form the new engagement
            wife[most_valid_partner] = currmale #Do a temporary engagement here.
            husband[currmale] = most_valid_partner  #Also fill the husband tabel for reference.
            # proposal_count[currmale] += 1
        else: #If she is not switching
            print("She's Won't Switch")
            #Mark he can't get her
            male_pref_list[currmale][most_valid_partner_arr_loc] = -1
            #Enqueue the guy one more time
            freeMale.enqueue(currmale)
    proposal_count[currmale] += 1

    
    print("Male Pref List", male_pref_list)
    print("Wife table\t", wife)
    print("Husband table\t", husband)
    print("Proposal Counts\t", proposal_count)
    print("<------------------------------------>")

    iteration += 1

for (h,w) in enumerate(husband):
        print((h,w))