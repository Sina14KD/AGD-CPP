import math
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt

def make_edge_list(nodes_list):
    
    edge_list=[]
    
    for idx,e in enumerate(nodes_list):
        
        if idx!=len(nodes_list)-1:
            edge=[]
            n1=nodes_list[idx]
            n2=nodes_list[idx+1]
            if n2[0]-n1[0]!=0:
                m=(n2[1]-n1[1])/(n2[0]-n1[0])
                h=n1[1]-m*n1[0]
            else:
                m="inf"
                h=n1[0]
            
            edge.append(m)
            edge.append(h)
            edge_list.append(edge)
            
        else:
            edge=[]
            n1=nodes_list[idx]
            n2=nodes_list[0]
            if n2[0]-n1[0]!=0:
                m=(n2[1]-n1[1])/(n2[0]-n1[0])
                h=n1[1]-m*n1[0]
            else:
                m="inf"
                h=n1[0]
            
            edge.append(m)
            edge.append(h)
            edge_list.append(edge)
            
    return edge_list



def nodes_between_segments_lines(nodes_list,y_b,y_t):
    
    nodes=[]
    
    for n in nodes_list:
        if n[1]>y_b and n[1]<y_t:
            nodes.append(n)
            
    return nodes  

def nodes_above_and_below_topline(nodes_list,y_t):
    
    nodes=[]
    nodes_index=[]
    
    
    for idx,n in enumerate(nodes_list):
        
        if idx<len(nodes_list)-1:
            
            if nodes_list[idx][1]<=y_t and nodes_list[idx+1][1]>=y_t :
                
                nodes.append(nodes_list[idx])
                nodes.append(nodes_list[idx+1])
                nodes_index.append(idx)
                nodes_index.append(idx+1)
                
            elif nodes_list[idx][1]>=y_t and nodes_list[idx+1][1]<=y_t:
                
                nodes.append(nodes_list[idx])
                nodes.append(nodes_list[idx+1])
                nodes_index.append(idx)
                nodes_index.append(idx+1)
                
                
        else:
            
            if nodes_list[idx][1]<=y_t and nodes_list[0][1]>=y_t :
                
                nodes.append(nodes_list[idx])
                nodes.append(nodes_list[0])
                nodes_index.append(idx)
                nodes_index.append(0)
            
            elif nodes_list[idx][1]>=y_t and nodes_list[0][1]<=y_t: 
                
                nodes.append(nodes_list[idx])
                nodes.append(nodes_list[0])
                nodes_index.append(idx)
                nodes_index.append(0)
                
    
    return nodes,nodes_index
                
    


def nodes_cross_topline_edges(nodes_list,nodes_index,edges_list,y_t):
    
    nodes=[]
    cross_points=[]
    
    if nodes_index!=[]:
        edge1=edges_list[nodes_index[0]]
        edge2=edges_list[nodes_index[2]]
        
        if nodes_index[0]!=nodes_index[1] and nodes_index[2]!=nodes_index[3]:
            
            m1=edge1[0]
            m2=edge2[0]
            
            if m1!='inf':
                h1=edge1[1]
                x_cross1=(y_t-h1)/m1
                
            else: 
                x_cross1=edge1[1]
                
            if m2!='inf':
                 h2=edge2[1]
                 x_cross2=(y_t-h2)/m2
                  
            else: 
                 x_cross2=edge2[1]   
            
            cross_points.append([x_cross1,y_t])
            cross_points.append([x_cross2,y_t])

        
        elif nodes_index[0]==nodes_index[1] and nodes_index[2]!=nodes_index[3]:
            
            x_cross1=nodes_list[0][0]
            
            m2=edge2[0]
            if m2!='inf':
                 h2=edge2[1]
                 x_cross2=(y_t-h2)/m2
                  
            else: 
                 x_cross2=edge2[1]   
                 
            cross_points.append([x_cross1,y_t])
            cross_points.append([x_cross2,y_t])
        
        elif nodes_index[0]!=nodes_index[1] and nodes_index[2]==nodes_index[3]:
            
            m1=edge1[0]
            
            if m1!='inf':
                h1=edge1[1]
                x_cross1=(y_t-h1)/m1
                
            else: 
                x_cross1=edge1[1]
            
            x_cross2=nodes_list[2][0]
            cross_points.append([x_cross1,y_t])
            cross_points.append([x_cross2,y_t])
                
                
        
        elif nodes_index[0]==nodes_index[1] and nodes_index[2]==nodes_index[3]:
            
            x_cross1=nodes_list[0][0]
            x_cross2=nodes_list[2][0]
            cross_points.append([x_cross1,y_t])
            cross_points.append([x_cross2,y_t])
        
        else:
            pass
        
    return cross_points


def calculate_max_lenght(cross_points,between_points,P1):
    
    all_nodes=[]
    l_max=0
    
    if between_points!=[]:
        for p in between_points:
            all_nodes.append(p)
            
    if cross_points!=[]:
        for p in cross_points:
            all_nodes.append(p)
            
    if P1!=[]:
        for p in P1:
            all_nodes.append(p)        
    
    print("all_nodes : ",all_nodes)        
            
    # find node with min x-coordinate
    x_min = min(all_nodes, key=lambda coord: coord[0])[0]
    x_max = max(all_nodes, key=lambda coord: coord[0])[0]
    
    for p in all_nodes:
        
        if p[0]<x_min:
            
            x_min=p[0]
            x_min_point=p
            
        if p[0]>x_max:
            
            x_max=p[0]
            x_max_point=p
            
    l_max=x_max-x_min   
    
    return l_max,x_min,x_max


def number_of_cells(l_max,r):
    
    n=l_max/(math.sqrt(2)*r)
    
    return math.ceil(n)

def excess_value(n,r,l_max):
    
    e=n*math.sqrt(2)*r-l_max
    
    return e

def adjustment_value(n,e):
    
    delta=e/n
    
    return delta

def make_y_new_t(y_b,r,delta):
    
    y_new_t=y_b+math.sqrt(2*(r**2)+2*math.sqrt(2)*r*delta-(delta**2))
    
    return y_new_t

def make_nodes_between_line_segments(x_min,x_max,r,delta,y_new_t,y_b):
    
    x=x_min+((math.sqrt(2)*r-delta)/2)
    
    created_nodes_list=[]
    
    while x-((math.sqrt(2)*r-delta)/2)<x_max:
        
        created_nodes_list.append([x,y_b+((y_new_t-y_b)/2)])
        
        x=x+(math.sqrt(2)*r-delta)
        
        
    return created_nodes_list


def AGD(nodes_list,r):
    
    
    edges_list=make_edge_list(nodes_list)
    max_y = max(node[1] for node in nodes_list)
    All_cells_nodes=[]
    
    width_list=[]
    height_list=[]
    
    
    # first step value assignment to y_b and y_t
    
    y_b=0
    y_t=math.sqrt(2)*r
    
    k=0
    
    while y_b<max_y:
        k+=1
        print("============= Run While Loop : {} ==============".format(k))
        
        P1=[]  
           
        if y_b==0:
            for n in nodes_list:
                if n[1]==0:
                    P1.append(n)
                    P1.reverse()
        else:            
            nodes_p1,nodes_index_p1=nodes_above_and_below_topline(nodes_list, y_b)
            
          
            
            
            # crossing nodes
            P01=nodes_cross_topline_edges(nodes_p1, nodes_index_p1, edges_list, y_b)
            
            for p in P01:
                P1.append(p)
                
        print('P1 : ', P1)
        
        # fill P_2 list        
        # indicate points crossing the top line
        nodes,nodes_index=nodes_above_and_below_topline(nodes_list, y_t)
                
        # crossing nodes
        n_c=nodes_cross_topline_edges(nodes, nodes_index, edges_list, y_t)    
        print('P2 : ', n_c)
         
        # fill P_3 list
        n_b_s_l=nodes_between_segments_lines(nodes_list, y_b, y_t)      
        print('P3 : ',n_b_s_l)
          
        #Calculate max length
        l_max,x_min,x_max=calculate_max_lenght(n_c, n_b_s_l,P1)
        print('max_lenght : ',l_max)
        
        #Calculate n
        num_cell=number_of_cells(l_max, r)
        print("num of cells : ",num_cell)
        
        e=excess_value(num_cell, r, l_max)
        print("e: ", e)
        
        #Calcuate adjustement , delta
        delta=adjustment_value(num_cell, e)
        print("Delta: ",delta)
        
        # claculate width and height of the cell
        
        width=math.sqrt(2)*r-delta
        height=math.sqrt(2*(r**2)+2*math.sqrt(2)*r*delta-(delta**2))
        width_list.append(width)
        height_list.append(height)
        
        # Make new y_t
        y_new_t=make_y_new_t(y_b,r, delta)
        
        print('y_t_adj : ', y_new_t)
        
        # Make nodes between line segments
        nodes_between_segments=make_nodes_between_line_segments(x_min, x_max, r, delta, y_new_t,y_b)

        All_cells_nodes.append(nodes_between_segments)         
        
        #Update y_b
        y_b=y_new_t
        print("updated y_b : ",y_b)
        
        #Update y_t
        y_t=y_b+math.sqrt(2)*r
        print("updated y_t : ", y_t)
        
    final_solution=[]

    for a in All_cells_nodes:
        for i in a:
            final_solution.append(i)
            
    print("final solutions : ",final_solution)        
        
        
        
    return final_solution
        
        
        
    
    
        
#%%
"""
Code execution for the paper's example demonstrated in Fig. 2.

r : The radius of the the UAV's camera footprint

nodes_list: the list of the polygon vertices (after transformation) 
in counterclockwise order, starting with the vertex on the longest edge with the minimum X-coordinate.
"""      
nodes_list=[[0,0],[10,0],[12,5],[8,8.5],[2,8.5]] 
r=math.sqrt(2)

final_sol=AGD(nodes_list,r)
print('The number of cells: ',len(final_sol))
