#Begin
#FAIL counters are default set to 0
Fail_counter = 0
Glob_fail_counter = 0
Max_Fails_allowed = 0
#Import of all librarys
try:    
    import Class_updater    #Class_updater.py import
    import datetime
    import Storage
    # import Pikaboobert     #Junk Library
except:
    Glob_fail_counter = 999     # Sets Gfc to the very high rate, so even all the the other tests are PASS, the overall result is FAIL. 
    print("!!!GLOBAL FAILURE 401 NO LIBRARY(S) FOUND!!!")
    pass
###########################
#Testing algorythms
def Evaluate(mod = 'none'):
    global Fail_counter, Max_Fails_allowed, Glob_fail_counter
    
    if mod == 'global':
        Fail_counter = Glob_fail_counter
    
    if Fail_counter != Max_Fails_allowed:
        Fail_counter = 0
        Glob_fail_counter += 1
        return "FAIL"
    else:
        return "PASS"       
    
def Con_Test(Library):
    global Fail_counter
    try:
        return "PASS" if Library.test else "FAIL"		
    except:
        Fail_counter+=1
        return "FAIL"

def Item_Test():
    global Fail_counter
    try:
        Item1 = Class_updater.Item("Test Title", "This is test text", 3)

        if str(Item1) == f"Test Title(3) created on {datetime.datetime.now().strftime('%x  %X')}: \n This is test text":
            return "PASS"
        else:
            return "FAIL"
    except:
        Fail_counter+=1
        return "FAIL"

def PointersTest():
    Pointer_List = Storage.ReturnAllPointers()

    if Pointer_List["TestTest_a1234567890"] == 4:
        return "PASS"
    else:
        return "FAIL"
    
###########################
#Testing of connections
print("---------TEST----------\n======CONNECTION TEST======\n")
try:
    print(f'Class_updater.py........({Con_Test(Class_updater)})')
    print(f'Main.py.................({Con_Test(Class_updater)})')
    # print(f'Pikaboobert........({Con_Test(Pikaboobert)})')
except NameError:
    print(f'NameError............(FAIL)')
print(f"====CONNECTION TEST({Evaluate()})====\n")
###########################
#Other Tests
print('=======OVERALL TEST=======\n')
print(f"Item <- Class Test......({Item_Test()})")
print(f"Pointers <- Storage.....({PointersTest()})")

###########################
#End Messege
print(f"=====OVERALL TEST({Evaluate('global')})======\n  With {Glob_fail_counter} global failures")


