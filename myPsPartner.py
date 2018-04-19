import pickle
import os.path
class myPsPartner():


    def __init__(self):
        self.nextProblem = None
        self.solvedProblem  = None


        if os.path.isfile("./nextProblem.pickle"):
            self.nextProblem = pickle.load(open('nextProblem.pickle','rb'))
        else:
            self.nextProblem = dict()
            pickle.dump(self.nextProblem, open( "nextProblem.pickle", "wb"))

        if os.path.isfile("./solvedProblem.pickle"):
            self.solvedProblem = pickle.load(open("solvedProblem.pickle","rb"))
        else:
            self.solvedProblem = list()
            pickle.dump(self.solvedProblem, open("solvedProblem.pickle","wb"))


    def iSolved(self, problems):
        for problem in problems.split(" "):
            self.solvedProblem.append(problem)

        self.refresh()
    def refresh(self):
        for problem in self.solvedProblem:
            if problem in self.nextProblem:
                self.nextProblem.pop(problem)
        pickle.dump(self.nextProblem, open("nextProblem.pickle", "wb"))
        pickle.dump(self.nextProblem, open("solvedProblem.pickle","wb"))

    def insertRival(self, problems):
        for problem in problems.split(" "):
            if problem in self.nextProblem:
                self.nextProblem[problem] += 1
            else:
                self.nextProblem[problem] = 1
        self.refresh()

    def nextProblem(self, numP = 3):
        num = numP
        for key, value in sorted(self.nextProblem.iteritems(), key=lambda (k,v): (v,k)):
            if num > 0:
                print "%s: %s" % (key, value)
            else:
                pass

mpp = myPsPartner()

while(True):
    a = raw_input("I to insert, N to recommend, S to update Solved Q to quit"):

    if a == "I":

    elif a == "N":


    elif a == "S":
        mpp.iSolved(raw_input("insert problems"))
    elif a == "Q":
        break
    else:
        print "retry"
        pass
