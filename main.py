import random;
#   hicham benhachem  #
#                     #

# show matrix
def printMatrix(M):
    for row in M:
        print(' '.join([str(elem) for elem in row]))



# find max sq
def findSeq(M):
    row = len(M)
    col = len(M[0])
    S = [[0 for k in range(col)] for l in range(row)]

    for i in range(1, row):
        for j in range(1, col):
            if (M[i][j] == '.'):
                S[i][j] = min(S[i][j - 1], S[i - 1][j],
                              S[i - 1][j - 1]) + 1
            else:
                S[i][j] = 0


    m_s = S[0][0]
    m_i = 0
    m_j = 0
    for i in range(row):
        for j in range(col):
            if (m_s < S[i][j]):
                m_s = S[i][j]
                m_i = i
                m_j = j

    for i in range(m_i, m_i - m_s, -1):
        for j in range(m_j, m_j - m_s, -1):
            M[i][j] = '#'
    return M

# generate val
def map_gen(x, y, density):
    str1=''
    for i in range(int(y)):
        for j in range(int(x)):
            if (random.randint(0, int(y)) * 2) < int(density):
                str1+= 'o'
            else:
                str1 += '.'

    return str1

# convert string to matrix
def StringToMatrix(myStr, nmb):

	temporale = [myStr[idx: idx + nmb] for idx in range(0, len(myStr), nmb)]
	res = [list(ele) for ele in temporale]
	return res;


if __name__ == '__main__':
    lstr = map_gen(10,10,2);
    printMatrix(StringToMatrix(lstr, 10))
    print('\n')
    printMatrix(findSeq(StringToMatrix(lstr, 10)))


