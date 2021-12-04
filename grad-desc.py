import copy

def grad_desc(u1,u2,u3):
    v=copy.deepcopy(u1)
    for i in range(len(u1)):
        while dcost_dvi(u1,u2,u3,v,i)>0.0001 or dcost_dvi(u1,u2,u3,v,i)<-0.0001:
                v[i]=v[i]-dcost_dvi(u1,u2,u3,v,i)*0.01
    return v

def dcost_dvi(u1,u2,u3,v,i):
    return -2*(u1[i]+u2[i]+u3[i]-3*v[i])

if __name__ =='__main__':
    u1 = [1,0,0]
    u2 = [0,1,0]
    u3 = [0,0,1]
    print(grad_desc(u1,u2,u3))

