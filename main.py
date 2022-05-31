# Hope Crisafi
# Problem set 7
# 6/4/21
# this is a program that determines if congressional districts are gerrymandered


def print_introduction():
    print()
    print("This program allows you to search through data about")
    print("congresssional voting districts and determine whether")
    print("a particular state is gerrymandered.")
    print()


def get_state():
    stateInput = input('enter a state: ')
    stateInput = stateInput.lower()
    return stateInput


def get_eligible_voters(state, filename):
    myFile = open(filename, 'r')

    for line in myFile:

        textSplit = line.split(',')
        stateLower = textSplit[0].lower()

        if stateLower == state:
            # print(state, 'has', textSplit[1], 'voters')
            return textSplit[1]
    return False


def get_district_info(state, filename):
    myFile = open(filename, 'r')

    stateList = []

    for value in myFile:

        data = value.split(',')
        stateLowercase = data[0].lower()

        if stateLowercase == state:
            for index in range(1, len(data), 3):
                list2 = []
                list2.append(data[index])
                list2.append(data[index + 1])
                list2.append(data[index + 2])
                stateList.append(list2)

    return stateList


def wasted_votes(district_info):
    democratList = []
    republicanList = []
    demWaste = []
    repWaste = []

    for index in district_info:
        if index[0] == 'AL':
            return 'cannot be gerrymandered'

    for value in district_info:
        democrat = int(value[1])
        republican = int(value[2])
        democratList.append(democrat)
        republicanList.append(republican)

        if republican == min(democrat, republican):
            repWaste.append(republican)
            voteTotal = democrat + republican
            waste = voteTotal - ((voteTotal / 2) + 1)
            demWaste.append(waste)
            # return demWaste

        elif democrat == min(democrat, republican):
            demWaste.append(democrat)
            voteTotal = democrat + republican
            waste = voteTotal - ((voteTotal / 2) + 1)
            repWaste.append(waste)
            # return repWaste

        totalDem = sum(democratList)
        totalRep = sum(republicanList)
        totalVotes = totalDem + totalRep
        demWasteTotal = sum(demWaste)
        repWasteTotal = sum(repWaste)

    print('democrat votes wasted: ', demWasteTotal)
    print('republican votes wasted: ', repWasteTotal)

    if totalRep > totalDem:
        votesWaste = repWasteTotal - demWasteTotal
        votePercentage = votesWaste / totalVotes

        if votePercentage >= .07:
            print('gerrymandered to foavor republicans')
        else:
            print('district not gerrymandered')

    else:  # totalDem > totalRep:
        votesWaste = demWasteTotal - repWasteTotal
        votePercentage = votesWaste / totalVotes

        if votePercentage >= .07:
            print('gerrymandered to favor democrats')
        else:
            print('not gerrymandered')


def eligible_voters(number_voters):
    print('eligible voters: ', number_voters)
    # return number_voters


def main():
    print_introduction()
    state = get_state()
    number_voters = get_eligible_voters(state, "eligible_voters.txt")
    if number_voters == False:
        print("\"" + state + "\" not found.")
    else:
        district_info = get_district_info(state, "districts.txt")
        votesWasted = wasted_votes(district_info)
        eligibleVoters = eligible_voters(number_voters)


main()

# get_district_info('Ohio', 'districts.txt')
