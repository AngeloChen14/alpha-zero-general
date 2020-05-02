n=980
x1=2
y1=2
x2=82
y2=2
if(x1==x2 and y1==y2):
    action=n*x1+y1 
else:
    if y1!=y2:
        action=n*n+n*(n-1)*x1/2+(2*n-y1-1)*y1/2+y2-y1-1
    if x1!=x2:
        action=n*n*(n+1)/2+n*(n-1)*y1/2+(2*n-x1-1)*x1/2+x2-x1-1

if action<n*n:
    move = (int(action/n), action%n,int(action/n), action%n)
else:
    if(action<n*n*(n+1)/2):
        x1=int((action-n*n)/((n*n-n)/2))
        x2=x1
        res=(action-n*n)%((n*(n-1))/2)
        for i in range(n):
            if res<(2*n-i-2)*(i+1)/2:
                y1=i
                y2=n+res-(2*n-i-2)*(i+1)/2
                move=(x1,y1,x2,y2)
                break
    else:
        y1=int((action-n*n*(n+1)/2)/((n*n-n)/2))
        y2=y1
        res=(action-n*n*(n+1)/2)%((n*(n-1))/2)
        for i in range(n):
            if res<(2*n-i-2)*(i+1)/2:
                x1=i
                x2=n+res-(2*n-i-2)*(i+1)/2
                move=(x1,y1,x2,y2)
                break
print(move)