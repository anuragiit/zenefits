def inorder(a):
    for i in a:
        if i==',':
            eindexofparent=a.index(i)
    parent=a[1:eindexofparent]
    stack=1
    count=0
    for i in a[eindexofparent+2:]:
        if i=='{':
            stack+=1
        elif i=='}':
            stack-=1
        count+=1
        if not stack:
            break
        
    left=a[eindexofparent+1:eindexofparent+1+count]
    
    right=a[eindexofparent+count+3:-2]
    inorder(left)
    print(parent+',')
    inorder(right)






t=int(input())
for i in range(t):
    a=input()
    inorder(a)
    
