from automates.program_analysis.for2py.format import *
from automates.program_analysis.for2py.arrays import *

def main():
    A = Array([(1,5),(1,5)])

    for i in range(1,5+1):
        for j in range(1,5+1):
            A.set_((i,j), i+j)          # A(i,j) = i+j


    fmt_obj_10 = Format(['5(I5)'])
    fmt_obj_11 = Format(['""'])

    for i in range(1,5+1):
        sys.stdout.write(fmt_obj_10.write_line([A.get_((i,1)), A.get_((i,2)), \
                                                A.get_((i,3)), A.get_((i,4)), \
                                                A.get_((i,5))]))
    sys.stdout.write(fmt_obj_11.write_line([]))

    A_subs = idx2subs([array_values(2), array_values([1,3,5])])    # A(2, (/1,3,5/))
    A.set_elems(A_subs, 555)

    for i in range(1,5+1):
        sys.stdout.write(fmt_obj_10.write_line([A.get_((i,1)), A.get_((i,2)), \
                                                A.get_((i,3)), A.get_((i,4)), \
                                                A.get_((i,5))]))



main()
