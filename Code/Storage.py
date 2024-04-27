#This library manages the storage of data

def test ():
    return True

####### Data   Storage   Structure ######
#
#   DATA POINTERS[L--1]
#       POINTER >> {Line_in_Code[3] }{Name[20]}   
#
#   DATA STORED 
#       Massive of lines. Lines are adressed in Line_in_Code. 1 line >> 1 file
#       DATA_LINE Sructure:
#               [:70]>POINTER   {PROPS_IN_USE [1]}                  << [0]
#                               {PROP1_P {Name[10]}{Adress[4]} }    << [1:14]
#                               {PROP2_P {Name[10]}{Adress[4]} }    << [15:28]
#                               {PROP3_P {Name[10]}{Adress[4]} }    << [29:42]
#                               {PROP4_P {Name[10]}{Adress[4]} }    << [43:56]
#                               {PROP5_P {Name[10]}{Adress[4]} }    << [57:70]
#           
#           [71:1120]>DATA      {PROP1 {Name[10]}{Data[200]}}   << [71:280]
#                               {PROP1 {Name[10]}{Data[200]}}   << [281:490]
#                               {PROP1 {Name[10]}{Data[200]}}   << [491:700]
#                               {PROP1 {Name[10]}{Data[200]}}   << [701:910]
#                               {PROP1 {Name[10]}{Data[200]}}   << [911:1120]
#
##########################################


class Adressed_Item:

    def __init__(self, name ="", adress=0, note=""):
        self.name = name
        self.adress = adress
        self.note = note
        pass 

    def __str__(self):
        return f"{self.name} at position {self.adress}"
        pass

##########################################
def group(Input_List):
    result=""
    for i in range(0, len(Input_List)):
        result += str(Input_List[i])
    
    return result

def Read_DATAPOINTER_ (queue = 1):       #       POINTER >> {Line_in_Code[3]}{Name[20]}
    file = open("Code\SFile.txt", "r")         #For whatsoever reason I MUST add ~Code\~

    Pointer = Adressed_Item()
    Pointer_block = ''

    EntireLine= list(file.readline())
    Pointer_block = EntireLine[(queue-1)*23:queue*23]       #somehow - it works!
    del EntireLine
    try:
        Pointer.adress=int(group(Pointer_block[0:3]))
        Pointer.name=group(Pointer_block[3:])
    except ValueError:
        Pointer.adress='PunPun'
        pass

    return (Pointer)


def ReturnAllPointers ():

    allPointers = {}
    i = 1
    while Read_DATAPOINTER_(i).adress != 'PunPun':
        allPointers[f"{str(Read_DATAPOINTER_(i).name)}"] = Read_DATAPOINTER_(i).adress
        i += 1

    return allPointers
#    del allPointers


#print(Read_DATAPOINTER_(2))

print(ReturnAllPointers())