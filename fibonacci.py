#!/usr/bin/python
# -*- coding: utf-8 -*-

def fibonacciInteractive(number):
    previous_number = 0
    next_number = 1
    sum_number = 1
    result = 0

    for n in range(0, number + 1):
        result = previous_number
        sum_number = next_number + previous_number
        previous_number = next_number
        next_number = sum_number

    return result


def fibonacciRecursive(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    return fibonacciRecursive(number - 1) + fibonacciRecursive(number - 2)
