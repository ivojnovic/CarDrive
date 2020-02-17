from collections import deque
import copy


class Cell:
    def __init__(self, i, j, k=0):
        self.i = i
        self.j = j
        self.k = k

def pretvori(r):
    road = [["." for x in range(len(r[0]))] for y in range(3)]
    for i in range (3):
        for j in range(len(r[0])):
            road[i][j] = r[i][j]
    road[1][0] = "c"
    for item in road:
        if (item[-1]!="#"):
            item[-1] = "d"
    return road


def reconstruct_path(path, d):
    i  = d[0]
    j =  d[1]
    k =  d[2]
    #print (i,j,k)
    path[1][0] = "c"
    #print (path)
    put = []
    start = path[i][j]
    #print (start)
    while(start != "c"):
        put.append([i,j,k])
        i = start[0]
        j = start[1]
        k = start[2]
        start = path[i][j]
    put.append([1,0,0])
    reverse = put[::-1]
    print ("Promjena trake", reverse[-1][-1], "puta")
    return reverse


def minimunNumberOfDrifts(road):

    source = Cell(1,0,0)
    path = []
    visited = [[0 for x in range(len(road[0]))] for y in range(3)]

    #izbjegavamo posjecivanje barijera
    for i in range (0, 3):
        for j in range (0, len(road[0])):
            if(road[i][j] == "#"):
               visited[i][j] = "true"
            else:
                visited[i][j] = "false"

    # BFS od izvora
    q = deque([])
    q.append(source)
    visited[source.i][source.j] = "true"
    #print (visited)
    prev = [[[0,0,0] for x in range(len(road[0]))] for y in range(3)]
    try:
        while(q.count!=0):
            cvor = q.popleft()
            path.append(cvor)
            #ako je pronadeno odrediste
            if(road[cvor.i][cvor.j] == "d"):
                c = Cell(cvor.i, cvor.j, cvor.k)
                reconstruc = reconstruct_path(prev, (c.i,c.j,c.k))
                return reconstruc

            #put naprijed
            if(visited[cvor.i][cvor.j + 1] == "false" and cvor.j +1 < len(road[0])):
                prev[cvor.i][cvor.j + 1] = (cvor.i, cvor.j,cvor.k)
                c = Cell(cvor.i, cvor.j + 1, cvor.k)
                q.append(c);
                visited[cvor.i][cvor.j + 1] = "true"


            #dolje digaonalno
            if(cvor.i < 2 and visited[cvor.i+1][cvor.j+1]=="false"):
                prev[cvor.i+1][cvor.j + 1] = (cvor.i, cvor.j,cvor.k)
                c = Cell(cvor.i + 1, cvor.j + 1, cvor.k+1)
                q.append(c);
                visited[cvor.i+1][cvor.j + 1] = "true"

            #gore dijagonalno
            if(cvor.i>0 and visited[cvor.i-1][cvor.j+1]=="false"):
                prev[cvor.i-1][cvor.j + 1] = (cvor.i, cvor.j,cvor.k)
                c = Cell(cvor.i-1, cvor.j + 1, cvor.k+1)
                q.append(c);
                visited[cvor.i-1][cvor.j + 1] = "true"
    except:
        return -1


def main():
    #returns -1
    #road =	["#..#.#.##.", ".#.#...##.",".###.##.#."]

    #returns 7
    #road = ["#.###.##",".#.#.#.#","###.###."]

    #returns 7
    #road = ["#.###.##",".#.#.#.#","###.###."]

    #returns 5
    #road = ["..#....#..#.#...#..", "...#.#...#.#..#..#.", ".##..........#...#."]

    #returns 0
    road = ["....","....","...."]


    road = pretvori(road)
    lista_puta = minimunNumberOfDrifts(road)
    print ("\n")
    if (lista_puta == -1):
        print ("Ne postoji put")
    else:
        for k in lista_puta:
            put = copy.deepcopy(road)
            put[1][0] = "."
            i = k[0]
            j = k[1]
            put[i][j] = "c"
            for p in put:
                print(p)
            print("\n")

if __name__== "__main__":
    main()
