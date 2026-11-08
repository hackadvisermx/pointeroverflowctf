import itertools,re
w=open('babel-1522.txt').read().split('Wrapped message:')[1].strip()
A={'b3':'012','b58':'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
'b85':'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~','b7':'AEIOUYX'}
def enc(data,al):
    n=int.from_bytes(data,'big');b=len(al);o=''
    while n: n,r=divmod(n,b);o=al[r]+o
    return o or al[0]
def dec(s,al):
    n=0
    for c in s: n=n*len(al)+al.index(c)
    return n.to_bytes((n.bit_length()+7)//8,'big')
def tr_dec(s,wd=7,colmajor_write=True):
    # forward: pad, write rows, read columns. inverse: split into columns
    h=len(s)//wd
    if len(s)%wd: return None
    cols=[s[i*h:(i+1)*h] for i in range(wd)]
    return ''.join(cols[c][r] for r in range(h) for c in range(wd)).rstrip('0')
def tr_dec2(s,wd=7):
    # alt: rows of width wd read as grid where ragged
    return None
ops=['b3','b58','b85','tr']
def inv(op,s):
    try:
        if op=='tr': return tr_dec(s)
        if not all(c in A[op] for c in s): return None
        return dec(s,A[op]).decode('ascii')
    except Exception: return None
s0=dec(w,A['b7']);print(len(s0),s0[:40])
try: s0=s0.decode('ascii')
except Exception as e: print('non-ascii',s0.hex()); s0=None
res=[]
if s0:
  for p in itertools.permutations(ops):
    s=s0;ok=True;tr=[]
    for op in p:
        s=inv(op,s)
        tr.append((op,s and s[:30]))
        if s is None: ok=False;break
    print(p,ok,tr[-1])
