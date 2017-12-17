from Structures import Stack as Stack
from Structures import BinaryTree as BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')','^']:
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+','-','*','/','^']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    if eTree.getRootVal() == '':
        eTree.setRootVal(eTree.getLeftChild().getRootVal())
        eTree.insertLeft(None)
    return eTree

def derivative(parseTree,var):

    def operators(oper,var):
        mainRoot = parseTree    #główny trzon
        derTree = BinaryTree('')
        if var == mainRoot.getRootVal() :
            derTree.setRootVal('1')
            return derTree
        elif '-'+var == mainRoot.getRootVal():
            derTree.setRootVal('-1')
            return derTree
        elif mainRoot.getRootVal() not in ['+','-','*','/','^']:
            derTree.setRootVal('0')
            return derTree

        StackTree = Stack()     #stos do przechowywania poddrzew
        lenOper = len(oper)
        for i in range(lenOper):        #przechodzimy po każdym korzeniu od tyłu bo zaczynamy od "najgłębszych" operacji

            derTree = BinaryTree('')
            root = oper[lenOper - i - 1].getRootVal()
            lChild = oper[lenOper - i - 1].getLeftChild().getRootVal()
            rChild = oper[lenOper - i - 1].getRightChild().getRootVal()

            if root == '+' or root == '-':
                derTree.setRootVal(root)
                if var == lChild:
                    derTree.insertLeft('1')
                elif var not in lChild and lChild not in ['+','-','*','^','/']:
                    derTree.insertLeft('0')
                elif lChild == 'sin'+var:   
                    derTree.insertLeft('cosx')
                elif lChild == 'cos'+var:
                    derTree.insertLeft('-sinx')
                elif lChild == 'tg'+var:
                    derTree.insertLeft('1/(cosx*cosx)')
                elif lChild == 'ctg'+var:
                    derTree.insertLeft('-1/(sinx*sinx)')
                elif lChild in ['+','-','^','*']:
                    derTree.insertLeftTree(StackTree.pop()) #jeśli lewe dziecko jest operatorem tzn, że już zróżniczkowałem i należy poprzedni korzeń podpiąć do aktualnego 

                if var == rChild:   #analogicznie
                    derTree.insertRight('1')
                elif var not in rChild and rChild not in ['+','-','*','^','/']:
                    derTree.insertRight('0')
                elif rChild == 'sin'+var:
                    derTree.insertRight('cosx')
                elif rChild == 'cos'+var:
                    derTree.insertRight('-sinx')
                elif rChild == 'tg'+var:
                    derTree.insertRight('1/(cosx*cosx)')
                elif rChild == 'ctg'+var:
                    derTree.insertRight('-1/(sinx*sinx)')
                elif rChild in ['+','-','^','*']:
                    derTree.insertRightTree(StackTree.pop())

                StackTree.push(derTree)
                
            if root == '^':
                if lChild != var and rChild != var and lChild != '-'+var and rChild != var:
                    derTree.setRootVal(None)
                elif rChild == '2' :
                    derTree.setRootVal(lChild)
                elif rChild == var:
                    derTree.setRootVal(lChild+'^'+var+' * ln'+lChild)
                elif lChild == var and int(rChild) > 0:
                    dim = int(rChild) - 1
                    derTree.setRootVal('^')
                    derTree.insertLeft(var)
                    derTree.insertRight(dim)
                elif lChild == var and int(rChild) < 0:
                    dim = int(rChild) - 1
                    derTree.setRootVal('^')
                    derTree.insertLeft('-'+var)
                    derTree.insertRight(dim)
                elif lChild == '-'+var and int(rChild) > 0:
                    dim = int(rChild) - 1
                    derTree.setRootVal('^')
                    derTree.insertLeft(lChild)
                    derTree.insertRight(dim)
                elif lChild == '-'+var and int(rChild) < 0:
                    dim = int(rChild) - 1
                    derTree.setRootVal('^')
                    derTree.insertLeft('-'+lChild)
                    derTree.insertRight(dim)

                StackTree.push(derTree)

            if root == '*':
                if var in lChild and rChild not in ['+','-','*','^','/']:
                    if lChild == 'sin' + var:
                        derTree.setRootVal('*')
                        derTree.insertLeft('cosx')
                    if lChild == 'cos' + var:
                        derTree.setRootVal('*')
                        derTree.setRootVal('-sinx')
                    if lChild == 'tg'+var:
                        derTree.setRootVal('*')
                        derTree.setRootVal('1/(cosx*cosx)')
                    if lChild == 'ctg'+var:
                        derTree.setRootVal('*')
                        derTree.setRootVal('-1/(sinx*sinx)')
                    if var == lChild:
                        derTree.setRootVal(rChild)
                    else:
                        derTree.insertRight(rChild)

                elif var in rChild and lChild not in ['+','-','*','^','/']:
                    if rChild == 'sin' + var:
                        derTree.setRootVal('*')
                        derTree.insertRight('cosx')
                    if rChild == 'cos' + var:
                        derTree.setRootVal('*')
                        derTree.insertRight('-sinx')
                    if rChild == 'tg'+var:
                        derTree.setRootVal('*')
                        derTree.insertRight('1/(cosx*cosx)')
                    if rChild == 'ctg'+var:
                        derTree.setRootVal('*')
                        derTree.insertRight('-1/(sinx*sinx)')
                    if var == rChild:
                        derTree.setRootVal(lChild)
                    else:
                        derTree.insertLeft(lChild)

                elif lChild == '-'+var and rChild not in ['+','-','*','^','/']:
                    derTree.setRootVal('-'+rChild)
                elif rChild == '-'+var and lChild not in ['+','-','*','^','/']:
                    derTree.setRootVal('-'+lChild)
                if lChild in ['^','*'] and rChild not in ['+','-','*','^','/']:
                    derTree.setRootVal('*')
                    derTree.insertRight(rChild)
                    derTree.insertLeftTree(StackTree.pop())
                if rChild in ['^','*'] and lChild not in ['+','-','*','^','/']:
                    derTree.setRootVal('*')
                    derTree.insertLeft(lChild)
                    derTree.insertRightTree(StackTree.pop())
                if lChild in ['^','*'] and rChild in ['^','*']:
                    derTree.insertLeftTree(StackTree.pop())
                    derTree.insertRightTree(StackTree.pop())
                StackTree.push(derTree)
        return derTree

    def checkRoots(tree):
        mainRoot = tree
        roots = [mainRoot]
        i = 0
        lenRoots = 1
        while i < lenRoots:
            derTree = BinaryTree('')
            lChild = roots[i].getLeftChild()
            rChild = roots[i].getRightChild()
            k = i

            if mainRoot.getRootVal() not in ['+', '-', '*', '/', '^']:
                derTree.setRootVal('0')
                return derTree
            if lChild != None:
                if lChild.getRootVal() in ['+', '-', '*', '/', '^']:
                    roots += [lChild]
                    lenRoots += 1
                    i += 1
            if rChild != None:
                if rChild.getRootVal() in ['+', '-', '*', '/', '^']:
                    roots += [rChild]
                    lenRoots += 1
                    i += 1
            if k == i:  # wykorzystanie iteratorów do stworzenia warunku na określenie wzrostu kręgosłupa
                i += 1
        return roots

    roots = checkRoots(parseTree)
    result = operators(roots,var)
    return result
