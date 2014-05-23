# ../ShEx/schema/ShEx.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d193fe7699f2aaf319c41d48f87f3f3e590b3ad4
# Generated 2014-05-16 11:21:24.055416 by PyXB version 1.2.3
# Namespace http:/www.w3.org/shex/

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1f8898b3-dd16-11e3-a92b-c82a1438c957')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http:/www.w3.org/shex/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http:/www.w3.org/shex/}IRIstem
class IRIstem (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IRIstem')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 187, 4)
    _Documentation = None
IRIstem._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'IRIstem', IRIstem)

# Atomic simple type: {http:/www.w3.org/shex/}OptValidity
class OptValidity (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OptValidity')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 214, 4)
    _Documentation = None
OptValidity._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OptValidity, enum_prefix=None)
OptValidity.PASS = OptValidity._CF_enumeration.addEnumeration(unicode_value=u'PASS', tag=u'PASS')
OptValidity.FAIL = OptValidity._CF_enumeration.addEnumeration(unicode_value=u'FAIL', tag=u'FAIL')
OptValidity.NOMATCH = OptValidity._CF_enumeration.addEnumeration(unicode_value=u'NOMATCH', tag=u'NOMATCH')
OptValidity.DUNNO = OptValidity._CF_enumeration.addEnumeration(unicode_value=u'DUNNO', tag=u'DUNNO')
OptValidity.ERROR = OptValidity._CF_enumeration.addEnumeration(unicode_value=u'ERROR', tag=u'ERROR')
OptValidity._InitializeFacetMap(OptValidity._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'OptValidity', OptValidity)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 230, 20)
    _Documentation = None
STD_ANON._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 233, 20)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.unbounded = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'unbounded', tag=u'unbounded')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Union simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_2 (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON, STD_ANON_."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 228, 12)
    _Documentation = None

    _MemberTypes = ( STD_ANON, STD_ANON_, )
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2)
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2.unbounded = u'unbounded'               # originally STD_ANON_.unbounded
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration,
   STD_ANON_2._CF_pattern)

# Complex type {http:/www.w3.org/shex/}Schema with content type ELEMENT_ONLY
class Schema_ (pyxb.binding.basis.complexTypeDefinition):
    """A  consists of a set of labeled rules and the optional label that
                identifies the starting rule (entry point) in the Schema"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Schema')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 9, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shape'), 'shape', '__httpwww_w3_orgshex_Schema__httpwww_w3_orgshexshape', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 15, 12), )

    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpwww_w3_orgshex_Schema__start', pyxb.binding.datatypes.IDREF, required=True)
    __start._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 17, 8)
    __start._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 17, 8)
    
    start = property(__start.value, __start.set, None, None)

    _ElementMap.update({
        __shape.name() : __shape
    })
    _AttributeMap.update({
        __start.name() : __start
    })
Namespace.addCategoryObject('typeBinding', u'Schema', Schema_)


# Complex type {http:/www.w3.org/shex/}LabeledRule with content type ELEMENT_ONLY
class LabeledRule (pyxb.binding.basis.complexTypeDefinition):
    """A LabeledRule is the combination of a Rule and a label that
                uniquely identifies it within the context of a Schema. A Label can either be a URI or a Blank Node
                identifier."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LabeledRule')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 21, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}and uses Python identifier and_
    __and = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'and'), 'and_', '__httpwww_w3_orgshex_LabeledRule_httpwww_w3_orgshexand', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12), )

    
    and_ = property(__and.value, __and.set, None, None)

    
    # Element {http:/www.w3.org/shex/}arc uses Python identifier arc
    __arc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'arc'), 'arc', '__httpwww_w3_orgshex_LabeledRule_httpwww_w3_orgshexarc', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12), )

    
    arc = property(__arc.value, __arc.set, None, None)

    
    # Element {http:/www.w3.org/shex/}rarc uses Python identifier rarc
    __rarc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rarc'), 'rarc', '__httpwww_w3_orgshex_LabeledRule_httpwww_w3_orgshexrarc', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12), )

    
    rarc = property(__rarc.value, __rarc.set, None, None)

    
    # Element {http:/www.w3.org/shex/}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'group'), 'group', '__httpwww_w3_orgshex_LabeledRule_httpwww_w3_orgshexgroup', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http:/www.w3.org/shex/}xor uses Python identifier xor
    __xor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'xor'), 'xor', '__httpwww_w3_orgshex_LabeledRule_httpwww_w3_orgshexxor', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12), )

    
    xor = property(__xor.value, __xor.set, None, None)

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__httpwww_w3_orgshex_LabeledRule_label', pyxb.binding.datatypes.ID)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 28, 8)
    __label._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 28, 8)
    
    label = property(__label.value, __label.set, None, None)

    _ElementMap.update({
        __and.name() : __and,
        __arc.name() : __arc,
        __rarc.name() : __rarc,
        __group.name() : __group,
        __xor.name() : __xor
    })
    _AttributeMap.update({
        __label.name() : __label
    })
Namespace.addCategoryObject('typeBinding', u'LabeledRule', LabeledRule)


# Complex type {http:/www.w3.org/shex/}AndRule with content type ELEMENT_ONLY
class AndRule (pyxb.binding.basis.complexTypeDefinition):
    """An  consists of a set of rules, all of which must not fail in order
                for the entire rule to pass."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AndRule')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}and uses Python identifier and_
    __and = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'and'), 'and_', '__httpwww_w3_orgshex_AndRule_httpwww_w3_orgshexand', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12), )

    
    and_ = property(__and.value, __and.set, None, None)

    
    # Element {http:/www.w3.org/shex/}arc uses Python identifier arc
    __arc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'arc'), 'arc', '__httpwww_w3_orgshex_AndRule_httpwww_w3_orgshexarc', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12), )

    
    arc = property(__arc.value, __arc.set, None, None)

    
    # Element {http:/www.w3.org/shex/}rarc uses Python identifier rarc
    __rarc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rarc'), 'rarc', '__httpwww_w3_orgshex_AndRule_httpwww_w3_orgshexrarc', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12), )

    
    rarc = property(__rarc.value, __rarc.set, None, None)

    
    # Element {http:/www.w3.org/shex/}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'group'), 'group', '__httpwww_w3_orgshex_AndRule_httpwww_w3_orgshexgroup', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http:/www.w3.org/shex/}xor uses Python identifier xor
    __xor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'xor'), 'xor', '__httpwww_w3_orgshex_AndRule_httpwww_w3_orgshexxor', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12), )

    
    xor = property(__xor.value, __xor.set, None, None)

    _ElementMap.update({
        __and.name() : __and,
        __arc.name() : __arc,
        __rarc.name() : __rarc,
        __group.name() : __group,
        __xor.name() : __xor
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AndRule', AndRule)


# Complex type {http:/www.w3.org/shex/}GroupRule with content type ELEMENT_ONLY
class GroupRule (pyxb.binding.basis.complexTypeDefinition):
    """A GroupRule of a rule, a sequence of actions that are to be
                "executed" if the rule returns  when evaluated against a graph and an optionality
                indicator that determines whether the graph must meet the """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GroupRule')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 57, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}and uses Python identifier and_
    __and = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'and'), 'and_', '__httpwww_w3_orgshex_GroupRule_httpwww_w3_orgshexand', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12), )

    
    and_ = property(__and.value, __and.set, None, None)

    
    # Element {http:/www.w3.org/shex/}arc uses Python identifier arc
    __arc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'arc'), 'arc', '__httpwww_w3_orgshex_GroupRule_httpwww_w3_orgshexarc', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12), )

    
    arc = property(__arc.value, __arc.set, None, None)

    
    # Element {http:/www.w3.org/shex/}rarc uses Python identifier rarc
    __rarc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rarc'), 'rarc', '__httpwww_w3_orgshex_GroupRule_httpwww_w3_orgshexrarc', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12), )

    
    rarc = property(__rarc.value, __rarc.set, None, None)

    
    # Element {http:/www.w3.org/shex/}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'group'), 'group', '__httpwww_w3_orgshex_GroupRule_httpwww_w3_orgshexgroup', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http:/www.w3.org/shex/}xor uses Python identifier xor
    __xor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'xor'), 'xor', '__httpwww_w3_orgshex_GroupRule_httpwww_w3_orgshexxor', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12), )

    
    xor = property(__xor.value, __xor.set, None, None)

    
    # Element {http:/www.w3.org/shex/}action uses Python identifier action
    __action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'action'), 'action', '__httpwww_w3_orgshex_GroupRule_httpwww_w3_orgshexaction', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 66, 12), )

    
    action = property(__action.value, __action.set, None, None)

    
    # Attribute optional uses Python identifier optional
    __optional = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'optional'), 'optional', '__httpwww_w3_orgshex_GroupRule_optional', pyxb.binding.datatypes.boolean, required=True)
    __optional._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 68, 8)
    __optional._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 68, 8)
    
    optional = property(__optional.value, __optional.set, None, None)

    _ElementMap.update({
        __and.name() : __and,
        __arc.name() : __arc,
        __rarc.name() : __rarc,
        __group.name() : __group,
        __xor.name() : __xor,
        __action.name() : __action
    })
    _AttributeMap.update({
        __optional.name() : __optional
    })
Namespace.addCategoryObject('typeBinding', u'GroupRule', GroupRule)


# Complex type {http:/www.w3.org/shex/}XorRule with content type ELEMENT_ONLY
class XorRule (pyxb.binding.basis.complexTypeDefinition):
    """An  consists of a set of rules, exactly one of which must pass for the
                entire rule to pass."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'XorRule')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 104, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}and uses Python identifier and_
    __and = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'and'), 'and_', '__httpwww_w3_orgshex_XorRule_httpwww_w3_orgshexand', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12), )

    
    and_ = property(__and.value, __and.set, None, None)

    
    # Element {http:/www.w3.org/shex/}arc uses Python identifier arc
    __arc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'arc'), 'arc', '__httpwww_w3_orgshex_XorRule_httpwww_w3_orgshexarc', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12), )

    
    arc = property(__arc.value, __arc.set, None, None)

    
    # Element {http:/www.w3.org/shex/}rarc uses Python identifier rarc
    __rarc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rarc'), 'rarc', '__httpwww_w3_orgshex_XorRule_httpwww_w3_orgshexrarc', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12), )

    
    rarc = property(__rarc.value, __rarc.set, None, None)

    
    # Element {http:/www.w3.org/shex/}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'group'), 'group', '__httpwww_w3_orgshex_XorRule_httpwww_w3_orgshexgroup', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12), )

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http:/www.w3.org/shex/}xor uses Python identifier xor
    __xor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'xor'), 'xor', '__httpwww_w3_orgshex_XorRule_httpwww_w3_orgshexxor', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12), )

    
    xor = property(__xor.value, __xor.set, None, None)

    _ElementMap.update({
        __and.name() : __and,
        __arc.name() : __arc,
        __rarc.name() : __rarc,
        __group.name() : __group,
        __xor.name() : __xor
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'XorRule', XorRule)


# Complex type {http:/www.w3.org/shex/}PredicateFilter with content type ELEMENT_ONLY
class PredicateFilter (pyxb.binding.basis.complexTypeDefinition):
    """The filter for a set of predicates in a graph."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PredicateFilter')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 115, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}inclusion uses Python identifier inclusion
    __inclusion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'inclusion'), 'inclusion', '__httpwww_w3_orgshex_PredicateFilter_httpwww_w3_orgshexinclusion', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 121, 16), )

    
    inclusion = property(__inclusion.value, __inclusion.set, None, None)

    
    # Element {http:/www.w3.org/shex/}exclusion uses Python identifier exclusion
    __exclusion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'exclusion'), 'exclusion', '__httpwww_w3_orgshex_PredicateFilter_httpwww_w3_orgshexexclusion', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 126, 16), )

    
    exclusion = property(__exclusion.value, __exclusion.set, None, None)

    _ElementMap.update({
        __inclusion.name() : __inclusion,
        __exclusion.name() : __exclusion
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'PredicateFilter', PredicateFilter)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 122, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}iri uses Python identifier iri
    __iri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iri'), 'iri', '__httpwww_w3_orgshex_CTD_ANON_httpwww_w3_orgshexiri', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12), )

    
    iri = property(__iri.value, __iri.set, None, None)

    
    # Element {http:/www.w3.org/shex/}stem uses Python identifier stem
    __stem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'stem'), 'stem', '__httpwww_w3_orgshex_CTD_ANON_httpwww_w3_orgshexstem', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12), )

    
    stem = property(__stem.value, __stem.set, None, None)

    _ElementMap.update({
        __iri.name() : __iri,
        __stem.name() : __stem
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 127, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}iri uses Python identifier iri
    __iri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iri'), 'iri', '__httpwww_w3_orgshex_CTD_ANON__httpwww_w3_orgshexiri', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12), )

    
    iri = property(__iri.value, __iri.set, None, None)

    
    # Element {http:/www.w3.org/shex/}stem uses Python identifier stem
    __stem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'stem'), 'stem', '__httpwww_w3_orgshex_CTD_ANON__httpwww_w3_orgshexstem', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12), )

    
    stem = property(__stem.value, __stem.set, None, None)

    _ElementMap.update({
        __iri.name() : __iri,
        __stem.name() : __stem
    })
    _AttributeMap.update({
        
    })



# Complex type {http:/www.w3.org/shex/}ObjectSpecification with content type ELEMENT_ONLY
class ObjectSpecification (pyxb.binding.basis.complexTypeDefinition):
    """A  is a predicate used against the list of targets in a
                graph"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ObjectSpecification')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 136, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}valueType uses Python identifier valueType
    __valueType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'valueType'), 'valueType', '__httpwww_w3_orgshex_ObjectSpecification_httpwww_w3_orgshexvalueType', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 142, 12), )

    
    valueType = property(__valueType.value, __valueType.set, None, None)

    
    # Element {http:/www.w3.org/shex/}inclusion uses Python identifier inclusion
    __inclusion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'inclusion'), 'inclusion', '__httpwww_w3_orgshex_ObjectSpecification_httpwww_w3_orgshexinclusion', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 143, 12), )

    
    inclusion = property(__inclusion.value, __inclusion.set, None, None)

    
    # Element {http:/www.w3.org/shex/}exclusion uses Python identifier exclusion
    __exclusion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'exclusion'), 'exclusion', '__httpwww_w3_orgshex_ObjectSpecification_httpwww_w3_orgshexexclusion', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 148, 12), )

    
    exclusion = property(__exclusion.value, __exclusion.set, None, None)

    
    # Element {http:/www.w3.org/shex/}shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shape'), 'shape', '__httpwww_w3_orgshex_ObjectSpecification_httpwww_w3_orgshexshape', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 153, 12), )

    
    shape = property(__shape.value, __shape.set, None, None)

    _ElementMap.update({
        __valueType.name() : __valueType,
        __inclusion.name() : __inclusion,
        __exclusion.name() : __exclusion,
        __shape.name() : __shape
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ObjectSpecification', ObjectSpecification)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 144, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}iri uses Python identifier iri
    __iri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iri'), 'iri', '__httpwww_w3_orgshex_CTD_ANON_2_httpwww_w3_orgshexiri', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 200, 12), )

    
    iri = property(__iri.value, __iri.set, None, None)

    
    # Element {http:/www.w3.org/shex/}stem uses Python identifier stem
    __stem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'stem'), 'stem', '__httpwww_w3_orgshex_CTD_ANON_2_httpwww_w3_orgshexstem', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 201, 12), )

    
    stem = property(__stem.value, __stem.set, None, None)

    
    # Element {http:/www.w3.org/shex/}literal uses Python identifier literal
    __literal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'literal'), 'literal', '__httpwww_w3_orgshex_CTD_ANON_2_httpwww_w3_orgshexliteral', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 202, 12), )

    
    literal = property(__literal.value, __literal.set, None, None)

    _ElementMap.update({
        __iri.name() : __iri,
        __stem.name() : __stem,
        __literal.name() : __literal
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 149, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}iri uses Python identifier iri
    __iri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iri'), 'iri', '__httpwww_w3_orgshex_CTD_ANON_3_httpwww_w3_orgshexiri', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 200, 12), )

    
    iri = property(__iri.value, __iri.set, None, None)

    
    # Element {http:/www.w3.org/shex/}stem uses Python identifier stem
    __stem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'stem'), 'stem', '__httpwww_w3_orgshex_CTD_ANON_3_httpwww_w3_orgshexstem', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 201, 12), )

    
    stem = property(__stem.value, __stem.set, None, None)

    
    # Element {http:/www.w3.org/shex/}literal uses Python identifier literal
    __literal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'literal'), 'literal', '__httpwww_w3_orgshex_CTD_ANON_3_httpwww_w3_orgshexliteral', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 202, 12), )

    
    literal = property(__literal.value, __literal.set, None, None)

    _ElementMap.update({
        __iri.name() : __iri,
        __stem.name() : __stem,
        __literal.name() : __literal
    })
    _AttributeMap.update({
        
    })



# Complex type {http:/www.w3.org/shex/}SubjectSpecification with content type ELEMENT_ONLY
class SubjectSpecification (pyxb.binding.basis.complexTypeDefinition):
    """A  is a predicate used against the list of subjects in a
                graph"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SubjectSpecification')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 158, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}inclusion uses Python identifier inclusion
    __inclusion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'inclusion'), 'inclusion', '__httpwww_w3_orgshex_SubjectSpecification_httpwww_w3_orgshexinclusion', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 164, 12), )

    
    inclusion = property(__inclusion.value, __inclusion.set, None, None)

    
    # Element {http:/www.w3.org/shex/}exclusion uses Python identifier exclusion
    __exclusion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'exclusion'), 'exclusion', '__httpwww_w3_orgshex_SubjectSpecification_httpwww_w3_orgshexexclusion', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 169, 12), )

    
    exclusion = property(__exclusion.value, __exclusion.set, None, None)

    
    # Element {http:/www.w3.org/shex/}shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shape'), 'shape', '__httpwww_w3_orgshex_SubjectSpecification_httpwww_w3_orgshexshape', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 174, 12), )

    
    shape = property(__shape.value, __shape.set, None, None)

    _ElementMap.update({
        __inclusion.name() : __inclusion,
        __exclusion.name() : __exclusion,
        __shape.name() : __shape
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SubjectSpecification', SubjectSpecification)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 165, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}iri uses Python identifier iri
    __iri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iri'), 'iri', '__httpwww_w3_orgshex_CTD_ANON_4_httpwww_w3_orgshexiri', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12), )

    
    iri = property(__iri.value, __iri.set, None, None)

    
    # Element {http:/www.w3.org/shex/}stem uses Python identifier stem
    __stem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'stem'), 'stem', '__httpwww_w3_orgshex_CTD_ANON_4_httpwww_w3_orgshexstem', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12), )

    
    stem = property(__stem.value, __stem.set, None, None)

    _ElementMap.update({
        __iri.name() : __iri,
        __stem.name() : __stem
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 170, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}iri uses Python identifier iri
    __iri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iri'), 'iri', '__httpwww_w3_orgshex_CTD_ANON_5_httpwww_w3_orgshexiri', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12), )

    
    iri = property(__iri.value, __iri.set, None, None)

    
    # Element {http:/www.w3.org/shex/}stem uses Python identifier stem
    __stem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'stem'), 'stem', '__httpwww_w3_orgshex_CTD_ANON_5_httpwww_w3_orgshexstem', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12), )

    
    stem = property(__stem.value, __stem.set, None, None)

    _ElementMap.update({
        __iri.name() : __iri,
        __stem.name() : __stem
    })
    _AttributeMap.update({
        
    })



# Complex type {http:/www.w3.org/shex/}Literal with content type ELEMENT_ONLY
class Literal (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http:/www.w3.org/shex/}Literal with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Literal')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 179, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}lexicalValue uses Python identifier lexicalValue
    __lexicalValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'lexicalValue'), 'lexicalValue', '__httpwww_w3_orgshex_Literal_httpwww_w3_orgshexlexicalValue', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 181, 12), )

    
    lexicalValue = property(__lexicalValue.value, __lexicalValue.set, None, None)

    
    # Element {http:/www.w3.org/shex/}dataType uses Python identifier dataType
    __dataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dataType'), 'dataType', '__httpwww_w3_orgshex_Literal_httpwww_w3_orgshexdataType', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 182, 12), )

    
    dataType = property(__dataType.value, __dataType.set, None, None)

    
    # Element {http:/www.w3.org/shex/}langTag uses Python identifier langTag
    __langTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'langTag'), 'langTag', '__httpwww_w3_orgshex_Literal_httpwww_w3_orgshexlangTag', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 183, 12), )

    
    langTag = property(__langTag.value, __langTag.set, None, None)

    _ElementMap.update({
        __lexicalValue.name() : __lexicalValue,
        __dataType.name() : __dataType,
        __langTag.name() : __langTag
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Literal', Literal)


# Complex type {http:/www.w3.org/shex/}EvalContext with content type ELEMENT_ONLY
class EvalContext_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http:/www.w3.org/shex/}EvalContext with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EvalContext')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 207, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}schema uses Python identifier schema
    __schema = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'schema'), 'schema', '__httpwww_w3_orgshex_EvalContext__httpwww_w3_orgshexschema', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 209, 12), )

    
    schema = property(__schema.value, __schema.set, None, None)

    
    # Element {http:/www.w3.org/shex/}graph uses Python identifier graph
    __graph = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'graph'), 'graph', '__httpwww_w3_orgshex_EvalContext__httpwww_w3_orgshexgraph', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 210, 12), )

    
    graph = property(__graph.value, __graph.set, None, None)

    _ElementMap.update({
        __schema.name() : __schema,
        __graph.name() : __graph
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'EvalContext', EvalContext_)


# Complex type {http:/www.w3.org/shex/}ArcRule with content type ELEMENT_ONLY
class ArcRule (pyxb.binding.basis.complexTypeDefinition):
    """An  consists of a  that selects a subset of the
                target graph and a list and a  that the resulting subset must meet. It
                also carries an optional minimum () and maximum () number of triples
                that can meet the filter requirements as well as a collection of  that are
                "executed" if the graph passes the filter rules"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ArcRule')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 71, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}p uses Python identifier p
    __p = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'p'), 'p', '__httpwww_w3_orgshex_ArcRule_httpwww_w3_orgshexp', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 81, 12), )

    
    p = property(__p.value, __p.set, None, None)

    
    # Element {http:/www.w3.org/shex/}o uses Python identifier o
    __o = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'o'), 'o', '__httpwww_w3_orgshex_ArcRule_httpwww_w3_orgshexo', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 82, 12), )

    
    o = property(__o.value, __o.set, None, None)

    
    # Element {http:/www.w3.org/shex/}action uses Python identifier action
    __action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'action'), 'action', '__httpwww_w3_orgshex_ArcRule_httpwww_w3_orgshexaction', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 83, 12), )

    
    action = property(__action.value, __action.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'min'), 'min', '__httpwww_w3_orgshex_ArcRule_min', pyxb.binding.datatypes.nonNegativeInteger, unicode_default=u'1')
    __min._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 226, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 226, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max'), 'max', '__httpwww_w3_orgshex_ArcRule_max', STD_ANON_2, unicode_default=u'1')
    __max._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 227, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 227, 8)
    
    max = property(__max.value, __max.set, None, None)

    _ElementMap.update({
        __p.name() : __p,
        __o.name() : __o,
        __action.name() : __action
    })
    _AttributeMap.update({
        __min.name() : __min,
        __max.name() : __max
    })
Namespace.addCategoryObject('typeBinding', u'ArcRule', ArcRule)


# Complex type {http:/www.w3.org/shex/}RevArcRule with content type ELEMENT_ONLY
class RevArcRule (pyxb.binding.basis.complexTypeDefinition):
    """A  is the same as an  except that the selector
                goes from object to subject."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RevArcRule')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 88, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http:/www.w3.org/shex/}p uses Python identifier p
    __p = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'p'), 'p', '__httpwww_w3_orgshex_RevArcRule_httpwww_w3_orgshexp', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 95, 12), )

    
    p = property(__p.value, __p.set, None, None)

    
    # Element {http:/www.w3.org/shex/}o uses Python identifier o
    __o = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'o'), 'o', '__httpwww_w3_orgshex_RevArcRule_httpwww_w3_orgshexo', False, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 96, 12), )

    
    o = property(__o.value, __o.set, None, None)

    
    # Element {http:/www.w3.org/shex/}actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'actions'), 'actions', '__httpwww_w3_orgshex_RevArcRule_httpwww_w3_orgshexactions', True, pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 97, 12), )

    
    actions = property(__actions.value, __actions.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'min'), 'min', '__httpwww_w3_orgshex_RevArcRule_min', pyxb.binding.datatypes.nonNegativeInteger, unicode_default=u'1')
    __min._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 226, 8)
    __min._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 226, 8)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max'), 'max', '__httpwww_w3_orgshex_RevArcRule_max', STD_ANON_2, unicode_default=u'1')
    __max._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 227, 8)
    __max._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 227, 8)
    
    max = property(__max.value, __max.set, None, None)

    _ElementMap.update({
        __p.name() : __p,
        __o.name() : __o,
        __actions.name() : __actions
    })
    _AttributeMap.update({
        __min.name() : __min,
        __max.name() : __max
    })
Namespace.addCategoryObject('typeBinding', u'RevArcRule', RevArcRule)


Schema = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Schema'), Schema_, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', Schema.name().localName(), Schema)

EvalContext = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EvalContext'), EvalContext_, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 206, 4))
Namespace.addCategoryObject('elementBinding', EvalContext.name().localName(), EvalContext)



Schema_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shape'), LabeledRule, scope=Schema_, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 15, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Schema_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shape')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 15, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Schema_._Automaton = _BuildAutomaton()




LabeledRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'and'), AndRule, scope=LabeledRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12)))

LabeledRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'arc'), ArcRule, scope=LabeledRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12)))

LabeledRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rarc'), RevArcRule, scope=LabeledRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12)))

LabeledRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'group'), GroupRule, scope=LabeledRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12)))

LabeledRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xor'), XorRule, scope=LabeledRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LabeledRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'and')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LabeledRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'arc')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LabeledRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rarc')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LabeledRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'group')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LabeledRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xor')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LabeledRule._Automaton = _BuildAutomaton_()




AndRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'and'), AndRule, scope=AndRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12)))

AndRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'arc'), ArcRule, scope=AndRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12)))

AndRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rarc'), RevArcRule, scope=AndRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12)))

AndRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'group'), GroupRule, scope=AndRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12)))

AndRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xor'), XorRule, scope=AndRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AndRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'and')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AndRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'arc')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AndRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rarc')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AndRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'group')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AndRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xor')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AndRule._Automaton = _BuildAutomaton_2()




GroupRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'and'), AndRule, scope=GroupRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12)))

GroupRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'arc'), ArcRule, scope=GroupRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12)))

GroupRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rarc'), RevArcRule, scope=GroupRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12)))

GroupRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'group'), GroupRule, scope=GroupRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12)))

GroupRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xor'), XorRule, scope=GroupRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12)))

GroupRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'action'), pyxb.binding.datatypes.anyType, scope=GroupRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 66, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 66, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroupRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'and')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroupRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'arc')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroupRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rarc')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroupRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'group')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroupRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xor')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GroupRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'action')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 66, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GroupRule._Automaton = _BuildAutomaton_3()




XorRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'and'), AndRule, scope=XorRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12)))

XorRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'arc'), ArcRule, scope=XorRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12)))

XorRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rarc'), RevArcRule, scope=XorRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12)))

XorRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'group'), GroupRule, scope=XorRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12)))

XorRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xor'), XorRule, scope=XorRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XorRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'and')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 38, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XorRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'arc')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 39, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XorRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rarc')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 40, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XorRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'group')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 41, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XorRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xor')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 42, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
XorRule._Automaton = _BuildAutomaton_4()




PredicateFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'inclusion'), CTD_ANON, scope=PredicateFilter, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 121, 16)))

PredicateFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'exclusion'), CTD_ANON_, scope=PredicateFilter, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 126, 16)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PredicateFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'inclusion')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 121, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PredicateFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'exclusion')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 126, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PredicateFilter._Automaton = _BuildAutomaton_5()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iri'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stem'), IRIstem, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iri')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stem')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_6()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iri'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stem'), IRIstem, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 128, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iri')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stem')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_7()




ObjectSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'valueType'), pyxb.binding.datatypes.anyURI, scope=ObjectSpecification, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 142, 12)))

ObjectSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'inclusion'), CTD_ANON_2, scope=ObjectSpecification, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 143, 12)))

ObjectSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'exclusion'), CTD_ANON_3, scope=ObjectSpecification, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 148, 12)))

ObjectSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shape'), pyxb.binding.datatypes.IDREF, scope=ObjectSpecification, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 153, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObjectSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'valueType')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 142, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObjectSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'inclusion')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 143, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObjectSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'exclusion')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 148, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObjectSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shape')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 153, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObjectSpecification._Automaton = _BuildAutomaton_8()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iri'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 200, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stem'), IRIstem, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 201, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'literal'), Literal, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 202, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 145, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iri')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 200, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stem')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 201, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'literal')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 202, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_9()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iri'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 200, 12)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stem'), IRIstem, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 201, 12)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'literal'), Literal, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 202, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 150, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iri')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 200, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stem')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 201, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'literal')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 202, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_10()




SubjectSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'inclusion'), CTD_ANON_4, scope=SubjectSpecification, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 164, 12)))

SubjectSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'exclusion'), CTD_ANON_5, scope=SubjectSpecification, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 169, 12)))

SubjectSpecification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shape'), pyxb.binding.datatypes.IDREF, scope=SubjectSpecification, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 174, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubjectSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'inclusion')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 164, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubjectSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'exclusion')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 169, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubjectSpecification._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shape')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 174, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SubjectSpecification._Automaton = _BuildAutomaton_11()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iri'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stem'), IRIstem, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 166, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iri')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stem')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_12()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iri'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stem'), IRIstem, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 171, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iri')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 193, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stem')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 194, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_13()




Literal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lexicalValue'), pyxb.binding.datatypes.string, scope=Literal, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 181, 12)))

Literal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dataType'), pyxb.binding.datatypes.anyURI, scope=Literal, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 182, 12)))

Literal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'langTag'), pyxb.binding.datatypes.string, scope=Literal, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 183, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Literal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lexicalValue')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 181, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Literal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dataType')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 182, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Literal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'langTag')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 183, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Literal._Automaton = _BuildAutomaton_14()




EvalContext_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'schema'), Schema_, scope=EvalContext_, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 209, 12)))

EvalContext_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'graph'), pyxb.binding.datatypes.anyType, scope=EvalContext_, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 210, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EvalContext_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'schema')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 209, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EvalContext_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'graph')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 210, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EvalContext_._Automaton = _BuildAutomaton_15()




ArcRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'p'), PredicateFilter, scope=ArcRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 81, 12)))

ArcRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'o'), ObjectSpecification, scope=ArcRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 82, 12)))

ArcRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'action'), pyxb.binding.datatypes.anyType, scope=ArcRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 83, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 83, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ArcRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'p')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 81, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ArcRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'o')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 82, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ArcRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'action')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 83, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ArcRule._Automaton = _BuildAutomaton_16()




RevArcRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'p'), PredicateFilter, scope=RevArcRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 95, 12)))

RevArcRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'o'), SubjectSpecification, scope=RevArcRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 96, 12)))

RevArcRule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'actions'), pyxb.binding.datatypes.anyType, scope=RevArcRule, location=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 97, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 97, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RevArcRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'p')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 95, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RevArcRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'o')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 96, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RevArcRule._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'actions')), pyxb.utils.utility.Location('/Users/mrf7578/git/ShEx/ShEx/static/xsd/ShEx.xsd', 97, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RevArcRule._Automaton = _BuildAutomaton_17()

