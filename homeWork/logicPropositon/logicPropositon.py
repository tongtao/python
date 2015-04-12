# -*- coding: utf-8 -*-

import sys

#待解决命题
propositionList = ["(p|q|~r)&(p|~q|~s)&(p|~r|~s)&(~p|~q|~s)&(p|q|~s)",
                    "(~p|~q|r)&(~p|q|~s)&(p|~q|~s)&(~p|~r|~s)&(p|q|~r)&(p|~r|~s)",
                    "(p|q|r)&(p|~q|~s)&(q|~r|s)&(~p|r|s)&(~p|q|~s)&(p|~q|~r)&(~p|~q|s)&(~p|~r|~s)"]


#生成后缀表达式
def createPfixFormula( primPro ):
    elmList = []    #后缀表达式存储表
    opList = [] #操作符暂存表
    
    #遍历命题字符串
    for i in primPro:
        #遇到（入操作符列表
        if i == '(':
            opList.append('(')
        #遇到）则将操作符列表的操作符弹出到后缀表，直到（
        elif i == ')':
            while(True):
                tmp = opList.pop()
                if tmp == '(':
                    break
                else:
                    elmList.append(tmp)
        #遇到 逻辑操作符  
            #如果 opList 空则直接入栈
                        #不空则先将opList操作符弹出到elmList，
                        #直到栈空或遇到（，然后当前操作符入栈
        elif i in ['|', '&']:
            if len(opList):
                while(True):
                    tmp = opList.pop()
                    if tmp == '(':
                        opList.append('(')
                        break
                    else:
                        elmList.append(tmp)
                    if len(opList) == 0:
                        break
                opList.append(i)
            else:
                opList.append(i)
        #忽略空白字符
        elif i in [' ', '\t']:
            continue
        #其他字符直接入elmList
        else:
            elmList.append(i)
    
    #opList剩下的都送到elmList
    while len(opList):
        elmList.append(opList.pop())
    
    return elmList
    

#找到命题中的字符   
def createCharList( primPro ):
    charList = []
    
    for i in primPro:
        if i in ['|', '&', '~', ' ', '\t', '(', ')'] + charList:
            continue
        else:
            charList.append(i)
    return charList

    
#给定真值串计算命题真假
def calPro( pfixPro, valueStr, charList):
    #print pfixPro, valueStr, charList, "75"
    flag = False
    val1 = False
    val2 = False
    calList = []
    for elm in pfixPro:
        
        if elm == '|':
            var1 = calList.pop()
            var2 = calList.pop()
            #print var1, var2, var1 or var2
            if (var1 or var2):
                calList.append( True )
            else:
                calList.append( False )
        elif elm == '&':
            var1 = calList.pop()
            var2 = calList.pop()
            if (var1 and var2):
                calList.append( True )
            else:
                #print "come on!!"
                calList.append( False )
            #print calList
        elif elm == '~':
            flag = True
        else:
            if valueStr[charList.index(elm)] == '1':
                if flag is True:
                    tmp_value = False
                    flag = False
                else:
                    tmp_value = True
            elif valueStr[charList.index(elm)] == '0':
                if flag is True:
                    tmp_value = True
                    flag = False
                else:
                    tmp_value = False
            calList.append(tmp_value)
            
    return calList.pop()
        
    
#生成命题真值表
def caretValueTable( pfixPro ):
    #print pfixPro, "120"
    valueTable = []
    charList = createCharList(pfixPro)
    valueTable.append(charList)
    listLen = len(charList)
    num = 2 ** listLen
    
    formatStr = "0%db" % listLen
    
    for i in range(0, num): #range生成数列
        valueStr = format(i, formatStr)
        #print valueStr
        proValue = calPro(pfixPro, valueStr, charList)
        
        elmTable = []
        elmTable.append(proValue)
        elmTable.append(valueStr)
        
        valueTable.append(elmTable)
        
    return valueTable
    
#print caretValueTable(createPfixFormula(propositionList[1]))

#打印真值表
def printTable(primPro): 
    print primPro
    valueTable = []
    valueTable = caretValueTable(createPfixFormula(primPro))
        
    for ch in valueTable[0]:
        print ch, "\t",
    print
        
    #print valueTable
    for elmTable in valueTable[1:]:
        if elmTable[0]:
            for value in elmTable[1]:
                print value, "\t",
            print 
        
    print
    #print printTableStr(primPro)
#生成打印字符串
def printTableStr(primPro): 
    pTableStr = primPro + '\n'
    valueTable = []
    valueTable = caretValueTable(createPfixFormula(primPro))
    
    for ch in valueTable[0]:
        pTableStr = pTableStr + ch + '\t'
    pTableStr = pTableStr + '\n'
    
    for elmTable in valueTable[1:]:
        if elmTable[0]:
            for value in elmTable[1]:
                pTableStr = pTableStr + value + '\t'
            pTableStr = pTableStr + '\n'
        
    pTableStr = pTableStr + '\n'
    
    return pTableStr
    
    
#有效性检查
def validCheck(pro):
    pass

#用户输入处理
def calInput():
    proposition = raw_input('E>')
    if len(proposition) == 0:
        calInput()
        return 0
    validCheck(proposition)
    printTable(proposition)

readMe = """Hi, It's a truth table generator.
Input the number 1 or 2 or 3, you will get the truth table of prewrite proposition.
Or you may want to input your own proposition, please input E.
    |, &, ~, () are valid operational signs and serial letters won't work.
Input q for quit.
"""
if __name__ == "__main__":
    print readMe


    while(True):
    
        choice = raw_input('>')
        if choice == '1':
            printTable(propositionList[0])
        elif choice == '2':
            printTable(propositionList[1])
        elif choice == '3':
            printTable(propositionList[2])
        elif choice in ['e', 'E']:
            calInput()
        elif choice in ['q', 'Q']:
            exit(0)
        else:
            print "Invalid input"
            print
            print readMe




