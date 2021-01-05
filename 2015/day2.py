import src

strings = src.read()


def dimensions(string):
    split = string.split('x')
    return [int(x) for x in split]


def paper_needed(dims):
    l, w, h = sorted(dims)
    return 3*l*w + 2*w*h + 2*h*l


def ribbon_needed(dims):
    l, w, h = sorted(dims)
    return 2*l + 2*w + l*w*h


def main(presents=strings):
    dim_list = [dimensions(p) for p in presents]
    papers = [paper_needed(dims) for dims in dim_list]
    total_paper = sum(papers)
    ribbons = [ribbon_needed(dims) for dims in dim_list]
    total_ribbons = sum(ribbons)
    print(f"The total area of paper required is {total_paper} square feet.\n"
          f"The total length of ribbon required is {total_ribbons} feet.")
    return total_paper, total_ribbons


src.copy(main())
