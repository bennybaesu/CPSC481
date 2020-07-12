# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    def getActions(s, g, m, p):
        from game import Directions
        south = Directions.SOUTH
        west = Directions.WEST
        north = Directions.NORTH
        east = Directions.EAST
        print("MAP: ", m)
        actions = [g]
        t = g

        # Set the actions path equal to each node from the goal, back to the start state
        valid = True
        while valid:
            if t == s:
                valid = False
            else:
                if m[t] != s and t != s:
                    actions.append(m[t])
                t = m[t]

        # Reverse actions list so that it is in order from start to goal nodes
        actions.reverse()
        print(actions)
        c = p.getSuccessors(s)

        # Replace each node in "actions" with the direction it took to get there
        for i in range(0, len(actions)):
            for j in c:
                if actions[i] == j[0]:
                    if j[1] == 'North':
                        actions[i] = north
                    elif j[1] == 'South':
                        actions[i] = south
                    elif j[1] == 'West':
                        actions[i] = west
                    elif j[1] == 'East':
                        actions[i] = east
                    c = p.getSuccessors(j[0])
                    break

        print(actions)
        return actions

    # Initialize open stack
    opened = util.Stack()
    opened.push(problem.getStartState())

    # Closed doesn't have to be a stack, can just be a list
    closed = []

    # Temp queue for reading through the stack and putting values back in
    temp = util.Queue()

    # Parent nodes of the child to keep track of the parents
    parentMap = {

    }

    # Main algorithm loop
    while not opened.isEmpty():
        x = opened.pop()  # Top most element of stack gets popped

        children = problem.getSuccessors(x)
        closed.append(x)

        # Check if the node is already in "opened"
        while not opened.isEmpty():
            y = opened.pop()
            temp.push(y)
            for i in children:
                if i[0] == y:
                    children.remove(i)
                    continue

        # Put temp values back in opened
        while not temp.isEmpty():
            y = temp.pop()
            opened.push(y)

        counter = 0
        # Check if node is already in "closed"
        while True:
            for i in children:
                counter += 1
                if i[0] in closed:
                    children.remove(i)
                    counter = 0
                    break
            if counter == len(children):
                break

        for i in children:
            parentMap[i[0]] = x
            if problem.isGoalState(i[0]):
                return getActions(problem.getStartState(), i[0], parentMap, problem)
            opened.push(i[0])

    return []



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    def getActions(s, g, m, p):
        from game import Directions
        south = Directions.SOUTH
        west = Directions.WEST
        north = Directions.NORTH
        east = Directions.EAST
        print("MAP: ", m)
        actions = [g]
        t = g

        # Set the actions path equal to each node from the goal, back to the start state
        valid = True
        while valid:
            if t == s:
                valid = False
            else:
                if m[t] != s and t != s:
                    actions.append(m[t])
                t = m[t]

        # Reverse actions list so that it is in order from start to goal nodes
        actions.reverse()
        print(actions)
        c = p.getSuccessors(s)

        # Replace each node in "actions" with the direction it took to get there
        for i in range(0, len(actions)):
            for j in c:
                if actions[i] == j[0]:
                    if j[1] == 'North':
                        actions[i] = north
                    elif j[1] == 'South':
                        actions[i] = south
                    elif j[1] == 'West':
                        actions[i] = west
                    elif j[1] == 'East':
                        actions[i] = east
                    c = p.getSuccessors(j[0])
                    break

        print(actions)
        return actions

    # Initialize open Queue
    opened = util.Queue()
    opened.push(problem.getStartState())

    # Closed doesn't have to be a stack, can just be a list
    closed = []

    # Temp stack for reading through the stack and putting values back in
    temp = util.Stack()

    # Parent nodes of the child to keep track of the parents
    parentMap = {

    }

    # Main algorithm loop
    while not opened.isEmpty():
        x = opened.pop()  # Top most element of stack gets popped

        children = problem.getSuccessors(x)
        closed.append(x)

        # Check if the node is already in "opened"
        while not opened.isEmpty():
            y = opened.pop()
            temp.push(y)
            for i in children:
                if i[0] == y:
                    children.remove(i)
                    continue

        # Put temp values back in opened
        while not temp.isEmpty():
            y = temp.pop()
            opened.push(y)

        counter = 0
        # Check if node is already in "closed"
        while True:
            for i in children:
                counter += 1
                if i[0] in closed:
                    children.remove(i)
                    counter = 0
                    break
            if counter == len(children):
                break

        for i in children:
            parentMap[i[0]] = x
            if problem.isGoalState(i[0]):
                return getActions(problem.getStartState(), i[0], parentMap, problem)
            opened.push(i[0])

    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
