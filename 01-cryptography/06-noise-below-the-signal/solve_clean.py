import re,sys
from fractions import Fraction as F
src=open('solve.py').read()
ns={}
exec(src.split('def mod_q')[0],ns)
A,b,n,q,m=ns['A'],ns['b'],15,1601,30
import numpy as np
def lll(Bm,delta=0.99):
    Bm=[list(r) for r in Bm];k=len(Bm)
    def gs():
        X=np.array(Bm,dtype=float);Bs=np.zeros_like(X);mu=np.zeros((k,k))
        for i in range(k):
            v=X[i].copy()
            for j in range(i):
                mu[i,j]=X[i]@Bs[j]/(Bs[j]@Bs[j]);v-=mu[i,j]*Bs[j]
            Bs[i]=v
        return Bs,mu
    Bs,mu=gs();i=1
    while i<k:
        ch=False
        for j in range(i-1,-1,-1):
            r=int(round(mu[i,j]))
            if r:
                Bm[i]=[a-r*c for a,c in zip(Bm[i],Bm[j])];Bs,mu=gs()
        if Bs[i]@Bs[i]>=(delta-mu[i,i-1]**2)*(Bs[i-1]@Bs[i-1]): i+=1
        else:
            Bm[i],Bm[i-1]=Bm[i-1],Bm[i];Bs,mu=gs();i=max(i-1,1)
    return Bm
# row-reduce A^T (n x m) mod q to [I|C]
M=[[A[j][i]%q for j in range(m)] for i in range(n)]
for c in range(n):
    p=next(r for r in range(c,n) if M[r][c]%q)
    M[c],M[p]=M[p],M[c];inv=pow(M[c][c],-1,q);M[c]=[x*inv%q for x in M[c]]
    for r in range(n):
        if r!=c and M[r][c]:
            f=M[r][c];M[r]=[(x-f*y)%q for x,y in zip(M[r],M[c])]
basis=[M[i]+[0] for i in range(n)]+[[0]*n+[q if j==i else 0 for j in range(m-n)]+[0] for i in range(m-n)]
Wt=3
basis.append([x%q for x in b]+[Wt])
R=lll(basis)
for r in R:
    if abs(r[-1])==Wt and max(abs(x) for x in r[:-1])<=3:
        e=[x*(1 if r[-1]==-Wt else -1)*-1 for x in r[:-1]] if False else None
        # r = (A s - b)*(+-1) in first coords with last=+-Wt ; b - A s = e
        sgn=1 if r[-1]==Wt else -1
        err=[sgn*x for x in r[:-1]]  # = b - A s... check below
        print('err',err)
        # solve A s = b - err mod q (try both signs)
        for sg in (1,-1):
            t=[(b[i]-sg*err[i])%q for i in range(m)]
            # gauss on first n rows
            Mx=[A[i][:]+[t[i]] for i in range(m)]
            Mx=[[x%q for x in row] for row in Mx]
            ok=True
            for c in range(n):
                p=next((r2 for r2 in range(c,m) if Mx[r2][c]),None)
                if p is None: ok=False;break
                Mx[c],Mx[p]=Mx[p],Mx[c];iv=pow(Mx[c][c],-1,q);Mx[c]=[x*iv%q for x in Mx[c]]
                for r2 in range(m):
                    if r2!=c and Mx[r2][c]:
                        f=Mx[r2][c];Mx[r2]=[(x-f*y)%q for x,y in zip(Mx[r2],Mx[c])]
            if not ok: continue
            s=[Mx[i][n] for i in range(n)]
            bad=[ (sum(A[i][j]*s[j] for j in range(n))-b[i]+q//2)%q-q//2 for i in range(m)]
            if all(abs(x)<=3 for x in bad): print('SECRET',s,'\nerrors',bad)
