from collections import defaultdict

def get_symbol_counts(ds):
    n_symbols = 0
    symbol_counts = defaultdict(int)
    for _, y in ds:
        for s in y.decode('ascii'):
            symbol_counts[s] += 1
            n_symbols += 1
    return symbol_counts, n_symbols

def get_iupac_names(ds):
    names = set()
    for x, y in ds:
        names.add(y)
    return names

def name_len_counts(names):
    name_lens =  map(lambda x: len(x), list(names))

    l_counts = defaultdict(lambda: 0)
    for l in sorted(name_lens):
        l_counts[l] += 1
    return l_counts

def samples_per_course(len_counts, cutoffs):
    cutoffs.append(1e10)
    course_counts = defaultdict(lambda: 0)
    curr_course = 0
    c = cutoffs[0]
    ls = len_counts.keys()
    for l in ls:
        course_counts[curr_course] += len_counts[l]
        if l > c:
            curr_course += 1
            c = cutoffs[curr_course]
    return course_counts

def build_curriculum(ds, cutoffs):
    n_courses = len(cutoffs)
    courses = [list() for _ in range(n_courses)]
    for x,y in ds:
        for i in range(n_courses):
            if len(y) <= cutoffs[i]:
                courses[i].append((x,y))
    return courses
