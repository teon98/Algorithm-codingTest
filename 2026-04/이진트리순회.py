'''
* Date      : 2026.04.02
* Title     : 트리 순회
* Algorithm : 이진 트리 순회
* Level     : 실버1

https://www.acmicpc.net/problem/1991

첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다

7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

ABDCEFG
DBAECFG
DBEGFCA
'''
def preorder(tree, node): #부모 -> 왼쪽 -> 오른쪽
    if node != ".":
        print(node, end="")
        preorder(tree, tree[node][0])
        preorder(tree, tree[node][1])
    return 

def inorder(tree, node): #왼쪽 -> 부모 -> 오른쪽
    if node != ".":
        inorder(tree, tree[node][0])
        print(node, end="")
        inorder(tree, tree[node][1])
    return

def postorder(tree, node): #왼쪽 -> 오른쪽 -> 부모
    if node != ".":
        postorder(tree, tree[node][0])
        postorder(tree, tree[node][1])
        print(node, end="")
    return 

N=int(input())

tree = dict()

for i in range(N):
    parent, left, right = input().split()
    tree[parent] = (left, right)

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')