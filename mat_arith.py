# There is no need to import SAMPLE_MATRICES
# Devon Taylor
# U2L4
# DS
# 10/7/24


def mat_sum(m1, m2):
    m1Row = len(m1)
    m2Col = len(m2[0])

    if m1Row == m2Col:
        new = [[0]*m1Row for i in range(m2Col)]
        m1Num = 0
        m2Num = 0

        for i in range(m1Row):
            for x in range(m2Col):
                m1Num = m1[i][x]
                m2Num = m2[i][x]
                mSum = m1Num + m2Num
                new[i][x] = mSum
        return new
    else:
        return "no solution"

def mat_mul(m1, m2):
    m1Row = len(m1)
    m1Col = len(m1[0])
    m2Row = len(m2)
    m2Col = len(m2[0])

    if m1Col == m2Row:
        new = [[0]*m2Col for i in range(m1Row)]
        for i in range(m1Row):
            for x in range(m2Col):
                for z in range(m1Col):
                    new[i][x] += m1[i][z] * m2[z][x]
        return new
    else:
        return "no solution"