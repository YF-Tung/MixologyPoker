#!/usr/bin/env python3
import csv
import copy
import operator

def get_bar(filename='bar.txt'):
    """ Return a set containing what you have """
    fin = open(filename)
    ls = [x.strip() for x in list(fin.readlines()) if not x.startswith('#')]
    return [x for x in ls if x]

def get_recipes(filename='poker.csv'):
    """ Return a list of (name, [ingredients]) tuple """
    with open(filename) as csvfile:
        recipes = csv.reader(csvfile)
        return [(x[0],x[1:]) for x in list(recipes)]

def main():
    recipes = get_recipes()
    bar = get_bar()
    lack_list = {}
    for _, recipe in recipes:
        lack = [x for x in recipe if x not in bar]
        num_lack = len(lack)
        if num_lack not in lack_list:
            lack_list[num_lack] = []
        lack_list[num_lack].append(lack)

    # Recipes that you can make already
    print ('You can make {} cocktail(s) currently.'.format(len(lack_list.get(0, []))))

    # Recipes that you can make by buying one
    print('==============================================================================')
    if 1 in lack_list:
        count = {}
        for x in lack_list[1]:
            if x[0] in count:
                count[x[0]] += 1
            else:
                count[x[0]] = 1
        sorted_count = sorted(count.items(), key=operator.itemgetter(1))
        for tpl in reversed(sorted_count):
            print ('You can make {} more by buying {}'.format(
                tpl[1], tpl[0]))
    else:
        print ('You cannot make more cocktails by just buying another ingredient.')

    print('==============================================================================')
    count = {}
    total_lack = [ingr for _,group in lack_list.items() for recipe in group for ingr in recipe]
    for ingr in total_lack:
        count[ingr] = 1 + count.get(ingr, 0)
    print_cnt = 0
    sorted_count = sorted(count.items(), key=operator.itemgetter(1))
    for tpl in reversed(sorted_count):
        print ('{} cocktails requires {}'.format(tpl[1], tpl[0]))
        print_cnt += 1
        if print_cnt == 10:
            break

if __name__ == '__main__':
    main()
