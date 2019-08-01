class Node:
    '''
    the node to store the states and action Q value and the next step infomation
    states store the node we have put chess    
    actions contain the q value of action, achieved by dictionay
    '''
    def __init__(self,parent_node,state):
        self.states = []
        if parent_node!=None:
            self.states = [x for x in parent_node.states]
        if state != None:
            self.states.append(state)
        self.next_node = None
        self.child_node = None
        self.parent_node = parent_node
        self.actions={}
        #here I put the initial q value to the actions which doesn't contain any chess
        
        #states_len = len(self.states)
        for i in range(0,9):
            if i not in self.states:
                self.actions[i]=0
    def isEqual(self,node):
        if len(self.states) != len(node.states):
            return False
        le = len(self.states)
        for i in range(le):
            if self.states[i] != node.states[i]:
                return False
        return True



class Tree:
    '''
    this is the main class to store the data of the game
    '''
    def __init__(self,head_node):
        self.head_node = head_node

    def insert(self,parent_node,node):
        '''
        when i instert a node, i should:
        first, check if the node already in the tree
        second, find the last None node and put the new node to it
        third, set the parent node and the child node
        '''
        if parent_node.child_node == None:
            parent_node.child_node = node
            node.parent_node = parent_node
        else:
            current_node = parent_node.child_node
            while current_node.next_node!=None:
                if current_node.isEqual(node):
                    return
                current_node = current_node.next_node
            if current_node.isEqual(node):
                return
            current_node.next_node = node
            node.parent_node = current_node
            
    def find_max_actions(self,node):
        maxq = -1000000000.0
        for x in node.actions:
            if node.actions[x]>maxq:
                maxq = node.actions[x]
        return maxq


