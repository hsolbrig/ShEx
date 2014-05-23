# -*- coding: utf-8 -*-
# Copyright (c) 2014, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
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

from rdflib import RDFS, XSD, URIRef, Literal

from ShEx.optValiditySyns import *
from ShEx.rdfops import toLiteral
from ShEx.iriOrStem import stemCompare

def evalValueType(vt, n):
    if vt == RDFS.Resource and isinstance(n, URIRef):
        return P
    elif vt == XSD.string and (not n.datatype or n.datatype == XSD.string):
        return P
    else:
        return P if vt == n.datatype else F

def evalInclusion(mvs, n):
    if mvs.iri:
        for i in mvs.iri:
            if URIRef(i) == n:
                return P

    if mvs.stem:
        for s in mvs.stem:
            if stemCompare(n,s):
                return P

    if mvs.literal:
        for l in mvs.literal:
            if toLiteral(l) == n:
                return P
    return F


def evalExclusion(mvs, n):
    return F if evalInclusion(mvs, n) == P else P

def evalShape(ec, vr, n):
    from ShEx.evaluate import evalRule, ruleFor
    return evalRule(ec, n, ruleFor(ec.schema,vr)) if not isinstance(n, Literal) else F
