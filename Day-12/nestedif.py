'''
fa = eval(input("follows account: "))
cf = eval(input("close friends: "))
if fa:
    if cf:
        print("story visible")
    else:
        print("not in close friend list")
else:
    print("follow the account first")
    '''
'''
registerd_fee=eval(input("registerd_fee: "))
fee_paid=eval(input("fee_paid: "))
if registerd_fee:
    if fee_paid:
         print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")
    '''


link_active = eval(input("link_active: "))
permission_granted = eval(input("permission_granted: "))
if link_active:
    if permission_granted:
        print("file opened successfully")
    else:
        print("access denied")
else:
    print("invalid file link")