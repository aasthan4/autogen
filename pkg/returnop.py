from . import func_ewt

def returnop2(full_con_term, output, new_list):
    new_list.append('\\{E^{')
    up=[]
    down=[]
    new_output=[] #based on the formalism that dagger comes before undaggered
    for item in output:
        if item.dag=='1' and item.string==1:
            tmp_4 = item
            new_output.append(item)
            up.append(tmp_4.name)
            new_list.append(tmp_4.name)
    for item in output :
        if ( item.dag=='1') and item.string ==2:
            tmp_4 = item
            new_output.append(item)
            up.append(tmp_4.name)
            new_list.append(tmp_4.name)
    new_list.append('}_{')
    for item in reversed(output) :
        #remember here the 1st string comes first as in writig in E has different rules than straight
        if item.dag=='0' and item.string==1:
            #print "item name is ", item.name
            tmp_4 = item
            new_output.append(item)
            down.append(tmp_4.name)
            new_list.append(tmp_4.name)
    for item in reversed(output) :
        if ( item.dag=='0') and item.string ==2:

            #print "item name is ", item.name
            tmp_4 = item
            new_output.append(item)
            down.append(tmp_4.name)
            new_list.append(tmp_4.name)
    #make and object of the operator
    op_left=func_ewt.contractedobj('op', 1, 1)
    output=new_output
    op_left.upper=up
    op_left.lower=down
    #print "op left upper ", op_left.upper
    full_con_term.append(op_left)
    new_list.append('}\\}')
    return output



def returnop(full_con_term, output, new_list):
    new_list.append('\\{E^{')
    up=[]
    down=[]
    new_output=[] #based on the formalism that dagger comes before undaggered
    new_output1=[]
    for item in output:
        if item.dag=='1':
            tmp_4 = item
            new_output.append(item)
            up.append(tmp_4.name)
            new_list.append(tmp_4.name)
    '''
    for item in output :
        if ( item.dag=='1') and item.string ==2:
            tmp_4 = item
            new_output.append(item)
            up.append(tmp_4.name)
            new_list.append(tmp_4.name)
    '''
    new_list.append('}_{')
    for item in output :
        #remember here the 1st string comes first as in writig in E has different rules than straight
        if item.dag=='0':
            #print "item name is ", item.name
            tmp_4 = item
            new_output1.append(item)
            down.append(tmp_4.name)
            new_list.append(tmp_4.name)
    '''
    for item in output :
        if ( item.dag=='0') and item.string ==2:

            #print "item name is ", item.name
            tmp_4 = item
            new_output.append(item)
            down.append(tmp_4.name)
            new_list.append(tmp_4.name)
    '''
    #make and object of the operator
    op_left=func_ewt.contractedobj('op', 1, 1)
    output=new_output
    output.extend(reversed(new_output1))
    op_left.upper=up
    op_left.lower=down[::-1]
    #print "op left upper ", op_left.upper
    full_con_term.append(op_left)
    new_list.append('}\\}')
    return output
'''

def returnop(full_con_term, output, new_list):
    new_list.append('\\{E^{')
    up=[]
    down=[]
    new_output=[] #based on the formalism that dagger comes before undaggered
    for item in output:
            tmp_4 = item
            new_output.append(item)
            up.append(tmp_4.name)
            new_list.append(tmp_4.name)
    #make and object of the operator
    op_left=func_ewt.contractedobj('op', 1, 1)
    output=new_output
    op_left.upper=up
    op_left.lower=down
    #print "op left upper ", op_left.upper
    full_con_term.append(op_left)
    new_list.append('}\\}')
    return output

'''
