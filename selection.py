
def sort(args):
    for i in range(1,len(args)):
        adjust_position(args[:i+1],args[i],i)

    return args

def adjust_position(arr, val,index):
    for i in range(0,len(arr)):
        if(arr[i] >= val):
            arr.insert(i-1,val);
            del arr[index]
            print(arr)
