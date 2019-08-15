# type
matched_stmt
open_stmt
expr 

# branch 
if
then
else

def new_node():
    d = {
        "type":None,
        "branch":None,
        "childre":[]
    }
    return(d)


####

left_recursive
immediate_left_recursive
non_left_recursive

import elist.elist as elel

def eliminate_ilr_s0(m,n):
    arr_non_term = elel.init_range(1,m+1,1)
    arr_non_term = elel.mapiv(arr_non_term,lambda i,v:"Aa"+str(i))
    arr_term = elel.init_range(1,n+1,1)
    arr_term = elel.mapiv(arr_term,lambda i,v:"B"+str(i))
    arr = arr_non_term + arr_term 
    s = elel.join(arr,"|")
    s = "A -> " + s
    return(s)


def eliminate_ilr_s1(n):
    arr = elel.init_range(1,n+1,1)
    arr = elel.mapiv(arr,lambda i,v:"b"+str(i)+"A'")
    s = elel.join(arr,"|")
    s = "A -> " + s
    return(s)

def eliminate_ilr_s2(n):
    arr = elel.init_range(1,n+1,1)
    arr = elel.mapiv(arr,lambda i,v:"a"+str(i)+"A'")
    s = elel.join(arr,"|")
    s = "A' -> " + s + "|" + "epsilon"
    return(s)


def eliminate_ilr(arr_alpha,arr_beta,non_term="A"):
    arr_alpha_tmp = elel.mapiv(arr_alpha,lambda i,v:non_term+v)
    arr = arr_alpha_tmp + arr_beta
    s = elel.join(arr,"|")
    s = non_term + " -> " + s
    print(s)
    arr_beta = elel.mapiv(arr_beta,lambda i,v:v+non_term+"'")
    s = elel.join(arr_beta,"|")
    s = non_term + " -> " + s
    print(s)
    arr_alpha = elel.mapiv(arr_alpha,lambda i,v:v+non_term+"'" )
    s = elel.join(arr_alpha,"|")
    s = non_term + "'"  + " -> " + s +"|" + "epsilon"
    print(s)    
    
    

    
