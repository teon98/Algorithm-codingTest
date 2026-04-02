'''
* Date      : 2026.04.02
* Title     : 트리 순회
* Algorithm : 이진 트리 순회
* Level     : 실버1

https://www.acmicpc.net/problem/1920

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
N=int(input())
tree = [0]*26

for i in range(N):
    parent, left, right = input().split()
    