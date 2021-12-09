def pal_ric(a):
    if len(a) <= 1:
        return True
    else:
        if a[0] == a[-1]:
            return pal_ric(a[1:-1])
        else:
            return False

if __name__ == "__main__":
    