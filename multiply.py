def multiply_list(ilist):
    '''Takes in list variable, and outputs the product of all the values'''
    sum=1
    if len(ilist)==0: 
        return 'List is empty'
    if type(ilist) != list:
        return 'Not a list!'
    for i in ilist:
        if not type(i)==int:
            return False
        sum=i*sum
    return sum
