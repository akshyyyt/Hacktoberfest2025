def canFormSquare(l1, b1, l2, b2, l3, b3):
    # Return "YES" if the rectangles can be arranged to form a square, otherwise return "NO"
    sum_b = b1+b2+b3
    sum_l = l1+l2+l3
    if l1 == l2 == l3 == sum_b or b1 == b2 == b3 == sum_l or l1 == (l2+l3) == (b1 + b2) == (b1+3) or b1 == (b2+b3) == (l1+l2) == (l1+l3):
        return "YES"
    else:
        return "NO"
