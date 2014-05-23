# -*- coding: utf-8 -*-
# Copyright (c) 2014, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
from rdflib import Graph

from schema.ShEx import GroupRule, AndRule, XorRule, ArcRule
from EvalContext import EvalContext
from evalCardinality import evalCardinality
from optValiditySyns import *
from utils.trace import trace_rule

from rdfops import triplesForSubject, triplesForObject
from predicateFilter import evalPredicateFilter
from subjectSpecification import evalSubjectSpecification
from objectSpecification import evalObjectSpecification

from dispatch import dispatch



def evaluate(s, g, i):
    return P if evalRule(EvalContext(s,g), i, ruleFor(s,s.start)) in [Z,P] else F

def ruleFor(s, label):
    for r in s.shape:
        if r.label == label:
            return r.orderedContent()[0].value
    return None

def evalRule(ec, i, r):
    if isinstance(r, GroupRule):
        return evalGroupRule(ec, i, r)
    elif isinstance(r, AndRule):
        return evalAndRule(ec, i, r)
    elif isinstance(r, XorRule):
        return evalXorRule(ec, i, r)
    elif isinstance(r, ArcRule):
        return evalArcRule(ec, i, r)
    else:
        return evalRevArcRule(ec,i, r)

@trace_rule
def evalArcRule(ec, i, ar):
    sg = evalPredicateFilter(ar.p, triplesForSubject(i, ec.graph))
    res = evalCardinality(sg, ar.min, ar.max)
    if res == P:
        res = evalObjectSpecification(ec, ar.o, sg)
    if res == P:
        res = dispatch(ar.action, sg, ec)
    return res


@trace_rule
def evalRevArcRule(ec, o, rar):
    og = evalPredicateFilter(rar.p, triplesForObject(o, ec.graph))
    res = evalCardinality(og, rar.min, rar.max)
    if res == P:
        res = evalSubjectSpecification(ec, rar.s, og)
    if res == P:
        res = dispatch(rar.action, og, ec)
    return res


@trace_rule
def evalGroupRule(ec, i, r):
    res = evalRule(ec, i, r.orderedContent()[0].value)
    if res == D and r.optional:
        res = Z
    elif res == P:
        res =  dispatch(r.action, Graph(), ec)
    return res

And = {
    D : {D: D, Z: D, F: F, P: F, E: E},
    Z : {D: D, Z: Z, F: F, P: P, E: E},
    F : {D: F, Z: F, F: F, P: F, E: E},
    P : {D: F, Z: P, F: F, P: P, E: E},
    E : {D: E, Z: E, F: E, P: E, E: E}}

@trace_rule
def evalAndRule(ec, i, r):
    return reduce(lambda a1, a2: And[a1][a2], map(lambda e: evalRule(ec, i, e.value), r.orderedContent()), Z)


Xor = {
    D : {D: D, Z: Z, F: D, P: P, E: E},
    Z : {D: Z, Z: Z, F: Z, P: P, E: E},
    F : {D: D, Z: Z, F: F, P: P, E: E},
    P : {D: P, Z: P, F: P, P: E, E: E},
    E : {D: E, Z: E, F: E, P: E, E: E}}

@trace_rule
def evalXorRule(ec, i, r):
    return reduce(lambda a1, a2: Xor[a1][a2], map(lambda e: evalRule(ec, i, e.value),r.orderedContent()), F)


