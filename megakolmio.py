p1 = ('a+', 'b+', 'b-')         # Alphabet = animal id; + = face, - = chest.
p2 = ('c-', 'a+', 'b-')         # Index: [base side, left side, right side].
p3 = ('b+', 'a+', 'b-')
p4 = ('b-', 'a+', 'a-')
p5 = ('a-', 'a+', 'c-')
p6 = ('c+', 'c-', 'b-')
p7 = ('b+', 'b-', 'c+')
p8 = ('c-', 'c+', 'a+')
p9 = ('a+', 'b-', 'a-')

all_triangles = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

def fail(side1, side2):      # Non-matching test for sides of two triangles.
    return (side1[0] != side2[0]) or (side1[1] == side2[1])

def rot(triangle, rotation):
    return triangle[rotation:] + triangle[:rotation]

x = [[0, 0], [1, 2], [2, 1], [1, 0], [4, 2], [5, 1], [3, 0], [6, 2], [7, 1]]
y = [[2, 0], [2, 2], [3, 1], [5, 0], [5, 2], [6, 1], [7, 0], [7, 2], [8, 1]]
critical = { 3: [0, 2], 4: [2, 3], 6: [3, 5], 7: [5, 6], 8: [6, 8], 9: [8, 9]}

def match(triangles, rotations):     # Megakolmio test. 
    n = len(triangles)
    if not n in critical: return True
    for i in range(critical[n][0], critical[n][1]):
        if fail(rot(triangles[x[i][0]], rotations[x[i][0]])[x[i][1]],
                rot(triangles[y[i][0]], rotations[y[i][0]])[y[i][1]]):
            return False
    return True

def solve(triangles, fix_tri=[], fix_rot=[]):
    if not match(fix_tri, fix_rot): return []
    if len(fix_tri) == 9: return [fix_tri]
    return [s for t in triangles
            for n in range(3)
            for s in solve(triangles - set([t]), fix_tri + [t], fix_rot + [n])]

for solution in solve(set(all_triangles)):
    string_rep = ('P' + str(all_triangles.index(t) + 1) for t in solution)
    print('[' + ', '.join(string_rep) + ']')
