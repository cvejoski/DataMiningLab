# ./actions.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-12-30 14:18:49.579627 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6452519c-9026-11e4-a0c9-002710dca3dc')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
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
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Copyright (c) 2003 - 2011 proFILE Computersysteme GmbH.
				All Rights Reserved.
				proFILE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE SUITABILITY OF
				THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
				IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE,
				OR NON-INFRINGEMENT. proFILE SHALL NOT BE LIABLE FOR ANY DAMAGES SUFFERED
				BY LICENSEE AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE
				OR ITS DERIVATIVES."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 13, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sports-metadata uses Python identifier sports_metadata
    __sports_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-metadata'), 'sports_metadata', '__AbsentNamespace0_CTD_ANON_sports_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 15, 4), )

    
    sports_metadata = property(__sports_metadata.value, __sports_metadata.set, None, None)

    
    # Element tournament uses Python identifier tournament
    __tournament = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tournament'), 'tournament', '__AbsentNamespace0_CTD_ANON_tournament', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 43, 4), )

    
    tournament = property(__tournament.value, __tournament.set, None, None)

    _ElementMap.update({
        __sports_metadata.name() : __sports_metadata,
        __tournament.name() : __tournament
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
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 16, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sports-title uses Python identifier sports_title
    __sports_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-title'), 'sports_title', '__AbsentNamespace0_CTD_ANON__sports_title', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 18, 7), )

    
    sports_title = property(__sports_title.value, __sports_title.set, None, None)

    
    # Element sports-content-codes uses Python identifier sports_content_codes
    __sports_content_codes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-content-codes'), 'sports_content_codes', '__AbsentNamespace0_CTD_ANON__sports_content_codes', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 19, 7), )

    
    sports_content_codes = property(__sports_content_codes.value, __sports_content_codes.set, None, None)

    
    # Attribute date-time uses Python identifier date_time
    __date_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-time'), 'date_time', '__AbsentNamespace0_CTD_ANON__date_time', pyxb.binding.datatypes.string)
    __date_time._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 38, 6)
    __date_time._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 38, 6)
    
    date_time = property(__date_time.value, __date_time.set, None, None)

    
    # Attribute doc-id uses Python identifier doc_id
    __doc_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'doc-id'), 'doc_id', '__AbsentNamespace0_CTD_ANON__doc_id', pyxb.binding.datatypes.string)
    __doc_id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 39, 6)
    __doc_id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 39, 6)
    
    doc_id = property(__doc_id.value, __doc_id.set, None, None)

    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'language'), 'language', '__AbsentNamespace0_CTD_ANON__language', pyxb.binding.datatypes.string)
    __language._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 40, 6)
    __language._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 40, 6)
    
    language = property(__language.value, __language.set, None, None)

    _ElementMap.update({
        __sports_title.name() : __sports_title,
        __sports_content_codes.name() : __sports_content_codes
    })
    _AttributeMap.update({
        __date_time.name() : __date_time,
        __doc_id.name() : __doc_id,
        __language.name() : __language
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 20, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sports-content-code uses Python identifier sports_content_code
    __sports_content_code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-content-code'), 'sports_content_code', '__AbsentNamespace0_CTD_ANON_2_sports_content_code', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 22, 10), )

    
    sports_content_code = property(__sports_content_code.value, __sports_content_code.set, None, None)

    _ElementMap.update({
        __sports_content_code.name() : __sports_content_code
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 23, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute code-type uses Python identifier code_type
    __code_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code-type'), 'code_type', '__AbsentNamespace0_CTD_ANON_3_code_type', pyxb.binding.datatypes.string)
    __code_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 26, 14)
    __code_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 26, 14)
    
    code_type = property(__code_type.value, __code_type.set, None, None)

    
    # Attribute code-key uses Python identifier code_key
    __code_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code-key'), 'code_key', '__AbsentNamespace0_CTD_ANON_3_code_key', pyxb.binding.datatypes.string)
    __code_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 27, 14)
    __code_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 27, 14)
    
    code_key = property(__code_key.value, __code_key.set, None, None)

    
    # Attribute code-source uses Python identifier code_source
    __code_source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code-source'), 'code_source', '__AbsentNamespace0_CTD_ANON_3_code_source', pyxb.binding.datatypes.string)
    __code_source._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 28, 14)
    __code_source._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 28, 14)
    
    code_source = property(__code_source.value, __code_source.set, None, None)

    
    # Attribute code-name uses Python identifier code_name
    __code_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code-name'), 'code_name', '__AbsentNamespace0_CTD_ANON_3_code_name', pyxb.binding.datatypes.string)
    __code_name._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 29, 14)
    __code_name._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 29, 14)
    
    code_name = property(__code_name.value, __code_name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code_type.name() : __code_type,
        __code_key.name() : __code_key,
        __code_source.name() : __code_source,
        __code_name.name() : __code_name
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 44, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element tournament-metadata uses Python identifier tournament_metadata
    __tournament_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tournament-metadata'), 'tournament_metadata', '__AbsentNamespace0_CTD_ANON_4_tournament_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 46, 7), )

    
    tournament_metadata = property(__tournament_metadata.value, __tournament_metadata.set, None, None)

    
    # Element tournament-division uses Python identifier tournament_division
    __tournament_division = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tournament-division'), 'tournament_division', '__AbsentNamespace0_CTD_ANON_4_tournament_division', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 59, 7), )

    
    tournament_division = property(__tournament_division.value, __tournament_division.set, None, None)

    _ElementMap.update({
        __tournament_metadata.name() : __tournament_metadata,
        __tournament_division.name() : __tournament_division
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 47, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute tournament-name uses Python identifier tournament_name
    __tournament_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tournament-name'), 'tournament_name', '__AbsentNamespace0_CTD_ANON_5_tournament_name', pyxb.binding.datatypes.string)
    __tournament_name._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 50, 11)
    __tournament_name._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 50, 11)
    
    tournament_name = property(__tournament_name.value, __tournament_name.set, None, None)

    
    # Attribute tournament-key uses Python identifier tournament_key
    __tournament_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tournament-key'), 'tournament_key', '__AbsentNamespace0_CTD_ANON_5_tournament_key', pyxb.binding.datatypes.byte)
    __tournament_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 51, 11)
    __tournament_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 51, 11)
    
    tournament_key = property(__tournament_key.value, __tournament_key.set, None, None)

    
    # Attribute tournament-source uses Python identifier tournament_source
    __tournament_source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tournament-source'), 'tournament_source', '__AbsentNamespace0_CTD_ANON_5_tournament_source', pyxb.binding.datatypes.string)
    __tournament_source._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 52, 11)
    __tournament_source._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 52, 11)
    
    tournament_source = property(__tournament_source.value, __tournament_source.set, None, None)

    
    # Attribute date-coverage-type uses Python identifier date_coverage_type
    __date_coverage_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-coverage-type'), 'date_coverage_type', '__AbsentNamespace0_CTD_ANON_5_date_coverage_type', pyxb.binding.datatypes.string)
    __date_coverage_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 53, 11)
    __date_coverage_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 53, 11)
    
    date_coverage_type = property(__date_coverage_type.value, __date_coverage_type.set, None, None)

    
    # Attribute date-coverage-value uses Python identifier date_coverage_value
    __date_coverage_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-coverage-value'), 'date_coverage_value', '__AbsentNamespace0_CTD_ANON_5_date_coverage_value', pyxb.binding.datatypes.string)
    __date_coverage_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 54, 11)
    __date_coverage_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 54, 11)
    
    date_coverage_value = property(__date_coverage_value.value, __date_coverage_value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tournament_name.name() : __tournament_name,
        __tournament_key.name() : __tournament_key,
        __tournament_source.name() : __tournament_source,
        __date_coverage_type.name() : __date_coverage_type,
        __date_coverage_value.name() : __date_coverage_value
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 60, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element tournament-division-metadata uses Python identifier tournament_division_metadata
    __tournament_division_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tournament-division-metadata'), 'tournament_division_metadata', '__AbsentNamespace0_CTD_ANON_6_tournament_division_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 62, 10), )

    
    tournament_division_metadata = property(__tournament_division_metadata.value, __tournament_division_metadata.set, None, None)

    
    # Element tournament-round uses Python identifier tournament_round
    __tournament_round = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tournament-round'), 'tournament_round', '__AbsentNamespace0_CTD_ANON_6_tournament_round', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 73, 10), )

    
    tournament_round = property(__tournament_round.value, __tournament_round.set, None, None)

    _ElementMap.update({
        __tournament_division_metadata.name() : __tournament_division_metadata,
        __tournament_round.name() : __tournament_round
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 63, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute division-name uses Python identifier division_name
    __division_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'division-name'), 'division_name', '__AbsentNamespace0_CTD_ANON_7_division_name', pyxb.binding.datatypes.string)
    __division_name._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 66, 14)
    __division_name._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 66, 14)
    
    division_name = property(__division_name.value, __division_name.set, None, None)

    
    # Attribute division-key uses Python identifier division_key
    __division_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'division-key'), 'division_key', '__AbsentNamespace0_CTD_ANON_7_division_key', pyxb.binding.datatypes.byte)
    __division_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 67, 14)
    __division_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 67, 14)
    
    division_key = property(__division_key.value, __division_key.set, None, None)

    
    # Attribute division-source uses Python identifier division_source
    __division_source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'division-source'), 'division_source', '__AbsentNamespace0_CTD_ANON_7_division_source', pyxb.binding.datatypes.string)
    __division_source._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 68, 14)
    __division_source._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 68, 14)
    
    division_source = property(__division_source.value, __division_source.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __division_name.name() : __division_name,
        __division_key.name() : __division_key,
        __division_source.name() : __division_source
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 74, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sports-event uses Python identifier sports_event
    __sports_event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sports-event'), 'sports_event', '__AbsentNamespace0_CTD_ANON_8_sports_event', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 76, 13), )

    
    sports_event = property(__sports_event.value, __sports_event.set, None, None)

    
    # Attribute round-number uses Python identifier round_number
    __round_number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'round-number'), 'round_number', '__AbsentNamespace0_CTD_ANON_8_round_number', pyxb.binding.datatypes.byte)
    __round_number._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 442, 12)
    __round_number._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 442, 12)
    
    round_number = property(__round_number.value, __round_number.set, None, None)

    
    # Attribute round-name uses Python identifier round_name
    __round_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'round-name'), 'round_name', '__AbsentNamespace0_CTD_ANON_8_round_name', pyxb.binding.datatypes.string)
    __round_name._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 443, 12)
    __round_name._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 443, 12)
    
    round_name = property(__round_name.value, __round_name.set, None, None)

    
    # Attribute round-key uses Python identifier round_key
    __round_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'round-key'), 'round_key', '__AbsentNamespace0_CTD_ANON_8_round_key', pyxb.binding.datatypes.byte)
    __round_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 444, 12)
    __round_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 444, 12)
    
    round_key = property(__round_key.value, __round_key.set, None, None)

    
    # Attribute round-source uses Python identifier round_source
    __round_source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'round-source'), 'round_source', '__AbsentNamespace0_CTD_ANON_8_round_source', pyxb.binding.datatypes.string)
    __round_source._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 445, 12)
    __round_source._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 445, 12)
    
    round_source = property(__round_source.value, __round_source.set, None, None)

    _ElementMap.update({
        __sports_event.name() : __sports_event
    })
    _AttributeMap.update({
        __round_number.name() : __round_number,
        __round_name.name() : __round_name,
        __round_key.name() : __round_key,
        __round_source.name() : __round_source
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 77, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element event-metadata uses Python identifier event_metadata
    __event_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'event-metadata'), 'event_metadata', '__AbsentNamespace0_CTD_ANON_9_event_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 79, 16), )

    
    event_metadata = property(__event_metadata.value, __event_metadata.set, None, None)

    
    # Element team uses Python identifier team
    __team = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team'), 'team', '__AbsentNamespace0_CTD_ANON_9_team', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 116, 16), )

    
    team = property(__team.value, __team.set, None, None)

    
    # Element officials uses Python identifier officials
    __officials = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'officials'), 'officials', '__AbsentNamespace0_CTD_ANON_9_officials', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 216, 16), )

    
    officials = property(__officials.value, __officials.set, None, None)

    
    # Element event-actions uses Python identifier event_actions
    __event_actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'event-actions'), 'event_actions', '__AbsentNamespace0_CTD_ANON_9_event_actions', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 247, 16), )

    
    event_actions = property(__event_actions.value, __event_actions.set, None, None)

    _ElementMap.update({
        __event_metadata.name() : __event_metadata,
        __team.name() : __team,
        __officials.name() : __officials,
        __event_actions.name() : __event_actions
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 80, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element event-metadata-soccer uses Python identifier event_metadata_soccer
    __event_metadata_soccer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'event-metadata-soccer'), 'event_metadata_soccer', '__AbsentNamespace0_CTD_ANON_10_event_metadata_soccer', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 82, 19), )

    
    event_metadata_soccer = property(__event_metadata_soccer.value, __event_metadata_soccer.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_10_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 101, 18)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 101, 18)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute event-key uses Python identifier event_key
    __event_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'event-key'), 'event_key', '__AbsentNamespace0_CTD_ANON_10_event_key', pyxb.binding.datatypes.int)
    __event_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 102, 18)
    __event_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 102, 18)
    
    event_key = property(__event_key.value, __event_key.set, None, None)

    
    # Attribute event-status uses Python identifier event_status
    __event_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'event-status'), 'event_status', '__AbsentNamespace0_CTD_ANON_10_event_status', pyxb.binding.datatypes.string)
    __event_status._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 103, 18)
    __event_status._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 103, 18)
    
    event_status = property(__event_status.value, __event_status.set, None, None)

    
    # Attribute start-date-time uses Python identifier start_date_time
    __start_date_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-date-time'), 'start_date_time', '__AbsentNamespace0_CTD_ANON_10_start_date_time', pyxb.binding.datatypes.string)
    __start_date_time._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 104, 18)
    __start_date_time._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 104, 18)
    
    start_date_time = property(__start_date_time.value, __start_date_time.set, None, None)

    
    # Attribute start-weekday uses Python identifier start_weekday
    __start_weekday = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start-weekday'), 'start_weekday', '__AbsentNamespace0_CTD_ANON_10_start_weekday', pyxb.binding.datatypes.string)
    __start_weekday._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 105, 18)
    __start_weekday._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 105, 18)
    
    start_weekday = property(__start_weekday.value, __start_weekday.set, None, None)

    
    # Attribute heat-number uses Python identifier heat_number
    __heat_number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'heat-number'), 'heat_number', '__AbsentNamespace0_CTD_ANON_10_heat_number', pyxb.binding.datatypes.byte)
    __heat_number._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 106, 18)
    __heat_number._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 106, 18)
    
    heat_number = property(__heat_number.value, __heat_number.set, None, None)

    
    # Attribute date-coverage-type uses Python identifier date_coverage_type
    __date_coverage_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-coverage-type'), 'date_coverage_type', '__AbsentNamespace0_CTD_ANON_10_date_coverage_type', pyxb.binding.datatypes.string)
    __date_coverage_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 107, 18)
    __date_coverage_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 107, 18)
    
    date_coverage_type = property(__date_coverage_type.value, __date_coverage_type.set, None, None)

    
    # Attribute date-coverage-value uses Python identifier date_coverage_value
    __date_coverage_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date-coverage-value'), 'date_coverage_value', '__AbsentNamespace0_CTD_ANON_10_date_coverage_value', pyxb.binding.datatypes.string)
    __date_coverage_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 108, 18)
    __date_coverage_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 108, 18)
    
    date_coverage_value = property(__date_coverage_value.value, __date_coverage_value.set, None, None)

    
    # Attribute site-attendance uses Python identifier site_attendance
    __site_attendance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'site-attendance'), 'site_attendance', '__AbsentNamespace0_CTD_ANON_10_site_attendance', pyxb.binding.datatypes.int)
    __site_attendance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 109, 18)
    __site_attendance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 109, 18)
    
    site_attendance = property(__site_attendance.value, __site_attendance.set, None, None)

    
    # Attribute live-period uses Python identifier live_period
    __live_period = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'live-period'), 'live_period', '__AbsentNamespace0_CTD_ANON_10_live_period', pyxb.binding.datatypes.byte)
    __live_period._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 110, 18)
    __live_period._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 110, 18)
    
    live_period = property(__live_period.value, __live_period.set, None, None)

    
    # Attribute has-overtime uses Python identifier has_overtime
    __has_overtime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'has-overtime'), 'has_overtime', '__AbsentNamespace0_CTD_ANON_10_has_overtime', pyxb.binding.datatypes.byte)
    __has_overtime._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 111, 18)
    __has_overtime._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 111, 18)
    
    has_overtime = property(__has_overtime.value, __has_overtime.set, None, None)

    
    # Attribute has-overtime2 uses Python identifier has_overtime2
    __has_overtime2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'has-overtime2'), 'has_overtime2', '__AbsentNamespace0_CTD_ANON_10_has_overtime2', pyxb.binding.datatypes.byte)
    __has_overtime2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 112, 18)
    __has_overtime2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 112, 18)
    
    has_overtime2 = property(__has_overtime2.value, __has_overtime2.set, None, None)

    
    # Attribute has-penalty-shootout uses Python identifier has_penalty_shootout
    __has_penalty_shootout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'has-penalty-shootout'), 'has_penalty_shootout', '__AbsentNamespace0_CTD_ANON_10_has_penalty_shootout', pyxb.binding.datatypes.byte)
    __has_penalty_shootout._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 113, 18)
    __has_penalty_shootout._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 113, 18)
    
    has_penalty_shootout = property(__has_penalty_shootout.value, __has_penalty_shootout.set, None, None)

    _ElementMap.update({
        __event_metadata_soccer.name() : __event_metadata_soccer
    })
    _AttributeMap.update({
        __id.name() : __id,
        __event_key.name() : __event_key,
        __event_status.name() : __event_status,
        __start_date_time.name() : __start_date_time,
        __start_weekday.name() : __start_weekday,
        __heat_number.name() : __heat_number,
        __date_coverage_type.name() : __date_coverage_type,
        __date_coverage_value.name() : __date_coverage_value,
        __site_attendance.name() : __site_attendance,
        __live_period.name() : __live_period,
        __has_overtime.name() : __has_overtime,
        __has_overtime2.name() : __has_overtime2,
        __has_penalty_shootout.name() : __has_penalty_shootout
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 83, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element time-adjustment uses Python identifier time_adjustment
    __time_adjustment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time-adjustment'), 'time_adjustment', '__AbsentNamespace0_CTD_ANON_11_time_adjustment', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 85, 22), )

    
    time_adjustment = property(__time_adjustment.value, __time_adjustment.set, None, None)

    
    # Attribute period-value uses Python identifier period_value
    __period_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-value'), 'period_value', '__AbsentNamespace0_CTD_ANON_11_period_value', pyxb.binding.datatypes.byte)
    __period_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 95, 21)
    __period_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 95, 21)
    
    period_value = property(__period_value.value, __period_value.set, None, None)

    
    # Attribute minutes-elapsed uses Python identifier minutes_elapsed
    __minutes_elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minutes-elapsed'), 'minutes_elapsed', '__AbsentNamespace0_CTD_ANON_11_minutes_elapsed', pyxb.binding.datatypes.byte)
    __minutes_elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 96, 21)
    __minutes_elapsed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 96, 21)
    
    minutes_elapsed = property(__minutes_elapsed.value, __minutes_elapsed.set, None, None)

    
    # Attribute period-minute-elapsed uses Python identifier period_minute_elapsed
    __period_minute_elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-minute-elapsed'), 'period_minute_elapsed', '__AbsentNamespace0_CTD_ANON_11_period_minute_elapsed', pyxb.binding.datatypes.byte)
    __period_minute_elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 97, 21)
    __period_minute_elapsed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 97, 21)
    
    period_minute_elapsed = property(__period_minute_elapsed.value, __period_minute_elapsed.set, None, None)

    _ElementMap.update({
        __time_adjustment.name() : __time_adjustment
    })
    _AttributeMap.update({
        __period_value.name() : __period_value,
        __minutes_elapsed.name() : __minutes_elapsed,
        __period_minute_elapsed.name() : __period_minute_elapsed
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 86, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute period-extra-time-elapsed uses Python identifier period_extra_time_elapsed
    __period_extra_time_elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-extra-time-elapsed'), 'period_extra_time_elapsed', '__AbsentNamespace0_CTD_ANON_12_period_extra_time_elapsed', pyxb.binding.datatypes.short)
    __period_extra_time_elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 89, 26)
    __period_extra_time_elapsed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 89, 26)
    
    period_extra_time_elapsed = property(__period_extra_time_elapsed.value, __period_extra_time_elapsed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __period_extra_time_elapsed.name() : __period_extra_time_elapsed
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 117, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element team-metadata uses Python identifier team_metadata
    __team_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team-metadata'), 'team_metadata', '__AbsentNamespace0_CTD_ANON_13_team_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 119, 19), )

    
    team_metadata = property(__team_metadata.value, __team_metadata.set, None, None)

    
    # Element team-stats uses Python identifier team_stats
    __team_stats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'team-stats'), 'team_stats', '__AbsentNamespace0_CTD_ANON_13_team_stats', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 140, 19), )

    
    team_stats = property(__team_stats.value, __team_stats.set, None, None)

    
    # Element player uses Python identifier player
    __player = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'player'), 'player', '__AbsentNamespace0_CTD_ANON_13_player', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 157, 19), )

    
    player = property(__player.value, __player.set, None, None)

    
    # Element associate uses Python identifier associate
    __associate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'associate'), 'associate', '__AbsentNamespace0_CTD_ANON_13_associate', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 188, 19), )

    
    associate = property(__associate.value, __associate.set, None, None)

    _ElementMap.update({
        __team_metadata.name() : __team_metadata,
        __team_stats.name() : __team_stats,
        __player.name() : __player,
        __associate.name() : __associate
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 120, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_14_name', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 122, 22), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_14_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 133, 21)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 133, 21)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute team-key uses Python identifier team_key
    __team_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'team-key'), 'team_key', '__AbsentNamespace0_CTD_ANON_14_team_key', pyxb.binding.datatypes.byte)
    __team_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 134, 21)
    __team_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 134, 21)
    
    team_key = property(__team_key.value, __team_key.set, None, None)

    
    # Attribute alignment uses Python identifier alignment
    __alignment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alignment'), 'alignment', '__AbsentNamespace0_CTD_ANON_14_alignment', pyxb.binding.datatypes.string)
    __alignment._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 135, 21)
    __alignment._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 135, 21)
    
    alignment = property(__alignment.value, __alignment.set, None, None)

    
    # Attribute uniform-color-name uses Python identifier uniform_color_name
    __uniform_color_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uniform-color-name'), 'uniform_color_name', '__AbsentNamespace0_CTD_ANON_14_uniform_color_name', pyxb.binding.datatypes.string)
    __uniform_color_name._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 136, 21)
    __uniform_color_name._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 136, 21)
    
    uniform_color_name = property(__uniform_color_name.value, __uniform_color_name.set, None, None)

    
    # Attribute uniform-color-hex uses Python identifier uniform_color_hex
    __uniform_color_hex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uniform-color-hex'), 'uniform_color_hex', '__AbsentNamespace0_CTD_ANON_14_uniform_color_hex', pyxb.binding.datatypes.string)
    __uniform_color_hex._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 137, 21)
    __uniform_color_hex._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 137, 21)
    
    uniform_color_hex = property(__uniform_color_hex.value, __uniform_color_hex.set, None, None)

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __id.name() : __id,
        __team_key.name() : __team_key,
        __alignment.name() : __alignment,
        __uniform_color_name.name() : __uniform_color_name,
        __uniform_color_hex.name() : __uniform_color_hex
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 123, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__AbsentNamespace0_CTD_ANON_15_full', pyxb.binding.datatypes.string)
    __full._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 126, 26)
    __full._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 126, 26)
    
    full = property(__full.value, __full.set, None, None)

    
    # Attribute nickname uses Python identifier nickname
    __nickname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nickname'), 'nickname', '__AbsentNamespace0_CTD_ANON_15_nickname', pyxb.binding.datatypes.string)
    __nickname._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 127, 26)
    __nickname._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 127, 26)
    
    nickname = property(__nickname.value, __nickname.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __full.name() : __full,
        __nickname.name() : __nickname
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 141, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sub-score uses Python identifier sub_score
    __sub_score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sub-score'), 'sub_score', '__AbsentNamespace0_CTD_ANON_16_sub_score', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 143, 22), )

    
    sub_score = property(__sub_score.value, __sub_score.set, None, None)

    
    # Attribute score uses Python identifier score
    __score = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score'), 'score', '__AbsentNamespace0_CTD_ANON_16_score', pyxb.binding.datatypes.byte)
    __score._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 154, 21)
    __score._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 154, 21)
    
    score = property(__score.value, __score.set, None, None)

    _ElementMap.update({
        __sub_score.name() : __sub_score
    })
    _AttributeMap.update({
        __score.name() : __score
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 144, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute period-value uses Python identifier period_value
    __period_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-value'), 'period_value', '__AbsentNamespace0_CTD_ANON_17_period_value', pyxb.binding.datatypes.string)
    __period_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 147, 26)
    __period_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 147, 26)
    
    period_value = property(__period_value.value, __period_value.set, None, None)

    
    # Attribute score uses Python identifier score
    __score = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score'), 'score', '__AbsentNamespace0_CTD_ANON_17_score', pyxb.binding.datatypes.byte)
    __score._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 148, 26)
    __score._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 148, 26)
    
    score = property(__score.value, __score.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __period_value.name() : __period_value,
        __score.name() : __score
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 158, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element player-metadata uses Python identifier player_metadata
    __player_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'player-metadata'), 'player_metadata', '__AbsentNamespace0_CTD_ANON_18_player_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 160, 22), )

    
    player_metadata = property(__player_metadata.value, __player_metadata.set, None, None)

    _ElementMap.update({
        __player_metadata.name() : __player_metadata
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 161, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_19_name', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 163, 25), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_19_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 175, 24)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 175, 24)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute player-key uses Python identifier player_key
    __player_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-key'), 'player_key', '__AbsentNamespace0_CTD_ANON_19_player_key', pyxb.binding.datatypes.int)
    __player_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 176, 24)
    __player_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 176, 24)
    
    player_key = property(__player_key.value, __player_key.set, None, None)

    
    # Attribute position-regular uses Python identifier position_regular
    __position_regular = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position-regular'), 'position_regular', '__AbsentNamespace0_CTD_ANON_19_position_regular', pyxb.binding.datatypes.string)
    __position_regular._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 177, 24)
    __position_regular._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 177, 24)
    
    position_regular = property(__position_regular.value, __position_regular.set, None, None)

    
    # Attribute position-event uses Python identifier position_event
    __position_event = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position-event'), 'position_event', '__AbsentNamespace0_CTD_ANON_19_position_event', pyxb.binding.datatypes.string)
    __position_event._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 178, 24)
    __position_event._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 178, 24)
    
    position_event = property(__position_event.value, __position_event.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__AbsentNamespace0_CTD_ANON_19_status', pyxb.binding.datatypes.string)
    __status._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 179, 24)
    __status._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 179, 24)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute uniform-number uses Python identifier uniform_number
    __uniform_number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uniform-number'), 'uniform_number', '__AbsentNamespace0_CTD_ANON_19_uniform_number', pyxb.binding.datatypes.byte)
    __uniform_number._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 180, 24)
    __uniform_number._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 180, 24)
    
    uniform_number = property(__uniform_number.value, __uniform_number.set, None, None)

    
    # Attribute vis-x uses Python identifier vis_x
    __vis_x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vis-x'), 'vis_x', '__AbsentNamespace0_CTD_ANON_19_vis_x', pyxb.binding.datatypes.float)
    __vis_x._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 181, 24)
    __vis_x._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 181, 24)
    
    vis_x = property(__vis_x.value, __vis_x.set, None, None)

    
    # Attribute vis-y uses Python identifier vis_y
    __vis_y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vis-y'), 'vis_y', '__AbsentNamespace0_CTD_ANON_19_vis_y', pyxb.binding.datatypes.float)
    __vis_y._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 182, 24)
    __vis_y._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 182, 24)
    
    vis_y = property(__vis_y.value, __vis_y.set, None, None)

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __id.name() : __id,
        __player_key.name() : __player_key,
        __position_regular.name() : __position_regular,
        __position_event.name() : __position_event,
        __status.name() : __status,
        __uniform_number.name() : __uniform_number,
        __vis_x.name() : __vis_x,
        __vis_y.name() : __vis_y
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 164, 26)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__AbsentNamespace0_CTD_ANON_20_full', pyxb.binding.datatypes.string)
    __full._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 167, 29)
    __full._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 167, 29)
    
    full = property(__full.value, __full.set, None, None)

    
    # Attribute nickname uses Python identifier nickname
    __nickname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nickname'), 'nickname', '__AbsentNamespace0_CTD_ANON_20_nickname', pyxb.binding.datatypes.string)
    __nickname._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 168, 29)
    __nickname._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 168, 29)
    
    nickname = property(__nickname.value, __nickname.set, None, None)

    
    # Attribute last uses Python identifier last
    __last = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'last'), 'last', '__AbsentNamespace0_CTD_ANON_20_last', pyxb.binding.datatypes.string)
    __last._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 169, 29)
    __last._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 169, 29)
    
    last = property(__last.value, __last.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __full.name() : __full,
        __nickname.name() : __nickname,
        __last.name() : __last
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 189, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element associate-metadata uses Python identifier associate_metadata
    __associate_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'associate-metadata'), 'associate_metadata', '__AbsentNamespace0_CTD_ANON_21_associate_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 191, 22), )

    
    associate_metadata = property(__associate_metadata.value, __associate_metadata.set, None, None)

    _ElementMap.update({
        __associate_metadata.name() : __associate_metadata
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 192, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_22_name', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 194, 25), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_22_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 205, 24)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 205, 24)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute associate-metadata-key uses Python identifier associate_metadata_key
    __associate_metadata_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'associate-metadata-key'), 'associate_metadata_key', '__AbsentNamespace0_CTD_ANON_22_associate_metadata_key', pyxb.binding.datatypes.short)
    __associate_metadata_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 206, 24)
    __associate_metadata_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 206, 24)
    
    associate_metadata_key = property(__associate_metadata_key.value, __associate_metadata_key.set, None, None)

    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__AbsentNamespace0_CTD_ANON_22_position', pyxb.binding.datatypes.string)
    __position._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 207, 24)
    __position._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 207, 24)
    
    position = property(__position.value, __position.set, None, None)

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __id.name() : __id,
        __associate_metadata_key.name() : __associate_metadata_key,
        __position.name() : __position
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 195, 26)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__AbsentNamespace0_CTD_ANON_23_full', pyxb.binding.datatypes.string)
    __full._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 198, 29)
    __full._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 198, 29)
    
    full = property(__full.value, __full.set, None, None)

    
    # Attribute nickname uses Python identifier nickname
    __nickname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nickname'), 'nickname', '__AbsentNamespace0_CTD_ANON_23_nickname', pyxb.binding.datatypes.string)
    __nickname._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 199, 29)
    __nickname._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 199, 29)
    
    nickname = property(__nickname.value, __nickname.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __full.name() : __full,
        __nickname.name() : __nickname
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 217, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element official uses Python identifier official
    __official = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'official'), 'official', '__AbsentNamespace0_CTD_ANON_24_official', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 219, 19), )

    
    official = property(__official.value, __official.set, None, None)

    _ElementMap.update({
        __official.name() : __official
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 220, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element official-metadata uses Python identifier official_metadata
    __official_metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'official-metadata'), 'official_metadata', '__AbsentNamespace0_CTD_ANON_25_official_metadata', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 222, 22), )

    
    official_metadata = property(__official_metadata.value, __official_metadata.set, None, None)

    _ElementMap.update({
        __official_metadata.name() : __official_metadata
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 223, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_26_name', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 225, 25), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute official-key uses Python identifier official_key
    __official_key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'official-key'), 'official_key', '__AbsentNamespace0_CTD_ANON_26_official_key', pyxb.binding.datatypes.string)
    __official_key._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 237, 24)
    __official_key._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 237, 24)
    
    official_key = property(__official_key.value, __official_key.set, None, None)

    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__AbsentNamespace0_CTD_ANON_26_position', pyxb.binding.datatypes.string)
    __position._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 238, 24)
    __position._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 238, 24)
    
    position = property(__position.value, __position.set, None, None)

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __official_key.name() : __official_key,
        __position.name() : __position
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 226, 26)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute full uses Python identifier full
    __full = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'full'), 'full', '__AbsentNamespace0_CTD_ANON_27_full', pyxb.binding.datatypes.string)
    __full._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 229, 29)
    __full._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 229, 29)
    
    full = property(__full.value, __full.set, None, None)

    
    # Attribute nickname uses Python identifier nickname
    __nickname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nickname'), 'nickname', '__AbsentNamespace0_CTD_ANON_27_nickname', pyxb.binding.datatypes.string)
    __nickname._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 230, 29)
    __nickname._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 230, 29)
    
    nickname = property(__nickname.value, __nickname.set, None, None)

    
    # Attribute city uses Python identifier city
    __city = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'city'), 'city', '__AbsentNamespace0_CTD_ANON_27_city', pyxb.binding.datatypes.string)
    __city._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 231, 29)
    __city._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 231, 29)
    
    city = property(__city.value, __city.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __full.name() : __full,
        __nickname.name() : __nickname,
        __city.name() : __city
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 248, 17)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element event-actions-soccer uses Python identifier event_actions_soccer
    __event_actions_soccer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'event-actions-soccer'), 'event_actions_soccer', '__AbsentNamespace0_CTD_ANON_28_event_actions_soccer', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 250, 19), )

    
    event_actions_soccer = property(__event_actions_soccer.value, __event_actions_soccer.set, None, None)

    _ElementMap.update({
        __event_actions_soccer.name() : __event_actions_soccer
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 251, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element action-soccer-other uses Python identifier action_soccer_other
    __action_soccer_other = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'action-soccer-other'), 'action_soccer_other', '__AbsentNamespace0_CTD_ANON_29_action_soccer_other', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 253, 22), )

    
    action_soccer_other = property(__action_soccer_other.value, __action_soccer_other.set, None, None)

    
    # Element action-soccer-score-attempt uses Python identifier action_soccer_score_attempt
    __action_soccer_score_attempt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'action-soccer-score-attempt'), 'action_soccer_score_attempt', '__AbsentNamespace0_CTD_ANON_29_action_soccer_score_attempt', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 302, 22), )

    
    action_soccer_score_attempt = property(__action_soccer_score_attempt.value, __action_soccer_score_attempt.set, None, None)

    
    # Element action-soccer-score uses Python identifier action_soccer_score
    __action_soccer_score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'action-soccer-score'), 'action_soccer_score', '__AbsentNamespace0_CTD_ANON_29_action_soccer_score', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 334, 22), )

    
    action_soccer_score = property(__action_soccer_score.value, __action_soccer_score.set, None, None)

    
    # Element action-soccer-foul uses Python identifier action_soccer_foul
    __action_soccer_foul = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'action-soccer-foul'), 'action_soccer_foul', '__AbsentNamespace0_CTD_ANON_29_action_soccer_foul', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 371, 22), )

    
    action_soccer_foul = property(__action_soccer_foul.value, __action_soccer_foul.set, None, None)

    
    # Element action-soccer-penalty uses Python identifier action_soccer_penalty
    __action_soccer_penalty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'action-soccer-penalty'), 'action_soccer_penalty', '__AbsentNamespace0_CTD_ANON_29_action_soccer_penalty', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 391, 22), )

    
    action_soccer_penalty = property(__action_soccer_penalty.value, __action_soccer_penalty.set, None, None)

    
    # Element action-soccer-offside uses Python identifier action_soccer_offside
    __action_soccer_offside = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'action-soccer-offside'), 'action_soccer_offside', '__AbsentNamespace0_CTD_ANON_29_action_soccer_offside', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 411, 22), )

    
    action_soccer_offside = property(__action_soccer_offside.value, __action_soccer_offside.set, None, None)

    _ElementMap.update({
        __action_soccer_other.name() : __action_soccer_other,
        __action_soccer_score_attempt.name() : __action_soccer_score_attempt,
        __action_soccer_score.name() : __action_soccer_score,
        __action_soccer_foul.name() : __action_soccer_foul,
        __action_soccer_penalty.name() : __action_soccer_penalty,
        __action_soccer_offside.name() : __action_soccer_offside
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 254, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element info uses Python identifier info
    __info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'info'), 'info', '__AbsentNamespace0_CTD_ANON_30_info', True, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 256, 25), )

    
    info = property(__info.value, __info.set, None, None)

    
    # Attribute action-type uses Python identifier action_type
    __action_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'action-type'), 'action_type', '__AbsentNamespace0_CTD_ANON_30_action_type', pyxb.binding.datatypes.string)
    __action_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 268, 24)
    __action_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 268, 24)
    
    action_type = property(__action_type.value, __action_type.set, None, None)

    
    # Attribute freekick-type uses Python identifier freekick_type
    __freekick_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'freekick-type'), 'freekick_type', '__AbsentNamespace0_CTD_ANON_30_freekick_type', pyxb.binding.datatypes.string)
    __freekick_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 269, 24)
    __freekick_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 269, 24)
    
    freekick_type = property(__freekick_type.value, __freekick_type.set, None, None)

    
    # Attribute freekick-result uses Python identifier freekick_result
    __freekick_result = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'freekick-result'), 'freekick_result', '__AbsentNamespace0_CTD_ANON_30_freekick_result', pyxb.binding.datatypes.string)
    __freekick_result._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 270, 24)
    __freekick_result._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 270, 24)
    
    freekick_result = property(__freekick_result.value, __freekick_result.set, None, None)

    
    # Attribute throwin-type uses Python identifier throwin_type
    __throwin_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'throwin-type'), 'throwin_type', '__AbsentNamespace0_CTD_ANON_30_throwin_type', pyxb.binding.datatypes.string)
    __throwin_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 271, 24)
    __throwin_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 271, 24)
    
    throwin_type = property(__throwin_type.value, __throwin_type.set, None, None)

    
    # Attribute pass-type uses Python identifier pass_type
    __pass_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pass-type'), 'pass_type', '__AbsentNamespace0_CTD_ANON_30_pass_type', pyxb.binding.datatypes.string)
    __pass_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 272, 24)
    __pass_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 272, 24)
    
    pass_type = property(__pass_type.value, __pass_type.set, None, None)

    
    # Attribute pass-result uses Python identifier pass_result
    __pass_result = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pass-result'), 'pass_result', '__AbsentNamespace0_CTD_ANON_30_pass_result', pyxb.binding.datatypes.string)
    __pass_result._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 273, 24)
    __pass_result._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 273, 24)
    
    pass_result = property(__pass_result.value, __pass_result.set, None, None)

    
    # Attribute throwin-result uses Python identifier throwin_result
    __throwin_result = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'throwin-result'), 'throwin_result', '__AbsentNamespace0_CTD_ANON_30_throwin_result', pyxb.binding.datatypes.string)
    __throwin_result._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 274, 24)
    __throwin_result._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 274, 24)
    
    throwin_result = property(__throwin_result.value, __throwin_result.set, None, None)

    
    # Attribute period-value uses Python identifier period_value
    __period_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-value'), 'period_value', '__AbsentNamespace0_CTD_ANON_30_period_value', pyxb.binding.datatypes.byte)
    __period_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 275, 24)
    __period_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 275, 24)
    
    period_value = property(__period_value.value, __period_value.set, None, None)

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__AbsentNamespace0_CTD_ANON_30_timestamp', pyxb.binding.datatypes.time)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 276, 24)
    __timestamp._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 276, 24)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_30_id', pyxb.binding.datatypes.short)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 277, 24)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 277, 24)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute action-side uses Python identifier action_side
    __action_side = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'action-side'), 'action_side', '__AbsentNamespace0_CTD_ANON_30_action_side', pyxb.binding.datatypes.string)
    __action_side._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 278, 24)
    __action_side._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 278, 24)
    
    action_side = property(__action_side.value, __action_side.set, None, None)

    
    # Attribute team-idref uses Python identifier team_idref
    __team_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'team-idref'), 'team_idref', '__AbsentNamespace0_CTD_ANON_30_team_idref', pyxb.binding.datatypes.string)
    __team_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 279, 24)
    __team_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 279, 24)
    
    team_idref = property(__team_idref.value, __team_idref.set, None, None)

    
    # Attribute player-idref uses Python identifier player_idref
    __player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-idref'), 'player_idref', '__AbsentNamespace0_CTD_ANON_30_player_idref', pyxb.binding.datatypes.string)
    __player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 280, 24)
    __player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 280, 24)
    
    player_idref = property(__player_idref.value, __player_idref.set, None, None)

    
    # Attribute second-player-idref uses Python identifier second_player_idref
    __second_player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'second-player-idref'), 'second_player_idref', '__AbsentNamespace0_CTD_ANON_30_second_player_idref', pyxb.binding.datatypes.string)
    __second_player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 281, 24)
    __second_player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 281, 24)
    
    second_player_idref = property(__second_player_idref.value, __second_player_idref.set, None, None)

    
    # Attribute corner-kick-result uses Python identifier corner_kick_result
    __corner_kick_result = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'corner-kick-result'), 'corner_kick_result', '__AbsentNamespace0_CTD_ANON_30_corner_kick_result', pyxb.binding.datatypes.string)
    __corner_kick_result._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 282, 24)
    __corner_kick_result._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 282, 24)
    
    corner_kick_result = property(__corner_kick_result.value, __corner_kick_result.set, None, None)

    
    # Attribute minutes-elapsed uses Python identifier minutes_elapsed
    __minutes_elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minutes-elapsed'), 'minutes_elapsed', '__AbsentNamespace0_CTD_ANON_30_minutes_elapsed', pyxb.binding.datatypes.byte)
    __minutes_elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 283, 24)
    __minutes_elapsed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 283, 24)
    
    minutes_elapsed = property(__minutes_elapsed.value, __minutes_elapsed.set, None, None)

    
    # Attribute x1 uses Python identifier x1
    __x1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x1'), 'x1', '__AbsentNamespace0_CTD_ANON_30_x1', pyxb.binding.datatypes.string)
    __x1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 284, 24)
    __x1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 284, 24)
    
    x1 = property(__x1.value, __x1.set, None, None)

    
    # Attribute y1 uses Python identifier y1
    __y1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y1'), 'y1', '__AbsentNamespace0_CTD_ANON_30_y1', pyxb.binding.datatypes.string)
    __y1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 285, 24)
    __y1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 285, 24)
    
    y1 = property(__y1.value, __y1.set, None, None)

    
    # Attribute x2 uses Python identifier x2
    __x2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x2'), 'x2', '__AbsentNamespace0_CTD_ANON_30_x2', pyxb.binding.datatypes.string)
    __x2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 286, 24)
    __x2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 286, 24)
    
    x2 = property(__x2.value, __x2.set, None, None)

    
    # Attribute y2 uses Python identifier y2
    __y2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y2'), 'y2', '__AbsentNamespace0_CTD_ANON_30_y2', pyxb.binding.datatypes.string)
    __y2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 287, 24)
    __y2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 287, 24)
    
    y2 = property(__y2.value, __y2.set, None, None)

    
    # Attribute first-player-idref uses Python identifier first_player_idref
    __first_player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'first-player-idref'), 'first_player_idref', '__AbsentNamespace0_CTD_ANON_30_first_player_idref', pyxb.binding.datatypes.string)
    __first_player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 288, 24)
    __first_player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 288, 24)
    
    first_player_idref = property(__first_player_idref.value, __first_player_idref.set, None, None)

    
    # Attribute first-team-idref uses Python identifier first_team_idref
    __first_team_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'first-team-idref'), 'first_team_idref', '__AbsentNamespace0_CTD_ANON_30_first_team_idref', pyxb.binding.datatypes.string)
    __first_team_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 289, 24)
    __first_team_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 289, 24)
    
    first_team_idref = property(__first_team_idref.value, __first_team_idref.set, None, None)

    
    # Attribute second-team-idref uses Python identifier second_team_idref
    __second_team_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'second-team-idref'), 'second_team_idref', '__AbsentNamespace0_CTD_ANON_30_second_team_idref', pyxb.binding.datatypes.string)
    __second_team_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 290, 24)
    __second_team_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 290, 24)
    
    second_team_idref = property(__second_team_idref.value, __second_team_idref.set, None, None)

    
    # Attribute tackle-type uses Python identifier tackle_type
    __tackle_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tackle-type'), 'tackle_type', '__AbsentNamespace0_CTD_ANON_30_tackle_type', pyxb.binding.datatypes.string)
    __tackle_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 291, 24)
    __tackle_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 291, 24)
    
    tackle_type = property(__tackle_type.value, __tackle_type.set, None, None)

    
    # Attribute tackle-description uses Python identifier tackle_description
    __tackle_description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tackle-description'), 'tackle_description', '__AbsentNamespace0_CTD_ANON_30_tackle_description', pyxb.binding.datatypes.string)
    __tackle_description._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 292, 24)
    __tackle_description._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 292, 24)
    
    tackle_description = property(__tackle_description.value, __tackle_description.set, None, None)

    
    # Attribute tackle-dribblings uses Python identifier tackle_dribblings
    __tackle_dribblings = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tackle-dribblings'), 'tackle_dribblings', '__AbsentNamespace0_CTD_ANON_30_tackle_dribblings', pyxb.binding.datatypes.string)
    __tackle_dribblings._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 293, 24)
    __tackle_dribblings._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 293, 24)
    
    tackle_dribblings = property(__tackle_dribblings.value, __tackle_dribblings.set, None, None)

    
    # Attribute tackle-result uses Python identifier tackle_result
    __tackle_result = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tackle-result'), 'tackle_result', '__AbsentNamespace0_CTD_ANON_30_tackle_result', pyxb.binding.datatypes.string)
    __tackle_result._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 294, 24)
    __tackle_result._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 294, 24)
    
    tackle_result = property(__tackle_result.value, __tackle_result.set, None, None)

    
    # Attribute cross-result uses Python identifier cross_result
    __cross_result = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cross-result'), 'cross_result', '__AbsentNamespace0_CTD_ANON_30_cross_result', pyxb.binding.datatypes.string)
    __cross_result._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 295, 24)
    __cross_result._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 295, 24)
    
    cross_result = property(__cross_result.value, __cross_result.set, None, None)

    
    # Attribute direction uses Python identifier direction
    __direction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'direction'), 'direction', '__AbsentNamespace0_CTD_ANON_30_direction', pyxb.binding.datatypes.string)
    __direction._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 296, 24)
    __direction._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 296, 24)
    
    direction = property(__direction.value, __direction.set, None, None)

    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__AbsentNamespace0_CTD_ANON_30_time', pyxb.binding.datatypes.double)
    __time._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 297, 24)
    __time._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 297, 24)
    
    time = property(__time.value, __time.set, None, None)

    
    # Attribute distance uses Python identifier distance
    __distance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'distance'), 'distance', '__AbsentNamespace0_CTD_ANON_30_distance', pyxb.binding.datatypes.double)
    __distance._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 298, 24)
    __distance._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 298, 24)
    
    distance = property(__distance.value, __distance.set, None, None)

    
    # Attribute max-speed uses Python identifier max_speed
    __max_speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max-speed'), 'max_speed', '__AbsentNamespace0_CTD_ANON_30_max_speed', pyxb.binding.datatypes.double)
    __max_speed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 299, 24)
    __max_speed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 299, 24)
    
    max_speed = property(__max_speed.value, __max_speed.set, None, None)

    _ElementMap.update({
        __info.name() : __info
    })
    _AttributeMap.update({
        __action_type.name() : __action_type,
        __freekick_type.name() : __freekick_type,
        __freekick_result.name() : __freekick_result,
        __throwin_type.name() : __throwin_type,
        __pass_type.name() : __pass_type,
        __pass_result.name() : __pass_result,
        __throwin_result.name() : __throwin_result,
        __period_value.name() : __period_value,
        __timestamp.name() : __timestamp,
        __id.name() : __id,
        __action_side.name() : __action_side,
        __team_idref.name() : __team_idref,
        __player_idref.name() : __player_idref,
        __second_player_idref.name() : __second_player_idref,
        __corner_kick_result.name() : __corner_kick_result,
        __minutes_elapsed.name() : __minutes_elapsed,
        __x1.name() : __x1,
        __y1.name() : __y1,
        __x2.name() : __x2,
        __y2.name() : __y2,
        __first_player_idref.name() : __first_player_idref,
        __first_team_idref.name() : __first_team_idref,
        __second_team_idref.name() : __second_team_idref,
        __tackle_type.name() : __tackle_type,
        __tackle_description.name() : __tackle_description,
        __tackle_dribblings.name() : __tackle_dribblings,
        __tackle_result.name() : __tackle_result,
        __cross_result.name() : __cross_result,
        __direction.name() : __direction,
        __time.name() : __time,
        __distance.name() : __distance,
        __max_speed.name() : __max_speed
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 257, 26)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute nr uses Python identifier nr
    __nr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nr'), 'nr', '__AbsentNamespace0_CTD_ANON_31_nr', pyxb.binding.datatypes.int)
    __nr._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 260, 29)
    __nr._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 260, 29)
    
    nr = property(__nr.value, __nr.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__AbsentNamespace0_CTD_ANON_31_x', pyxb.binding.datatypes.double)
    __x._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 261, 29)
    __x._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 261, 29)
    
    x = property(__x.value, __x.set, None, None)

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__AbsentNamespace0_CTD_ANON_31_y', pyxb.binding.datatypes.double)
    __y._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 262, 29)
    __y._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 262, 29)
    
    y = property(__y.value, __y.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __nr.name() : __nr,
        __x.name() : __x,
        __y.name() : __y
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 303, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element action-soccer-assisting-player uses Python identifier action_soccer_assisting_player
    __action_soccer_assisting_player = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'action-soccer-assisting-player'), 'action_soccer_assisting_player', '__AbsentNamespace0_CTD_ANON_32_action_soccer_assisting_player', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 305, 25), )

    
    action_soccer_assisting_player = property(__action_soccer_assisting_player.value, __action_soccer_assisting_player.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_32_id', pyxb.binding.datatypes.short)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 315, 24)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 315, 24)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute team-idref uses Python identifier team_idref
    __team_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'team-idref'), 'team_idref', '__AbsentNamespace0_CTD_ANON_32_team_idref', pyxb.binding.datatypes.string)
    __team_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 316, 24)
    __team_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 316, 24)
    
    team_idref = property(__team_idref.value, __team_idref.set, None, None)

    
    # Attribute player-idref uses Python identifier player_idref
    __player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-idref'), 'player_idref', '__AbsentNamespace0_CTD_ANON_32_player_idref', pyxb.binding.datatypes.string)
    __player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 317, 24)
    __player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 317, 24)
    
    player_idref = property(__player_idref.value, __player_idref.set, None, None)

    
    # Attribute second-player-idref uses Python identifier second_player_idref
    __second_player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'second-player-idref'), 'second_player_idref', '__AbsentNamespace0_CTD_ANON_32_second_player_idref', pyxb.binding.datatypes.string)
    __second_player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 318, 24)
    __second_player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 318, 24)
    
    second_player_idref = property(__second_player_idref.value, __second_player_idref.set, None, None)

    
    # Attribute score-attempt-method uses Python identifier score_attempt_method
    __score_attempt_method = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-method'), 'score_attempt_method', '__AbsentNamespace0_CTD_ANON_32_score_attempt_method', pyxb.binding.datatypes.string)
    __score_attempt_method._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 319, 24)
    __score_attempt_method._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 319, 24)
    
    score_attempt_method = property(__score_attempt_method.value, __score_attempt_method.set, None, None)

    
    # Attribute score-attempt-type uses Python identifier score_attempt_type
    __score_attempt_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-type'), 'score_attempt_type', '__AbsentNamespace0_CTD_ANON_32_score_attempt_type', pyxb.binding.datatypes.string)
    __score_attempt_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 320, 24)
    __score_attempt_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 320, 24)
    
    score_attempt_type = property(__score_attempt_type.value, __score_attempt_type.set, None, None)

    
    # Attribute score-attempt-result uses Python identifier score_attempt_result
    __score_attempt_result = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-result'), 'score_attempt_result', '__AbsentNamespace0_CTD_ANON_32_score_attempt_result', pyxb.binding.datatypes.string)
    __score_attempt_result._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 321, 24)
    __score_attempt_result._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 321, 24)
    
    score_attempt_result = property(__score_attempt_result.value, __score_attempt_result.set, None, None)

    
    # Attribute score-attempt-position uses Python identifier score_attempt_position
    __score_attempt_position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-position'), 'score_attempt_position', '__AbsentNamespace0_CTD_ANON_32_score_attempt_position', pyxb.binding.datatypes.string)
    __score_attempt_position._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 322, 24)
    __score_attempt_position._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 322, 24)
    
    score_attempt_position = property(__score_attempt_position.value, __score_attempt_position.set, None, None)

    
    # Attribute score-attempt-counterattack uses Python identifier score_attempt_counterattack
    __score_attempt_counterattack = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-counterattack'), 'score_attempt_counterattack', '__AbsentNamespace0_CTD_ANON_32_score_attempt_counterattack', pyxb.binding.datatypes.string)
    __score_attempt_counterattack._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 323, 24)
    __score_attempt_counterattack._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 323, 24)
    
    score_attempt_counterattack = property(__score_attempt_counterattack.value, __score_attempt_counterattack.set, None, None)

    
    # Attribute score-attempt-quality uses Python identifier score_attempt_quality
    __score_attempt_quality = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-quality'), 'score_attempt_quality', '__AbsentNamespace0_CTD_ANON_32_score_attempt_quality', pyxb.binding.datatypes.string)
    __score_attempt_quality._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 324, 24)
    __score_attempt_quality._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 324, 24)
    
    score_attempt_quality = property(__score_attempt_quality.value, __score_attempt_quality.set, None, None)

    
    # Attribute period-value uses Python identifier period_value
    __period_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-value'), 'period_value', '__AbsentNamespace0_CTD_ANON_32_period_value', pyxb.binding.datatypes.byte)
    __period_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 325, 24)
    __period_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 325, 24)
    
    period_value = property(__period_value.value, __period_value.set, None, None)

    
    # Attribute minutes-elapsed uses Python identifier minutes_elapsed
    __minutes_elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minutes-elapsed'), 'minutes_elapsed', '__AbsentNamespace0_CTD_ANON_32_minutes_elapsed', pyxb.binding.datatypes.byte)
    __minutes_elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 326, 24)
    __minutes_elapsed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 326, 24)
    
    minutes_elapsed = property(__minutes_elapsed.value, __minutes_elapsed.set, None, None)

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__AbsentNamespace0_CTD_ANON_32_timestamp', pyxb.binding.datatypes.time)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 327, 24)
    __timestamp._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 327, 24)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Attribute x1 uses Python identifier x1
    __x1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x1'), 'x1', '__AbsentNamespace0_CTD_ANON_32_x1', pyxb.binding.datatypes.float)
    __x1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 328, 24)
    __x1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 328, 24)
    
    x1 = property(__x1.value, __x1.set, None, None)

    
    # Attribute y1 uses Python identifier y1
    __y1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y1'), 'y1', '__AbsentNamespace0_CTD_ANON_32_y1', pyxb.binding.datatypes.float)
    __y1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 329, 24)
    __y1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 329, 24)
    
    y1 = property(__y1.value, __y1.set, None, None)

    
    # Attribute x2 uses Python identifier x2
    __x2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x2'), 'x2', '__AbsentNamespace0_CTD_ANON_32_x2', pyxb.binding.datatypes.string)
    __x2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 330, 24)
    __x2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 330, 24)
    
    x2 = property(__x2.value, __x2.set, None, None)

    
    # Attribute y2 uses Python identifier y2
    __y2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y2'), 'y2', '__AbsentNamespace0_CTD_ANON_32_y2', pyxb.binding.datatypes.string)
    __y2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 331, 24)
    __y2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 331, 24)
    
    y2 = property(__y2.value, __y2.set, None, None)

    _ElementMap.update({
        __action_soccer_assisting_player.name() : __action_soccer_assisting_player
    })
    _AttributeMap.update({
        __id.name() : __id,
        __team_idref.name() : __team_idref,
        __player_idref.name() : __player_idref,
        __second_player_idref.name() : __second_player_idref,
        __score_attempt_method.name() : __score_attempt_method,
        __score_attempt_type.name() : __score_attempt_type,
        __score_attempt_result.name() : __score_attempt_result,
        __score_attempt_position.name() : __score_attempt_position,
        __score_attempt_counterattack.name() : __score_attempt_counterattack,
        __score_attempt_quality.name() : __score_attempt_quality,
        __period_value.name() : __period_value,
        __minutes_elapsed.name() : __minutes_elapsed,
        __timestamp.name() : __timestamp,
        __x1.name() : __x1,
        __y1.name() : __y1,
        __x2.name() : __x2,
        __y2.name() : __y2
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 306, 26)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute player-idref uses Python identifier player_idref
    __player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-idref'), 'player_idref', '__AbsentNamespace0_CTD_ANON_33_player_idref', pyxb.binding.datatypes.string)
    __player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 309, 29)
    __player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 309, 29)
    
    player_idref = property(__player_idref.value, __player_idref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __player_idref.name() : __player_idref
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 335, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element action-soccer-assisting-player uses Python identifier action_soccer_assisting_player
    __action_soccer_assisting_player = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'action-soccer-assisting-player'), 'action_soccer_assisting_player', '__AbsentNamespace0_CTD_ANON_34_action_soccer_assisting_player', False, pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 337, 25), )

    
    action_soccer_assisting_player = property(__action_soccer_assisting_player.value, __action_soccer_assisting_player.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_34_id', pyxb.binding.datatypes.short)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 347, 24)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 347, 24)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute team-idref uses Python identifier team_idref
    __team_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'team-idref'), 'team_idref', '__AbsentNamespace0_CTD_ANON_34_team_idref', pyxb.binding.datatypes.string)
    __team_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 348, 24)
    __team_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 348, 24)
    
    team_idref = property(__team_idref.value, __team_idref.set, None, None)

    
    # Attribute player-idref uses Python identifier player_idref
    __player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-idref'), 'player_idref', '__AbsentNamespace0_CTD_ANON_34_player_idref', pyxb.binding.datatypes.string)
    __player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 349, 24)
    __player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 349, 24)
    
    player_idref = property(__player_idref.value, __player_idref.set, None, None)

    
    # Attribute score-team uses Python identifier score_team
    __score_team = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-team'), 'score_team', '__AbsentNamespace0_CTD_ANON_34_score_team', pyxb.binding.datatypes.string)
    __score_team._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 350, 24)
    __score_team._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 350, 24)
    
    score_team = property(__score_team.value, __score_team.set, None, None)

    
    # Attribute score-team-opposing uses Python identifier score_team_opposing
    __score_team_opposing = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-team-opposing'), 'score_team_opposing', '__AbsentNamespace0_CTD_ANON_34_score_team_opposing', pyxb.binding.datatypes.string)
    __score_team_opposing._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 351, 24)
    __score_team_opposing._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 351, 24)
    
    score_team_opposing = property(__score_team_opposing.value, __score_team_opposing.set, None, None)

    
    # Attribute score-attempt-method uses Python identifier score_attempt_method
    __score_attempt_method = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-method'), 'score_attempt_method', '__AbsentNamespace0_CTD_ANON_34_score_attempt_method', pyxb.binding.datatypes.string)
    __score_attempt_method._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 352, 24)
    __score_attempt_method._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 352, 24)
    
    score_attempt_method = property(__score_attempt_method.value, __score_attempt_method.set, None, None)

    
    # Attribute score-attempt-type uses Python identifier score_attempt_type
    __score_attempt_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-type'), 'score_attempt_type', '__AbsentNamespace0_CTD_ANON_34_score_attempt_type', pyxb.binding.datatypes.string)
    __score_attempt_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 353, 24)
    __score_attempt_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 353, 24)
    
    score_attempt_type = property(__score_attempt_type.value, __score_attempt_type.set, None, None)

    
    # Attribute score-type uses Python identifier score_type
    __score_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-type'), 'score_type', '__AbsentNamespace0_CTD_ANON_34_score_type', pyxb.binding.datatypes.string)
    __score_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 354, 24)
    __score_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 354, 24)
    
    score_type = property(__score_type.value, __score_type.set, None, None)

    
    # Attribute score-attempt-position uses Python identifier score_attempt_position
    __score_attempt_position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-position'), 'score_attempt_position', '__AbsentNamespace0_CTD_ANON_34_score_attempt_position', pyxb.binding.datatypes.string)
    __score_attempt_position._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 355, 24)
    __score_attempt_position._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 355, 24)
    
    score_attempt_position = property(__score_attempt_position.value, __score_attempt_position.set, None, None)

    
    # Attribute score-attempt-counterattack uses Python identifier score_attempt_counterattack
    __score_attempt_counterattack = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-counterattack'), 'score_attempt_counterattack', '__AbsentNamespace0_CTD_ANON_34_score_attempt_counterattack', pyxb.binding.datatypes.string)
    __score_attempt_counterattack._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 356, 24)
    __score_attempt_counterattack._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 356, 24)
    
    score_attempt_counterattack = property(__score_attempt_counterattack.value, __score_attempt_counterattack.set, None, None)

    
    # Attribute score-attempt-quality uses Python identifier score_attempt_quality
    __score_attempt_quality = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score-attempt-quality'), 'score_attempt_quality', '__AbsentNamespace0_CTD_ANON_34_score_attempt_quality', pyxb.binding.datatypes.string)
    __score_attempt_quality._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 357, 24)
    __score_attempt_quality._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 357, 24)
    
    score_attempt_quality = property(__score_attempt_quality.value, __score_attempt_quality.set, None, None)

    
    # Attribute period-value uses Python identifier period_value
    __period_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-value'), 'period_value', '__AbsentNamespace0_CTD_ANON_34_period_value', pyxb.binding.datatypes.byte)
    __period_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 358, 24)
    __period_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 358, 24)
    
    period_value = property(__period_value.value, __period_value.set, None, None)

    
    # Attribute minutes-elapsed uses Python identifier minutes_elapsed
    __minutes_elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minutes-elapsed'), 'minutes_elapsed', '__AbsentNamespace0_CTD_ANON_34_minutes_elapsed', pyxb.binding.datatypes.byte)
    __minutes_elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 359, 24)
    __minutes_elapsed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 359, 24)
    
    minutes_elapsed = property(__minutes_elapsed.value, __minutes_elapsed.set, None, None)

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__AbsentNamespace0_CTD_ANON_34_timestamp', pyxb.binding.datatypes.time)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 360, 24)
    __timestamp._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 360, 24)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Attribute x1 uses Python identifier x1
    __x1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x1'), 'x1', '__AbsentNamespace0_CTD_ANON_34_x1', pyxb.binding.datatypes.float)
    __x1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 361, 24)
    __x1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 361, 24)
    
    x1 = property(__x1.value, __x1.set, None, None)

    
    # Attribute y1 uses Python identifier y1
    __y1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y1'), 'y1', '__AbsentNamespace0_CTD_ANON_34_y1', pyxb.binding.datatypes.float)
    __y1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 362, 24)
    __y1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 362, 24)
    
    y1 = property(__y1.value, __y1.set, None, None)

    
    # Attribute x2 uses Python identifier x2
    __x2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x2'), 'x2', '__AbsentNamespace0_CTD_ANON_34_x2', pyxb.binding.datatypes.float)
    __x2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 363, 24)
    __x2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 363, 24)
    
    x2 = property(__x2.value, __x2.set, None, None)

    
    # Attribute y2 uses Python identifier y2
    __y2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y2'), 'y2', '__AbsentNamespace0_CTD_ANON_34_y2', pyxb.binding.datatypes.float)
    __y2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 364, 24)
    __y2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 364, 24)
    
    y2 = property(__y2.value, __y2.set, None, None)

    
    # Attribute action-type uses Python identifier action_type
    __action_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'action-type'), 'action_type', '__AbsentNamespace0_CTD_ANON_34_action_type', pyxb.binding.datatypes.string)
    __action_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 365, 24)
    __action_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 365, 24)
    
    action_type = property(__action_type.value, __action_type.set, None, None)

    
    # Attribute freekick-type uses Python identifier freekick_type
    __freekick_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'freekick-type'), 'freekick_type', '__AbsentNamespace0_CTD_ANON_34_freekick_type', pyxb.binding.datatypes.string)
    __freekick_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 366, 24)
    __freekick_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 366, 24)
    
    freekick_type = property(__freekick_type.value, __freekick_type.set, None, None)

    
    # Attribute second-player-idref uses Python identifier second_player_idref
    __second_player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'second-player-idref'), 'second_player_idref', '__AbsentNamespace0_CTD_ANON_34_second_player_idref', pyxb.binding.datatypes.string)
    __second_player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 367, 24)
    __second_player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 367, 24)
    
    second_player_idref = property(__second_player_idref.value, __second_player_idref.set, None, None)

    
    # Attribute freekick-result uses Python identifier freekick_result
    __freekick_result = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'freekick-result'), 'freekick_result', '__AbsentNamespace0_CTD_ANON_34_freekick_result', pyxb.binding.datatypes.string)
    __freekick_result._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 368, 24)
    __freekick_result._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 368, 24)
    
    freekick_result = property(__freekick_result.value, __freekick_result.set, None, None)

    _ElementMap.update({
        __action_soccer_assisting_player.name() : __action_soccer_assisting_player
    })
    _AttributeMap.update({
        __id.name() : __id,
        __team_idref.name() : __team_idref,
        __player_idref.name() : __player_idref,
        __score_team.name() : __score_team,
        __score_team_opposing.name() : __score_team_opposing,
        __score_attempt_method.name() : __score_attempt_method,
        __score_attempt_type.name() : __score_attempt_type,
        __score_type.name() : __score_type,
        __score_attempt_position.name() : __score_attempt_position,
        __score_attempt_counterattack.name() : __score_attempt_counterattack,
        __score_attempt_quality.name() : __score_attempt_quality,
        __period_value.name() : __period_value,
        __minutes_elapsed.name() : __minutes_elapsed,
        __timestamp.name() : __timestamp,
        __x1.name() : __x1,
        __y1.name() : __y1,
        __x2.name() : __x2,
        __y2.name() : __y2,
        __action_type.name() : __action_type,
        __freekick_type.name() : __freekick_type,
        __second_player_idref.name() : __second_player_idref,
        __freekick_result.name() : __freekick_result
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 338, 26)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute player-idref uses Python identifier player_idref
    __player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-idref'), 'player_idref', '__AbsentNamespace0_CTD_ANON_35_player_idref', pyxb.binding.datatypes.string)
    __player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 341, 29)
    __player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 341, 29)
    
    player_idref = property(__player_idref.value, __player_idref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __player_idref.name() : __player_idref
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 372, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute fouled-team-idref uses Python identifier fouled_team_idref
    __fouled_team_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fouled-team-idref'), 'fouled_team_idref', '__AbsentNamespace0_CTD_ANON_36_fouled_team_idref', pyxb.binding.datatypes.string)
    __fouled_team_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 375, 26)
    __fouled_team_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 375, 26)
    
    fouled_team_idref = property(__fouled_team_idref.value, __fouled_team_idref.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_36_id', pyxb.binding.datatypes.short)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 376, 26)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 376, 26)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute fouled-player-idref uses Python identifier fouled_player_idref
    __fouled_player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fouled-player-idref'), 'fouled_player_idref', '__AbsentNamespace0_CTD_ANON_36_fouled_player_idref', pyxb.binding.datatypes.string)
    __fouled_player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 377, 26)
    __fouled_player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 377, 26)
    
    fouled_player_idref = property(__fouled_player_idref.value, __fouled_player_idref.set, None, None)

    
    # Attribute fouling-team-idref uses Python identifier fouling_team_idref
    __fouling_team_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fouling-team-idref'), 'fouling_team_idref', '__AbsentNamespace0_CTD_ANON_36_fouling_team_idref', pyxb.binding.datatypes.string)
    __fouling_team_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 378, 26)
    __fouling_team_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 378, 26)
    
    fouling_team_idref = property(__fouling_team_idref.value, __fouling_team_idref.set, None, None)

    
    # Attribute fouling-player-idref uses Python identifier fouling_player_idref
    __fouling_player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fouling-player-idref'), 'fouling_player_idref', '__AbsentNamespace0_CTD_ANON_36_fouling_player_idref', pyxb.binding.datatypes.string)
    __fouling_player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 379, 26)
    __fouling_player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 379, 26)
    
    fouling_player_idref = property(__fouling_player_idref.value, __fouling_player_idref.set, None, None)

    
    # Attribute period-value uses Python identifier period_value
    __period_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-value'), 'period_value', '__AbsentNamespace0_CTD_ANON_36_period_value', pyxb.binding.datatypes.byte)
    __period_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 380, 26)
    __period_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 380, 26)
    
    period_value = property(__period_value.value, __period_value.set, None, None)

    
    # Attribute minutes-elapsed uses Python identifier minutes_elapsed
    __minutes_elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minutes-elapsed'), 'minutes_elapsed', '__AbsentNamespace0_CTD_ANON_36_minutes_elapsed', pyxb.binding.datatypes.byte)
    __minutes_elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 381, 26)
    __minutes_elapsed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 381, 26)
    
    minutes_elapsed = property(__minutes_elapsed.value, __minutes_elapsed.set, None, None)

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__AbsentNamespace0_CTD_ANON_36_timestamp', pyxb.binding.datatypes.time)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 382, 26)
    __timestamp._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 382, 26)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Attribute x1 uses Python identifier x1
    __x1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x1'), 'x1', '__AbsentNamespace0_CTD_ANON_36_x1', pyxb.binding.datatypes.float)
    __x1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 383, 26)
    __x1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 383, 26)
    
    x1 = property(__x1.value, __x1.set, None, None)

    
    # Attribute y1 uses Python identifier y1
    __y1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y1'), 'y1', '__AbsentNamespace0_CTD_ANON_36_y1', pyxb.binding.datatypes.float)
    __y1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 384, 26)
    __y1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 384, 26)
    
    y1 = property(__y1.value, __y1.set, None, None)

    
    # Attribute x2 uses Python identifier x2
    __x2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x2'), 'x2', '__AbsentNamespace0_CTD_ANON_36_x2', pyxb.binding.datatypes.string)
    __x2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 385, 26)
    __x2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 385, 26)
    
    x2 = property(__x2.value, __x2.set, None, None)

    
    # Attribute y2 uses Python identifier y2
    __y2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y2'), 'y2', '__AbsentNamespace0_CTD_ANON_36_y2', pyxb.binding.datatypes.string)
    __y2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 386, 26)
    __y2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 386, 26)
    
    y2 = property(__y2.value, __y2.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fouled_team_idref.name() : __fouled_team_idref,
        __id.name() : __id,
        __fouled_player_idref.name() : __fouled_player_idref,
        __fouling_team_idref.name() : __fouling_team_idref,
        __fouling_player_idref.name() : __fouling_player_idref,
        __period_value.name() : __period_value,
        __minutes_elapsed.name() : __minutes_elapsed,
        __timestamp.name() : __timestamp,
        __x1.name() : __x1,
        __y1.name() : __y1,
        __x2.name() : __x2,
        __y2.name() : __y2
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 392, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute team-idref uses Python identifier team_idref
    __team_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'team-idref'), 'team_idref', '__AbsentNamespace0_CTD_ANON_37_team_idref', pyxb.binding.datatypes.string)
    __team_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 395, 26)
    __team_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 395, 26)
    
    team_idref = property(__team_idref.value, __team_idref.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_37_id', pyxb.binding.datatypes.short)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 396, 26)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 396, 26)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute recipient-idref uses Python identifier recipient_idref
    __recipient_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'recipient-idref'), 'recipient_idref', '__AbsentNamespace0_CTD_ANON_37_recipient_idref', pyxb.binding.datatypes.string)
    __recipient_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 397, 26)
    __recipient_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 397, 26)
    
    recipient_idref = property(__recipient_idref.value, __recipient_idref.set, None, None)

    
    # Attribute recipient-type uses Python identifier recipient_type
    __recipient_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'recipient-type'), 'recipient_type', '__AbsentNamespace0_CTD_ANON_37_recipient_type', pyxb.binding.datatypes.string)
    __recipient_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 398, 26)
    __recipient_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 398, 26)
    
    recipient_type = property(__recipient_type.value, __recipient_type.set, None, None)

    
    # Attribute penalty-level uses Python identifier penalty_level
    __penalty_level = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'penalty-level'), 'penalty_level', '__AbsentNamespace0_CTD_ANON_37_penalty_level', pyxb.binding.datatypes.string)
    __penalty_level._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 399, 26)
    __penalty_level._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 399, 26)
    
    penalty_level = property(__penalty_level.value, __penalty_level.set, None, None)

    
    # Attribute period-value uses Python identifier period_value
    __period_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-value'), 'period_value', '__AbsentNamespace0_CTD_ANON_37_period_value', pyxb.binding.datatypes.byte)
    __period_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 400, 26)
    __period_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 400, 26)
    
    period_value = property(__period_value.value, __period_value.set, None, None)

    
    # Attribute minutes-elapsed uses Python identifier minutes_elapsed
    __minutes_elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minutes-elapsed'), 'minutes_elapsed', '__AbsentNamespace0_CTD_ANON_37_minutes_elapsed', pyxb.binding.datatypes.byte)
    __minutes_elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 401, 26)
    __minutes_elapsed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 401, 26)
    
    minutes_elapsed = property(__minutes_elapsed.value, __minutes_elapsed.set, None, None)

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__AbsentNamespace0_CTD_ANON_37_timestamp', pyxb.binding.datatypes.time)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 402, 26)
    __timestamp._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 402, 26)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Attribute x1 uses Python identifier x1
    __x1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x1'), 'x1', '__AbsentNamespace0_CTD_ANON_37_x1', pyxb.binding.datatypes.string)
    __x1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 403, 26)
    __x1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 403, 26)
    
    x1 = property(__x1.value, __x1.set, None, None)

    
    # Attribute y1 uses Python identifier y1
    __y1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y1'), 'y1', '__AbsentNamespace0_CTD_ANON_37_y1', pyxb.binding.datatypes.string)
    __y1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 404, 26)
    __y1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 404, 26)
    
    y1 = property(__y1.value, __y1.set, None, None)

    
    # Attribute x2 uses Python identifier x2
    __x2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x2'), 'x2', '__AbsentNamespace0_CTD_ANON_37_x2', pyxb.binding.datatypes.string)
    __x2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 405, 26)
    __x2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 405, 26)
    
    x2 = property(__x2.value, __x2.set, None, None)

    
    # Attribute y2 uses Python identifier y2
    __y2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y2'), 'y2', '__AbsentNamespace0_CTD_ANON_37_y2', pyxb.binding.datatypes.string)
    __y2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 406, 26)
    __y2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 406, 26)
    
    y2 = property(__y2.value, __y2.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __team_idref.name() : __team_idref,
        __id.name() : __id,
        __recipient_idref.name() : __recipient_idref,
        __recipient_type.name() : __recipient_type,
        __penalty_level.name() : __penalty_level,
        __period_value.name() : __period_value,
        __minutes_elapsed.name() : __minutes_elapsed,
        __timestamp.name() : __timestamp,
        __x1.name() : __x1,
        __y1.name() : __y1,
        __x2.name() : __x2,
        __y2.name() : __y2
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 412, 23)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute team-idref uses Python identifier team_idref
    __team_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'team-idref'), 'team_idref', '__AbsentNamespace0_CTD_ANON_38_team_idref', pyxb.binding.datatypes.string)
    __team_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 415, 26)
    __team_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 415, 26)
    
    team_idref = property(__team_idref.value, __team_idref.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_38_id', pyxb.binding.datatypes.short)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 416, 26)
    __id._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 416, 26)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute player-offside-idref uses Python identifier player_offside_idref
    __player_offside_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-offside-idref'), 'player_offside_idref', '__AbsentNamespace0_CTD_ANON_38_player_offside_idref', pyxb.binding.datatypes.string)
    __player_offside_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 417, 26)
    __player_offside_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 417, 26)
    
    player_offside_idref = property(__player_offside_idref.value, __player_offside_idref.set, None, None)

    
    # Attribute player-passing-idref uses Python identifier player_passing_idref
    __player_passing_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-passing-idref'), 'player_passing_idref', '__AbsentNamespace0_CTD_ANON_38_player_passing_idref', pyxb.binding.datatypes.string)
    __player_passing_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 418, 26)
    __player_passing_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 418, 26)
    
    player_passing_idref = property(__player_passing_idref.value, __player_passing_idref.set, None, None)

    
    # Attribute period-value uses Python identifier period_value
    __period_value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-value'), 'period_value', '__AbsentNamespace0_CTD_ANON_38_period_value', pyxb.binding.datatypes.byte)
    __period_value._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 419, 26)
    __period_value._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 419, 26)
    
    period_value = property(__period_value.value, __period_value.set, None, None)

    
    # Attribute minutes-elapsed uses Python identifier minutes_elapsed
    __minutes_elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minutes-elapsed'), 'minutes_elapsed', '__AbsentNamespace0_CTD_ANON_38_minutes_elapsed', pyxb.binding.datatypes.byte)
    __minutes_elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 420, 26)
    __minutes_elapsed._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 420, 26)
    
    minutes_elapsed = property(__minutes_elapsed.value, __minutes_elapsed.set, None, None)

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timestamp'), 'timestamp', '__AbsentNamespace0_CTD_ANON_38_timestamp', pyxb.binding.datatypes.time)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 421, 26)
    __timestamp._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 421, 26)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Attribute x1 uses Python identifier x1
    __x1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x1'), 'x1', '__AbsentNamespace0_CTD_ANON_38_x1', pyxb.binding.datatypes.string)
    __x1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 422, 26)
    __x1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 422, 26)
    
    x1 = property(__x1.value, __x1.set, None, None)

    
    # Attribute y1 uses Python identifier y1
    __y1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y1'), 'y1', '__AbsentNamespace0_CTD_ANON_38_y1', pyxb.binding.datatypes.string)
    __y1._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 423, 26)
    __y1._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 423, 26)
    
    y1 = property(__y1.value, __y1.set, None, None)

    
    # Attribute x2 uses Python identifier x2
    __x2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x2'), 'x2', '__AbsentNamespace0_CTD_ANON_38_x2', pyxb.binding.datatypes.string)
    __x2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 424, 26)
    __x2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 424, 26)
    
    x2 = property(__x2.value, __x2.set, None, None)

    
    # Attribute y2 uses Python identifier y2
    __y2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y2'), 'y2', '__AbsentNamespace0_CTD_ANON_38_y2', pyxb.binding.datatypes.string)
    __y2._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 425, 26)
    __y2._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 425, 26)
    
    y2 = property(__y2.value, __y2.set, None, None)

    
    # Attribute action-type uses Python identifier action_type
    __action_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'action-type'), 'action_type', '__AbsentNamespace0_CTD_ANON_38_action_type', pyxb.binding.datatypes.string)
    __action_type._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 426, 26)
    __action_type._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 426, 26)
    
    action_type = property(__action_type.value, __action_type.set, None, None)

    
    # Attribute player-idref uses Python identifier player_idref
    __player_idref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'player-idref'), 'player_idref', '__AbsentNamespace0_CTD_ANON_38_player_idref', pyxb.binding.datatypes.string)
    __player_idref._DeclarationLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 427, 26)
    __player_idref._UseLocation = pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 427, 26)
    
    player_idref = property(__player_idref.value, __player_idref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __team_idref.name() : __team_idref,
        __id.name() : __id,
        __player_offside_idref.name() : __player_offside_idref,
        __player_passing_idref.name() : __player_passing_idref,
        __period_value.name() : __period_value,
        __minutes_elapsed.name() : __minutes_elapsed,
        __timestamp.name() : __timestamp,
        __x1.name() : __x1,
        __y1.name() : __y1,
        __x2.name() : __x2,
        __y2.name() : __y2,
        __action_type.name() : __action_type,
        __player_idref.name() : __player_idref
    })



sports_content = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sports-content'), CTD_ANON, documentation='Copyright (c) 2003 - 2011 proFILE Computersysteme GmbH.\n\t\t\t\tAll Rights Reserved.\n\t\t\t\tproFILE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE SUITABILITY OF\n\t\t\t\tTHE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE\n\t\t\t\tIMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE,\n\t\t\t\tOR NON-INFRINGEMENT. proFILE SHALL NOT BE LIABLE FOR ANY DAMAGES SUFFERED\n\t\t\t\tBY LICENSEE AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE\n\t\t\t\tOR ITS DERIVATIVES.', location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 2, 1))
Namespace.addCategoryObject('elementBinding', sports_content.name().localName(), sports_content)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-metadata'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 15, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tournament'), CTD_ANON_4, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 43, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 15, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'tournament')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 43, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-title'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 18, 7)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-content-codes'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 19, 7)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-title')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 18, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-content-codes')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 19, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-content-code'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 22, 10)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 22, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-content-code')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 22, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tournament-metadata'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 46, 7)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tournament-division'), CTD_ANON_6, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 59, 7)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'tournament-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 46, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'tournament-division')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 59, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_3()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tournament-division-metadata'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 62, 10)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tournament-round'), CTD_ANON_8, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 73, 10)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'tournament-division-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 62, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'tournament-round')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 73, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_4()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sports-event'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 76, 13)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'sports-event')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 76, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_5()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'event-metadata'), CTD_ANON_10, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 79, 16)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team'), CTD_ANON_13, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 116, 16)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'officials'), CTD_ANON_24, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 216, 16)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'event-actions'), CTD_ANON_28, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 247, 16)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 116, 16))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'event-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 79, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'team')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 116, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'officials')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 216, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'event-actions')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 247, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_6()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'event-metadata-soccer'), CTD_ANON_11, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 82, 19)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'event-metadata-soccer')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 82, 19))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_7()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time-adjustment'), CTD_ANON_12, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 85, 22)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'time-adjustment')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 85, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_8()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team-metadata'), CTD_ANON_14, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 119, 19)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'team-stats'), CTD_ANON_16, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 140, 19)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'player'), CTD_ANON_18, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 157, 19)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'associate'), CTD_ANON_21, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 188, 19)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 157, 19))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'team-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 119, 19))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'team-stats')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 140, 19))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'player')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 157, 19))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'associate')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 188, 19))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_9()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), CTD_ANON_15, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 122, 22)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 122, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_10()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sub-score'), CTD_ANON_17, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 143, 22)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 143, 22))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'sub-score')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 143, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_11()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'player-metadata'), CTD_ANON_19, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 160, 22)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'player-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 160, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_12()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), CTD_ANON_20, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 163, 25)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 163, 25))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_13()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'associate-metadata'), CTD_ANON_22, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 191, 22)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'associate-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 191, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_14()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), CTD_ANON_23, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 194, 25)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 194, 25))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_15()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'official'), CTD_ANON_25, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 219, 19)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(None, 'official')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 219, 19))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_16()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'official-metadata'), CTD_ANON_26, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 222, 22)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, 'official-metadata')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 222, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_17()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), CTD_ANON_27, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 225, 25)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 225, 25))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_18()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'event-actions-soccer'), CTD_ANON_29, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 250, 19)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(None, 'event-actions-soccer')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 250, 19))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_19()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'action-soccer-other'), CTD_ANON_30, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 253, 22)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'action-soccer-score-attempt'), CTD_ANON_32, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 302, 22)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'action-soccer-score'), CTD_ANON_34, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 334, 22)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'action-soccer-foul'), CTD_ANON_36, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 371, 22)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'action-soccer-penalty'), CTD_ANON_37, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 391, 22)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'action-soccer-offside'), CTD_ANON_38, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 411, 22)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 252, 21))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 253, 22))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 302, 22))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 334, 22))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 371, 22))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 391, 22))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 411, 22))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'action-soccer-other')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 253, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'action-soccer-score-attempt')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 302, 22))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'action-soccer-score')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 334, 22))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'action-soccer-foul')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 371, 22))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'action-soccer-penalty')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 391, 22))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'action-soccer-offside')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 411, 22))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_20()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'info'), CTD_ANON_31, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 256, 25)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 256, 25))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'info')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 256, 25))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_21()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'action-soccer-assisting-player'), CTD_ANON_33, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 305, 25)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(None, 'action-soccer-assisting-player')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 305, 25))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_22()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'action-soccer-assisting-player'), CTD_ANON_35, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 337, 25)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 337, 25))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(None, 'action-soccer-assisting-player')), pyxb.utils.utility.Location('/home/kostadin/Desktop/soccer/memmert/data/actions.xsd', 337, 25))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_23()

