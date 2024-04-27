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

    def __init__(self, name, adress, note):
        self.name = name
        self.adress = adress
        self.note = note
        pass 

    def __str__(self):
        return f"{self.name} at position {self.adress}"
        pass

##########################################
def Read_DATAPOINTER_ (queue = 1):       #       POINTER >> {Line_in_Code[3]}{Name[20]}
    file = open("SFile.txt", "r")
    

    Pointer = Adressed_Item
    Pointer_block = ''

    EntireLine= list(file.readline())
    print(file.readline())
    Pointer_block = EntireLine[(queue-1)*23:queue*23]

    return (Pointer_block)


def ReturnAllPointers ():
    allPointers = {}

    return allPointers()
#    del allPointers


file = open("SFile.txt", "r")
print(file.readline())
file = open("Hello world.txt", "r")
print(file.readline())