#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    Como o counter é apenas para monitoramento da execução do sistema, utilizei variável global para facilitar as coisas, mas a funcionalidade principal do sistema está seguindo o que foi pedido na aula.
'''

counter = 0


def is_in_list(element, list):
    global counter

    for i in list:
        counter += 1
        if element == i:
            return True

    return False


def list_for_set(list):
    set = []
    global counter

    for i in list:
        counter += 1
        if (not is_in_list(i, set)):
            set.append(i)

    return set


def difference(set1, set2):
    elements = []
    global counter

    for i in set1:
        counter += 1
        if (not is_in_list(i, set2)):
            elements.append(i)

    return elements


def symmetrical_difference(set1, set2):
    elements = difference(set1, set2) + difference(set2, set1)

    return elements


def union(set1, set2):
    elements = set1 + set2
    elements = list_for_set(elements)

    return elements


def intersections(set1, set2):
    elements = []
    global counter

    for i in set1:
        counter += 1
        if (is_in_list(i, set2)):
            elements.append(i)

    return elements


list1 = ['a', 'b', 'a', 'c', 'a', 't', 'e']
list2 = ['a', 'b', 'a', 'c', 'a', 'x', 'i']

set1 = list_for_set(list1)
set2 = list_for_set(list2)

print(difference(set1, set2))
print('Na função `difference` teve {} execuções\n'.format(counter))

counter = 0
print(symmetrical_difference(set1, set2))
print('Na função `symmetrical_difference` teve {} execuções\n'.format(counter))

counter = 0
print(union(set1, set2))
print('Na função `union` teve {} execuções\n'.format(counter))

counter = 0
print(intersections(set1, set2))
print('Na função `intersections` teve {} execuções\n'.format(counter))
